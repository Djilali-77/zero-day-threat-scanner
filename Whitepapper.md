# A Lightweight Unsupervised Approach for Zero-Day Network Anomaly Detection using Isolation Forest and Ghost Packet Imputation

**Abstract**
As cyber threats continuously evolve in complexity, zero-day attacks have become a critical challenge for modern network security systems. Existing intrusion detection models are often computationally expensive, prone to high false-positive rates (alert fatigue), and strictly require complete high-dimensional traffic data for inference. To address these limitations, this paper presents a lightweight, unsupervised anomaly detection system based on the Isolation Forest algorithm. To enhance usability and inference speed, we introduce a "Ghost Packet" imputation technique, allowing the model to accurately evaluate network traffic using only a minimal subset of essential features. The entire architecture is deployed as a containerized, full-stack application. Experimental evaluation demonstrates robust Recall and F1-scores, while a strictly designed preprocessing pipeline successfully mitigates data leakage, ensuring reliable zero-day threat detection in real-world scenarios.

---

### 1. Introduction
In 2025, the cybersecurity landscape witnessed a record-breaking exploitation of 90 zero-day vulnerabilities, underscoring a critical shift in the modern threat ecosystem. Traditional, signature-based defense mechanisms, such as conventional firewalls and antivirus software, are no longer sufficient to secure complex IT infrastructures against these novel threats. This escalating danger necessitates the deployment of adaptive defense perimeters powered by Machine Learning (ML), capable of dynamically scanning, learning, and identifying previously unseen attack vectors.

Despite the potential of ML in cybersecurity, real-world deployment faces significant operational hurdles. Chief among these is the phenomenon of "alert fatigue" experienced by Security Operations Center (SOC) analysts. This fatigue is driven by the high false-positive rates (FPR) of hypersensitive anomaly detection models that often misclassify benign network anomalies or human errors as malicious activities. Furthermore, many existing models enforce strict dimensionality requirements, demanding complete, high-dimensional feature sets to process network traffic. This rigid prerequisite severely limits real-time inference and degrades the overall operational experience during manual threat hunting.

To overcome these challenges, this paper proposes an efficient anomaly detection architecture leveraging the Isolation Forest (iForest) algorithm, renowned for its low computational overhead and rapid isolation of outliers. To resolve the strict feature dependency, we introduce a "Ghost Packet" imputation methodology, enabling SOC analysts to perform high-efficiency traffic scans using only a minimal subset of critical features. Finally, the system is wrapped in a modern, containerized dashboard that seamlessly handles both batch CSV processing and manual data entry, bridging the gap between advanced ML algorithms and practical SOC usability.

---

### 2. Methodology

**2.1. Dataset and Preprocessing Pipeline**
The proposed model is trained and evaluated using the benchmark NSL-KDD dataset. To ensure robust model performance, a rigorous preprocessing pipeline was established. Initial data cleaning involved the detection and handling of missing values (NaNs). To guarantee that the model evaluates all network parameters equally without being skewed by large-magnitude attributes, feature scaling was applied using `StandardScaler`. Furthermore, categorical features were transformed via categorical encoding techniques to ensure a strictly numerical feature space. Crucially, to prevent data leakage and ensure authentic evaluation of zero-day detection capabilities, the dataset was strictly partitioned into independent training and testing subsets prior to any model training.

**2.2. Core Algorithm: Isolation Forest**
The anomaly detection engine is powered by the Isolation Forest (iForest) algorithm. Unlike traditional models that attempt to profile the dense regions of normal traffic, iForest explicitly isolates anomalies by constructing isolation trees. This approach grants the algorithm a highly efficient computational complexity of $O(n)$, making it exceptionally well-suited for high-throughput network environments. Initially, the contamination parameter (the expected proportion of outliers) was set to an academic default of `0.5`. However, empirical observation revealed that this yielded an unacceptably high false-positive rate. To calibrate the model for real-world deployment and balance the anomaly threshold, the contamination parameter was iteratively optimized.

**2.3. Ghost Packet Imputation Strategy**
A primary barrier to deploying ML models in real-time Security Operations Centers (SOC) is the strict requirement for complete feature vectors (e.g., all 41 features of the NSL-KDD dataset). To dramatically improve the user experience and reduce cognitive load on SOC analysts, this paper introduces a novel "Ghost Packet" imputation strategy. This technique allows operators to manually input a minimal subset of the 7 most critical network features. The underlying backend dynamically synthesizes the remaining 34 features using carefully calculated baseline values derived from normal traffic distributions. This ensures the model receives a mathematically complete tensor for inference without blocking, failing, or requiring exhaustive manual data entry.

---

### 3. Evaluation and Results

**3.1. Mitigating Data Leakage and Overfitting**
During initial empirical testing, the model achieved an anomalously high Recall of 99%. Rather than accepting this as optimal performance, a rigorous code review was initiated, which identified a critical data leakage vulnerability: the model was inadvertently being evaluated on a subset of the data it had seen during the training phase. By correcting this leakage—enforcing a strict train/test split—the model yielded a true Recall of 68.66% and an F1-Score of 76.72%. This correction is paramount, as it proves the model's authentic capability to detect approximately 70% of genuine, unseen zero-day attacks without the deceptive inflation of overfitting.

**3.2. Hyperparameter Tuning for Alert Fatigue**
The adjustment of the contamination parameter played a critical role in the system's operational viability. While initial testing with a theoretical `0.05` contamination threshold resulted in severe underperformance (Recall: 14.39%, F1-Score: 24.49%), iterative empirical tuning demonstrated that a parameter of `0.3` provided the optimal mathematical equilibrium. This tuned threshold effectively minimized the False Positive Rate (FPR), ensuring that SOC analysts are not overwhelmed by alert fatigue while maintaining a robust detection rate for anomalous traffic.

---

### 4. Conclusion and Future Work
This paper presented a practical, lightweight machine learning architecture utilizing the Isolation Forest algorithm to detect zero-day network threats and anomalous traffic. By actively resolving data leakage vulnerabilities and implementing a novel "Ghost Packet" feature imputation strategy, the system achieves a strong balance between reliable threat detection and optimal user experience for security analysts. 

In future work, we plan to evolve this static model into a robust Continual Learning pipeline. Specifically, we aim to implement mathematical drift detection mechanisms, such as Kullback-Leibler (KL) Divergence, to automatically recognize Concept Drift in live network environments, while simultaneously integrating defensive constraints to protect the retraining pipeline against adversarial Data Poisoning attacks.