import pandas as pd
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

def preprocess_document(file_path, encoding='latin1'):
    df = pd.read_csv(file_path, encoding=encoding)
    
    # Print the column names for debugging
    print("Columns in the CSV file:", df.columns)
    
    # Extract text data
    texts = df[['Digraphs 1', 'Digraphs 2', 'Digraphs 3']].fillna('').values
    
    combined_texts = [' '.join(text) for text in texts]
    
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(combined_texts)
    sequences = tokenizer.texts_to_sequences(combined_texts)
    
    word_index = tokenizer.word_index
    data = pad_sequences(sequences, maxlen=100)
    
    # Print the shape of the data
    print(f'Shape of padded sequences: {data.shape}')
    
    return data, word_index

# Example usage
file_path = 'Digraphs.csv'
X, word_index = preprocess_document(file_path)
print(f'Padded sequences:\n{X}')
