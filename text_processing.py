import docx
import pandas as pd
import re
import string
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from spellchecker import SpellChecker

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

def read_word_file(filename):
    """Reads text from a Word document."""
    doc = docx.Document(filename)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return " ".join(full_text)

def preprocess_text(text):
    """Performs text preprocessing: tokenization, lowercasing, stopword removal, stemming, lemmatization, punctuation removal, and spell correction."""

    
    # Remove punctuation and special characters
    text = re.sub(f"[{string.punctuation}]", "", text)
    
    # Tokenization
    words = word_tokenize(text)
    
    # Remove stopwords
    stop_words = set(stopwords.words("english"))
    words = [word for word in words if word not in stop_words]
    
    # Spell correction
    spell = SpellChecker()
    words = [spell.correction(word) if spell.correction(word) is not None else word for word in words]
    
    # Stemming and Lemmatization
    stemmer = PorterStemmer()
    lemmatizer = WordNetLemmatizer()
    stemmed_words = [stemmer.stem(word) for word in words]
    lemmatized_words = [lemmatizer.lemmatize(word) for word in words]
    
    return " ".join(lemmatized_words)  # Returning lemmatized text

def save_to_excel(data, filename="output.xlsx"):
    """Saves processed text to an Excel file."""
    df = pd.DataFrame({"Processed Text": [data]})
    df.to_excel(filename, index=False)
    print(f"Processed text saved to {filename}")

def main():
    input_file = r"C:\New folder\user_text.docx"  # write your word doc path here(created in first step)
    output_file = r"C:\New folder\processed_text.xlsx"
    
    text = read_word_file(input_file)
    processed_text = preprocess_text(text)
    save_to_excel(processed_text, output_file)

if __name__ == "__main__":
    main()
