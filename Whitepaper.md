# Zero Day Network Anomaly Detection using iForest with Ghost Packets Imputation

## Abstract

Zero day attacks are a massive problem in the network security industry. The majority of Machine Learning models are very resource heavy, which leads to a high level of false positives. Most models also require all of the network features to be inputted which makes it difficult to carry out in real time. I have created a lightweight anomaly detection system using the Isolation Forest algorithm and have included a Ghost Packet methodology to make it practical for Security Analysts. This means that the algorithm can run with only 7 features instead of 41. Both the backend and frontend have been containerised using Docker. My final testing proved to be successful with a high Recall and F1-score. I made sure to fully follow the data pipeline to ensure no data leak occurred.

---

## 1. Introduction

In 2025 alone there were 90 zero-day vulnerabilities exploited by hackers. This is a critical metric and shows that traditional firewalls and anti-virus systems are no longer sufficient. Therefore we need to implement a Machine Learning solution.

However, in reality the majority of Machine Learning models are not preferred by the Security Analysts in the SOC due to the high amount of false positives producing ‘alert fatigue.’. The models are very sensitive which means almost everything gets flagged up. Having to manually input 41 different network features to determine if something is suspicious is not very user friendly.

The Isolation Forest algorithm works by identifying and isolating anomalies. This makes it very efficient. By only using 7 critical features, the model can analyse the data by the values input by the analyst. The rest of the features are auto filled on the backend. This has been implemented into a interactive dashboard using React and FastAPI.

---

## 2. Methodology

### 2.1 Data and Preprocessing

The model has been trained using the benchmark NSL KDD dataset. The data has been preprocessed using a clean pipeline. Any NaN values have been removed. We used StandardScaler from scikit learn to prevent any issues with the large numbers. Categorical text data has been turned into numerical values. The most important thing was that there was a strict train/test split done at the beginning of the project. This will ensure no data leak occurs.

### 2.2 Isolation Forest Model

The Isolation Forest algorithm was chosen due to its O(n) time complexity. This means it is very fast to run with network traffic. Instead of profiling normal data, random splits are made to find outliers. The default contamination rate was set to 0.5 however this resulted in a high amount of false positives. This would cause immediate alert fatigue in real life. I realised I needed to optimise this parameter.

### 2.3 Ghost Packets Imputation

The main area of engineering for this project was implementing Ghost Packets. If the model did not receive all 41 features it would crash. I used a Ghost Packet strategy. Only 7 of the most important network metrics were inputted by the user. The API would then create a Ghost Packet with the remaining 34 features. These would contain clean normal baseline values. This would complete the data array and allow the model to predict without any issues. This would make things easier for the SOC analyst.

---

## 3. Evaluation and Results

### 3.1 Preventing Data Leak

My first testing showed me that I had a 99% Recall score. I knew this wasn’t right, as such flawless results usually indicate overfitting. I checked my code and saw that I had a data leak. My model was unintentionally using data from the training phase. Once this was fixed my Recall score dropped to 68.66%. My F1-Score was 76.72%. This was a lower result but genuine. It shows that my model can detect around 70% of Zero Days without overfitting.

### 3.2 Optimising Contamination

I wanted to also improve the alert fatigue issue. I tested the model with a contamination rate of 0.05. This resulted in a very low result (Recall = 14.39%, F1-Score = 24.49%). I did some further testing and realised that by changing the contamination rate to 0.3 gave the best results. This meant there weren’t too many false positives so it could be easily managed by a human. There was still enough anomalous traffic detected to be useful.

---

### 4. Conclusion and Future Work
This project demonstrates that it is possible to build a fast, reliable Zero-Day detector if data leakage is handled properly and techniques like Ghost Packets are used to improve the software's usability.

For my future work, I want to make the model adaptable over time. I plan to add mathematical distance checks, such as KL Divergence, so the system can automatically detect Concept Drift in the network. I also want to build defenses to protect the retraining pipeline from Data Poisoning attacks.