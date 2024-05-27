import re

def extract_words_with_digraphs_from_document(document_path, target_digraphs):
    """
    Extract words containing specific Swahili digraphs from a document.
    
    Parameters:
    - document_path: str, path to the document file.
    - target_digraphs: list of str, digraphs to search for in words.
    
    Returns:
    - List of words containing any of the target digraphs.
    """
    # Read the document
    with open(document_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Split the text into words
    words = re.findall(r'\b\w+\b', text)

    # Initialize a list to store words containing target digraphs
    words_with_digraphs = []

    # Check each word for the presence of any target digraph
    for word in words:
        if any(digraph in word for digraph in target_digraphs):
            words_with_digraphs.append(word)

    return words_with_digraphs

# Example usage
document_path = "CLN4-DEV SWAHILI DATA SETS.txt"
target_digraphs = ["ch", "dh", "gh", "kh", "ng", "ny", "sh", "th"]

# Extract words with specified digraphs
words_with_digraphs = extract_words_with_digraphs_from_document(document_path, target_digraphs)

# Print the result
print("Words containing the specified digraphs found in document:")
for word in words_with_digraphs:
    print(word)
