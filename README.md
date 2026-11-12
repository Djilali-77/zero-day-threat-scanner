# 🛡️ ZeroDay Detector IsolationForest

![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker&logoColor=white)
![React](https://img.shields.io/badge/React-Frontend-61DAFB?logo=react&logoColor=black)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?logo=fastapi&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/ML-Isolation_Forest-F7931E?style=flat&logo=scikit-learn&logoColor=white)


An End-to-End, Full-Stack MLOps project that leverages Unsupervised Machine Learning (**Isolation Forest**) to detect Zero-Day network threats and anomalous traffic. Trained on the **NSL-KDD** dataset, this system features a FastAPI backend, a modern React (Vite) SOC dashboard, and is fully containerized using **Docker** for seamless production deployment.

## 🌟 Key Features
- **Dual-Mode Scanning:** Users can manually input 7 critical network parameters via an interactive form or upload a CSV file for batch processing.
- **Smart "Ghost Packet" Imputation:** To improve User Experience (UX) without sacrificing model accuracy, the API dynamically injects a "Ghost Packet" baseline. This handles the missing 34 features seamlessly in the background, allowing the user to provide only the 7 most important metrics.
- **Dockerized Architecture:** The entire stack (React frontend and FastAPI backend) is containerized, eliminating version conflicts and ensuring "it works on my machine" is a thing of the past.

## 🏗️ System Architecture
The machine learning pipeline is built with a modular, production-ready design:
1. **DataLoader:** Ingests the NSL-KDD dataset and transforms it into Pandas DataFrames.
2. **Preprocessor:** Handles data cleaning, feature scaling (StandardScaler), and categorical encoding.
3. **AnomalyDetector:** The core Engine powered by an `Isolation Forest` model to classify traffic.
4. **Evaluator:** Calculates real-world metrics (Recall, Precision, F1-Score) to monitor model health.

## 🧠 MLOps & Engineering Challenges Solved
- **Preventing Data Leakage:** Initially, the model achieved an unrealistic 99% recall. I identified this as a data leakage issue (evaluating on features the model had already seen) and refactored the pipeline to implement strict train/test splitting, ensuring genuine zero-day threat detection.
- **Tuning for Real-World Scenarios (Alert Fatigue):** The default academic contamination rate (`0.5`) resulted in high false positives, acting like an overly paranoid firewall. I adjusted the `contamination` hyperparameter to `0.05` to reflect realistic, real-world network attack frequencies and balance the data.

## 🛠️ Tech Stack

| Domain | Technologies Used |
| :--- | :--- |
| **Machine Learning** | Python, Scikit-Learn, Pandas, Numpy, Joblib (`Isolation Forest`) |
| **Backend API** | FastAPI, Uvicorn, Python-Multipart |
| **Frontend Dashboard**| React.js (Vite), TailwindCSS, Framer Motion, Axios |
| **DevOps / Deployment** | Docker, Docker-Compose |

## 🚀 How to Run the Project

Because the entire application is containerized, you don't need to install Python, Node.js, or any dependencies on your local machine.

### Prerequisites
- [Docker](https://www.docker.com/products/docker-desktop/) installed and running on your machine.

### Installation & Execution
1. **Clone the repository:**
   ```bash
   git clone https://github.com/Djilali-77/zero-day-threat-scanner.git
   cd zero-day-threat-scanner
   ```

2. **Build and start the application:**
   ```bash
   docker-compose up --build
   ```

3. **Access the application:**
   - **Frontend Dashboard:** Open your browser and navigate to 👉 `http://localhost:5173`
   - **Backend API (Swagger UI):** Open your browser and navigate to 👉 `http://localhost:8000/docs`

> **Note for Mac users:** If Safari fails to connect to `localhost:5173`, simply use `http://127.0.0.1:5173` instead.

### 🛑 How to Stop the Application
To safely shut down the containers and free up the ports, press `Ctrl+C` in the terminal, then run:
```bash
docker-compose down
```