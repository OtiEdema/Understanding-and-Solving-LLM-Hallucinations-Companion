import pandas as pd

def preprocess_text_data(file_path):
    data = pd.read_csv(file_path)
    data.dropna(inplace=True)
    data['text'] = data['text'].apply(lambda x: x.lower())
    return data
