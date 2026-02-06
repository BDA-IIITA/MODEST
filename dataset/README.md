#  Datasets
The following dataset links are available-

## Modma Dataset
​The Multi-modal Open Dataset for Mental-disorder Analysis (MODMA) is a comprehensive dataset designed to facilitate the detection and analysis of mental disorders, with a particular focus on Major Depressive Disorder (MDD). It integrates electroencephalogram (EEG) recordings and speech data from individuals diagnosed with MDD and healthy control participants, providing a robust foundation for research into behavioral and neurological indicators of depression.​

**EEG Data:**

***128-Channel EEG Recordings:***

*****1. Resting-State Recordings:****** 
Collected from 24 MDD subjects and 29 healthy controls, aged between 16 and 52 years. These recordings capture brain activity during rest, offering insights into the neural patterns associated with depression.​

*****2. Event-Related Potential (ERP) Recordings:*****
Obtained from the same group of participants, these recordings measure brain responses to specific stimuli, aiding in understanding cognitive processes affected by MDD.​

*****3-Channel EEG Recordings:*****
Resting-State Recordings: Acquired from 26 MDD subjects and 29 healthy controls, aged between 16 and 56 years. These recordings utilize a wearable 3-electrode EEG device, highlighting the potential for portable and accessible depression monitoring tools.

The MODMA dataset is publicly available for research purposes is available at - https://www.kaggle.com/datasets/mimino12/modma-dataset

**Speech Data:**

Speech recordings were collected from 23 individuals diagnosed with Major Depressive Disorder (MDD) and 29 healthy controls, ranging in age from 18 to 52 years. The data was gathered through structured tasks, including interviews, reading assignments, and picture descriptions, allowing for the extraction of linguistic and emotional features relevant to mental health analysis. Table I provides an overview of the dataset, demonstrating that each data modality includes both MDD participants and healthy individuals.

**Table I: MODMA Dataset Overview**

| Modality   | Subjects                  | Method               | Features                     |
|------------|---------------------------|----------------------|------------------------------|
| **128-Ch EEG** | 53 (24 MDD, 29 Healthy) | Resting & ERP       | Brain activity              |
| **3-Ch EEG**   | 55 (26 MDD, 29 Healthy) | Resting EEG         | Neural patterns             |
| **Speech**     | 52 (23 MDD, 29 Healthy) | Interview, Reading  | Speech, Emotion             |


By offering a rich combination of EEG and speech data from both MDD patients and healthy individuals, the MODMA dataset serves as a valuable resource for advancing the understanding and detection of mental disorders.

## WESAD (Wearable Stress and Affect Detection)dataset
The WESAD dataset which is multimodal, was created for the purpose of recognizing stress and emotions through the use of wearable sensor technology. The dataset, gathered from 15 participants (12 males and 3 females) in a controlled study, encompasses three emotional states: neutral, stress, and amusement. The Trier Social Stress Test (TSST), a widely recognized method for provoking psychological stress, was used to induce stress levels
Available at - https://uni-siegen.sciebo.de/s/HGdUkoNlW1Ub0Gx

 **Table I: Summary of WESAD Dataset**

| Sensor Device  | Signals        | Description            |
|---------------|---------------|------------------------|
| **6 × RespiBAN** (Chest-Worn) | ECG  | Heart activity      |
|               | EDA  | Skin conductivity    |
|               | EMG  | Muscle activity      |
|               | RESP | Breathing patterns  |
|               | TEMP | Body temperature    |
|               | ACC  | Body movement       |
| **4 × Empatica E4** (Wrist-Worn) | BVP  | Heart rate variability |
|               | TEMP | Skin temperature    |
|               | ACC  | Wrist movement      |

Table presents an overview of the dataset, detailing the wearable sensors used and the corresponding physiological signals recorded. The dataset includes signals from a sensor worn on the chest called RespirBAN. These signals include an electrocardiogram (ECG), electrodermal activity (EDA), respiration (RESP), and electromyography (EMG). It also includes additional signals from a wrist-worn sensor (Empatica E4), such as blood volume pulse (BVP), EDA, temperature, and acceleration.




# TDBRAIN GitHub Repository  

The **TDBRAIN GitHub Repository** provides open-source tools, preprocessing pipelines, and documentation to facilitate the use of the TDBRAIN dataset. It is designed to help researchers handle **EEG signals, clinical metadata, and neuropsychological test data** efficiently, ensuring reproducibility and ease of analysis in neuroscience and mental health studies.  

---

## Code Resources  

### 1. EEG Preprocessing Pipelines  
- Scripts for **filtering, artifact removal** (e.g., eye blinks, muscle noise), **epoching**, and **feature extraction** from raw EEG signals.  
- Optimized for **TDBRAIN’s 26-channel recordings**.  

### 2. ERP and Task-Based Analysis  
- Tools for extracting **event-related potentials (ERPs)** from task-based EEG sessions.  
- Supports research into **cognitive and affective neuroscience**.  

