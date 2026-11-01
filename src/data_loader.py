import pandas as pd

class DataLoader:
    """
        Reads the data and trasnlate it to DataFrame
    """
    def __init__(self, file_path: str, column_names: list):
        self.file_path = file_path
        self.column_names = column_names
    
    def load_data(self) -> pd.DataFrame:

        data = pd.read_csv(self.file_path, header=None, names=self.column_names)
        return data