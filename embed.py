import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.util import ngrams
from nltk.sentiment import SentimentIntensityAnalyzer
import gensim
from gensim.models import Word2Vec
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation
import spacy
import pandas as pd
import numpy as np
from textblob import TextBlob

# Download NLTK resources (uncomment if not downloaded)
# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('vader_lexicon')

def read_text_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

# Example usage: Provide the path to your document here
document_path = ''
text = read_text_from_file(document_path)

# Tokenization and stopwords removal
tokens = word_tokenize(text.lower())
stop_words = set(stopwords.words('english'))
filtered_tokens = [word for word in tokens if word.isalnum() and word not in stop_words]

# N-grams
n = 3
text_ngrams = list(ngrams(filtered_tokens, n))

# TF-IDF
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform([text])
tfidf_features = tfidf_vectorizer.get_feature_names_out()

# Word Embeddings (using Word2Vec)
word2vec_model = Word2Vec([filtered_tokens], vector_size=100, window=5, min_count=1, sg=1)
word_embeddings = {word: word2vec_model.wv[word] for word in filtered_tokens if word in word2vec_model.wv}

# Sentiment Analysis
sentiment_analyzer = SentimentIntensityAnalyzer()
sentiment_scores = sentiment_analyzer.polarity_scores(text)

# POS Tagging and Frequencies
pos_tagged = nltk.pos_tag(filtered_tokens)
pos_frequencies = nltk.FreqDist(tag for (word, tag) in pos_tagged)

# Statistical Measures
word_count = len(filtered_tokens)
unique_words = len(set(filtered_tokens))
avg_word_length = np.mean([len(word) for word in filtered_tokens])

# Topic Modeling (using LDA)
lda_model = LatentDirichletAllocation(n_components=1, random_state=42)
lda_model.fit(tfidf_matrix)
topic_probabilities = lda_model.transform(tfidf_matrix)

# Print Results
print("Filtered Tokens:", filtered_tokens)
print("\nN-grams:", text_ngrams)
print("\nTF-IDF Features:", tfidf_features)
print("\nWord Embeddings:", word_embeddings)
print("\nSentiment Scores:", sentiment_scores)
print("\nPOS Tag Frequencies:", pos_frequencies.most_common())
print("\nStatistical Measures:")
print("Total Words:", word_count)
print("Unique Words:", unique_words)
print("Average Word Length:", avg_word_length)
print("\nTopic Model Probabilities:", topic_probabilities)
