import os
import pickle
import numpy as np
import pandas as pd
import scipy.signal as scisig
import cvxEDA

fs_dict = {'ACC': 32, 'BVP': 64, 'EDA': 4, 'TEMP': 4, 'label': 700, 'Resp': 700}
savePath = 'data'
subject_feature_path = '/subject_feats'

if not os.path.exists(savePath):
    os.makedirs(savePath)
if not os.path.exists(savePath + subject_feature_path):
    os.makedirs(savePath + subject_feature_path)


class SubjectData:

    def __init__(self, main_path, subject_number):
        self.name = f'S{subject_number}'
        self.subject_keys = ['signal', 'label', 'subject']
        self.signal_keys = ['chest', 'wrist']
        self.chest_keys = ['ACC', 'ECG', 'EMG', 'EDA', 'Temp', 'Resp']
        self.wrist_keys = ['ACC', 'BVP', 'EDA', 'TEMP']
        with open(os.path.join(main_path, self.name) + '/' + self.name + '.pkl', 'rb') as file:
            self.data = pickle.load(file, encoding='latin1')

    def get_wrist_data(self):
        data = self.data['signal']['wrist']
        data.update({'Resp': self.data['signal']['chest']['Resp']})
        return data

    def get_chest_data(self):
        return self.data['signal']['chest']


def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = scisig.butter(order, normal_cutoff, btype='low', analog=False)
    return b, a


def butter_lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = scisig.lfilter(b, a, data)
    return y


def filterSignalFIR(data, cutoff=0.4, numtaps=64):
    f = cutoff / (fs_dict['ACC'] / 2.0)
    FIR_coeff = scisig.firwin(numtaps, f)
    return scisig.lfilter(FIR_coeff, 1, data)


def process_subject_data(subject_id):
    global savePath

    subject = SubjectData(main_path='data/WESAD', subject_number=subject_id)

    e4_data_dict = subject.get_wrist_data()

    eda_df = pd.DataFrame(e4_data_dict['EDA'], columns=['EDA'])
    bvp_df = pd.DataFrame(e4_data_dict['BVP'], columns=['BVP'])
    acc_df = pd.DataFrame(e4_data_dict['ACC'], columns=['ACC_x', 'ACC_y', 'ACC_z'])
    temp_df = pd.DataFrame(e4_data_dict['TEMP'], columns=['TEMP'])
    resp_df = pd.DataFrame(e4_data_dict['Resp'], columns=['Resp'])

    eda_df['EDA'] = butter_lowpass_filter(eda_df['EDA'], 1.0, fs_dict['EDA'], 6)

    for col in acc_df.columns:
        acc_df[col] = filterSignalFIR(acc_df[col])

    eda_df.index = [(1 / fs_dict['EDA']) * i for i in range(len(eda_df))]
    bvp_df.index = [(1 / fs_dict['BVP']) * i for i in range(len(bvp_df))]
    acc_df.index = [(1 / fs_dict['ACC']) * i for i in range(len(acc_df))]
    temp_df.index = [(1 / fs_dict['TEMP']) * i for i in range(len(temp_df))]
    resp_df.index = [(1 / fs_dict['Resp']) * i for i in range(len(resp_df))]

    eda_df.index = pd.to_datetime(eda_df.index, unit='s')
    bvp_df.index = pd.to_datetime(bvp_df.index, unit='s')
    temp_df.index = pd.to_datetime(temp_df.index, unit='s')
    acc_df.index = pd.to_datetime(acc_df.index, unit='s')
    resp_df.index = pd.to_datetime(resp_df.index, unit='s')

    df = eda_df.join(bvp_df, how='outer')
    df = df.join(temp_df, how='outer')
    df = df.join(acc_df, how='outer')
    df = df.join(resp_df, how='outer')

    df.to_csv(f'{savePath}{subject_feature_path}/S{subject_id}_raw.csv')

    subject = None


def combine_files(subjects):
    df_list = []
    for s in subjects:
        df = pd.read_csv(f'{savePath}{subject_feature_path}/S{s}_raw.csv', index_col=0)
        df['subject'] = s
        df_list.append(df)

    combined_df = pd.concat(df_list)
    combined_df.reset_index(drop=True, inplace=True)
    combined_df.to_csv(f'{savePath}/combined_raw_data.csv')

    counts = combined_df['subject'].value_counts()
    print('Number of samples per subject:')
    for subject, number in zip(counts.index, counts.values):
        print(f'Subject {subject}: {number}')


if __name__ == '__main__':
    subject_ids = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17]

    for subject_id in subject_ids:
        print(f'Processing data for S{subject_id}...')
        process_subject_data(subject_id)

    combine_files(subject_ids)
    print('Processing complete.')
