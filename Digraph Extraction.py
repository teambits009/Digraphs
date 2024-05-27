# Install the necessary libraries

# Import required libraries
import re
import speech_recognition as sr
from pydub import AudioSegment

# Function to extract words with digraphs from audio
def extract_words_with_digraphs_from_audio(audio_file_path, target_digraphs):
    # Initialize SpeechRecognizer
    recognizer = sr.Recognizer()

    # Load audio file
    audio = AudioSegment.from_file(audio_file_path)
    audio.export("temp.wav", format="wav")

    with sr.AudioFile("temp.wav") as source:
        audio_data = recognizer.record(source)

    # Recognize speech using Google Web Speech API
    try:
        recognized_text = recognizer.recognize_google(audio_data, language="sw-TZ")
    except sr.UnknownValueError:
        print("Google Web Speech API could not understand audio")
        return []
    except sr.RequestError as e:
        print(f"Could not request results from Google Web Speech API; {e}")
        return []

    return extract_words_with_digraphs(recognized_text, target_digraphs)

# Function to extract words with digraphs from text
def extract_words_with_digraphs(text, target_digraphs):
    # Initialize a list to store words containing target digraphs
    words_with_digraphs = []

    # Find words containing target digraphs in the text
    words = text.split()
    for word in words:
        if any(digraph in word for digraph in target_digraphs):
            words_with_digraphs.append(word)

    return words_with_digraphs

# Function to extract words with digraphs from a document
def extract_words_with_digraphs_from_document(document_path, target_digraphs):
    # Read the document
    with open(document_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Extract digraphs from the text
    return extract_words_with_digraphs(text, target_digraphs)

# Example usage
audio_file_path = "example_audio.wav"
document_path = "CLN4-DEV SWAHILI DATA SETS.txt"
target_digraphs = ["ch", "dh", "gh", "kh", "ng", "ny", "sh", "th", "ng"]

audio_digraphs = extract_words_with_digraphs_from_audio(audio_file_path, target_digraphs)
print("Words containing the specified digraphs found in audio:", audio_digraphs)

document_digraphs = extract_words_with_digraphs_from_document(document_path, target_digraphs)
print("Words containing the specified digraphs found in document:", document_digraphs)
