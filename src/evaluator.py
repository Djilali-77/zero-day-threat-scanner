from sklearn.metrics import recall_score, f1_score
import pandas as pd
import numpy as np

class Evaluator:
    def evaluate(self, y_true: pd.Series, y_pred: np.ndarray):
       
        y_true_numeric = np.where(y_true == 'normal', 1 , -1)
        
        recall = recall_score(y_true_numeric, y_pred, pos_label=-1)
        f1 = f1_score(y_true_numeric, y_pred, pos_label=-1)
        
        print(f"Recall: {recall * 100:.2f}%")
        print(f"F1-Score: {f1 * 100:.2f}%")