### 3. Clinical & Cognitive Data Handling  
- Scripts for cleaning and aligning **clinical questionnaires, diagnostic labels, and neuropsychological test scores** with EEG sessions.  
- Ensures multimodal integration of EEG, clinical, and cognitive data.  

---

## 📂 Additional Resources  

- **Tutorial notebooks** for beginners and advanced users  
- **Sample workflows** to replicate published analyses  
- **Visualization tools** for EEG signals and metadata  

---

##  TDBRAIN GitHub Repository Overview  

| **Resource**         | **Description**                        | **Purpose**                                |  
|-----------------------|----------------------------------------|--------------------------------------------|  
| **EEG Preprocessing** | Filtering, artifact removal, epoching  | Prepare clean EEG signals                   |  
| **ERP Analysis**      | Task-based ERP extraction              | Study cognitive & emotional responses       |  
| **Clinical Data**     | Scripts for demographics & diagnosis   | Integrate EEG with mental health metadata   |  
| **Tutorials**         | Jupyter notebooks & examples           | Guide researchers in dataset usage          |  

---

##  Access  

The repository is **publicly available for research purposes** at: [https://github.com/BrainClinics/TDBRAIN](https://github.com/BrainClinics/TDBRAIN)  

---

##  Citation  

If you use the TDBRAIN dataset or this repository in your research, please cite the corresponding publication(s).  



## Additional Dataset links:

## SWELL dataset
The SWELL Knowledge Work (SWELL-KW) dataset comprises multimodal physiological and behavioral data collected for research on stress and user modeling. It was developed by researchers at the Institute for Computing and Information Sciences at Radboud University. The dataset originates from experiments conducted on 25 participants performing typical office tasks such as writing reports, creating presentations, reading emails, and searching for information.
Available at - https://www.kaggle.com/datasets/qiriro/swell-heart-rate-variability-hrv

During the study, participants were subjected to common workplace stressors, including unexpected email interruptions and time pressure to complete tasks. The recorded data includes computer usage logs, facial expressions, body postures, electrocardiography (ECG) signals, and skin conductance. Additionally, researchers gathered subjective assessments related to task load, mental effort, emotional state, and perceived stress. Each participant underwent three distinct working conditions:

**No Stress:** Participants worked on tasks at their own pace, with a maximum duration of 45 minutes, but without prior knowledge of this time limit.

**Time Pressure:** The available time to complete tasks was reduced to two-thirds of the time taken in the neutral condition.

**Interruption:** Participants received eight emails during their assigned tasks. Some emails were relevant and required actions, while others were unrelated distractions.

**Table I: SWELL-KW Dataset Overview**

| Modality        | Data Collected                                  | Description                                    |
|----------------|-----------------------------------------------|------------------------------------------------|
| **Physiological Data** | ECG, Skin Conductance, HRV Indices   | Captures heart activity, stress response       |
| **Behavioral Data**    | Computer Logs, Facial Expressions, Body Posture | Tracks user interactions and physical responses |
| **Self-Reports**       | Task Load, Mental Effort, Emotion, Perceived Stress | Subjective assessments of workload and stress levels |
| **Experimental Conditions** | No Stress, Time Pressure, Interruption | Different working conditions to induce stress  |
| **Participants**      | 25 subjects                            | Engaged in various office tasks                |

**HRV COMPUTATION**
Heart Rate Variability (HRV) indices were computed using the following process:
First, the inter-beat interval (IBI) signal was extracted from the peaks of the electrocardiogram (ECG) recordings for each participant. Each HRV index was then computed using a 5-minute IBI window. The process involved appending a new IBI sample to the window while removing the oldest sample from the beginning. The updated IBI array was then used to compute the next HRV index, and this cycle continued until the entire IBI signal was processed.

Unlike traditional HRV computation methods, which analyze the entire ECG signal at once, this approach enables a more granular and detailed examination of how each heartbeat influences HRV. This method provides a more accurate representation of short-term variations in autonomic nervous system activity, making it valuable for stress research and personalized user modeling.

## Mental Health eda Prediction 
Available at - https://www.kaggle.com/code/imtkaggleteam/mental-health-eda-prediction

### The Depression Dataset Analysis
Related paper- https://www.sciencedirect.com/science/article/pii/S0165032724012278#f0010

dataset- https://www.kaggle.com/datasets/arashnic/the-depression-dataset/data

code at- https://www.kaggle.com/code/ahmedalbaz031/the-depression-dataset-analysis/notebook

### The Depression Dataset
Available at - https://www.kaggle.com/datasets/arashnic/the-depression-dataset

### student depression dataset
Available at - https://www.kaggle.com/datasets/hopesb/student-depression-dataset/data

### Sentiment140 dataset with 1.6 million tweets

Used twint to collect tweets based on the following hashtags

about: https://github.com/swcwang/depression-detection?tab=readme-ov-file
https://www.kaggle.com/code/redaabdou/depression-on-social-media/input

dataset avilable at - https://www.kaggle.com/datasets/kazanova/sentiment140?resource=download
