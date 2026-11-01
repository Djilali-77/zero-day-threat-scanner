from src.data_loader import DataLoader
from src.preprocessor import Preprocessor
from src.anomaly_model import AnomalyDetector
from src.evaluator import Evaluator
import time
import os

def main():

    nsl_kdd_columns = [
            "duration", "protocol_type", "service", "flag", "src_bytes", "dst_bytes", 
            "land", "wrong_fragment", "urgent", "hot", "num_failed_logins", 
            "logged_in", "num_compromised", "root_shell", "su_attempted", "num_root", 
            "num_file_creations", "num_shells", "num_access_files", "num_outbound_cmds", 
            "is_host_login", "is_guest_login", "count", "srv_count", "serror_rate", 
            "srv_serror_rate", "rerror_rate", "srv_rerror_rate", "same_srv_rate", 
            "diff_srv_rate", "srv_diff_host_rate", "dst_host_count", "dst_host_srv_count", 
            "dst_host_same_srv_rate", "dst_host_diff_srv_rate", "dst_host_same_src_port_rate", 
            "dst_host_srv_diff_host_rate", "dst_host_serror_rate", "dst_host_srv_serror_rate", 
            "dst_host_rerror_rate", "dst_host_srv_rerror_rate", "label", "difficulty_level"
        ]    
    
    train_loader = DataLoader(file_path="data/KDDTrain+.txt", column_names=nsl_kdd_columns)
    preprocessor = Preprocessor()
    detector = AnomalyDetector()
    evaluator = Evaluator()

    df_train = train_loader.load_data()
    df_clean = preprocessor.remove_missing(df_train)
    x, y = preprocessor.fit_transform_train(df_clean)
    
    print("X_train shape:", x.shape)
    print("y_train shape:", y.shape)


    print("Training Isolation Forest...")
    start_train = time.time()
    detector.train(x)
    train_time = time.time() - start_train
    print(f"Training completed in {round(train_time, 2)} seconds!")

    print("Predicting anomalies...")
    start_predict = time.time()
    preds = detector.predict(x)
    predict_time = time.time() - start_predict
    print(f"Predicted completed in {round(predict_time, 2)} seconds!")

    print(preds[:20])

    
    test_loader = DataLoader(file_path="data/KDDTest+.txt", column_names=nsl_kdd_columns)
    df_test = test_loader.load_data()
    df_test_clean = preprocessor.remove_missing(df_test)
    x_test, y_test = preprocessor.transform_test(df_test_clean)

    preds_test = detector.predict(x_test)
    evaluator.evaluate(y_test, preds_test)

    print("Saving models for production...")
    os.makedirs("models", exist_ok=True) 
    preprocessor.save("models/preprocessor.pkl")
    detector.save("models/isolation_forest.pkl")
    print("Saved successfully!")

if __name__ == "__main__":

    main()