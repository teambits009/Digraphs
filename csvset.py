import pandas as pd
import re

def extract_words_with_digraphs_from_csv(csv_file_path, target_digraphs, text_columns):
    """
    Extract words containing specific Swahili digraphs from a CSV file.

    Parameters:
    - csv_file_path: str, path to the CSV file.
    - target_digraphs: list of str, digraphs to search for in words.
    - text_columns: list of str, column names in the CSV file that contain text.

    Returns:
    - List of words containing any of the target digraphs.
    """
    # Read the CSV file
    df = pd.read_csv(csv_file_path)

    # Initialize a list to store words containing target digraphs
    words_with_digraphs = []

    # Iterate over each specified text column
    for column in text_columns:
        if column in df.columns:
            # Iterate over each row in the specified column
            for text in df[column].dropna():
                # Split the text into words
                words = re.findall(r'\b\w+\b', text)
                # Check each word for the presence of any target digraph
                for word in words:
                    if any(digraph in word for digraph in target_digraphs):
                        words_with_digraphs.append(word)

    return words_with_digraphs

# Example usage
csv_file_path = r"C:\Users\HP\Desktop\Tairus Project\train.csv"
target_digraphs = ["ch", "dh", "gh", "kh", "ng", "ny", "sh", "th"]
text_columns = ["path", "sentence"]  # Replace with actual column names from your CSV

# Extract words with specified digraphs
words_with_digraphs = extract_words_with_digraphs_from_csv(csv_file_path, target_digraphs, text_columns)

# Print the result
print("Words containing the specified digraphs found in CSV document:")
for word in words_with_digraphs:
    print(word)
