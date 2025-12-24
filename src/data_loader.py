import pandas as pd

def load_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path, delimiter=';')
    return df
