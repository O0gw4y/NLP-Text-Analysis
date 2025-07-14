import pandas as pd
import spacy
from textblob import TextBlob

# Load spaCy's English model
nlp = spacy.load("en_core_web_sm")

def analyze_text(text):
    """Perform advanced NLP analysis using spaCy"""
    doc = nlp(text)
    
    # POS Tagging with detailed morphology
    pos_tags = [(token.text, token.pos_, token.tag_, token.dep_) for token in doc]
    
    # Named Entity Recognition
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    
    # Lemmatization
    lemmas = [token.lemma_ for token in doc if not token.is_stop]
    
    # Dependency Parsing
    dependencies = [(token.text, token.dep_, token.head.text) for token in doc]
    
    return {
        "pos_tags": pos_tags,
        "entities": entities,
        "lemmas": lemmas,
        "dependencies": dependencies
    }

def get_sentiment(text):
    """Returns polarity and subjectivity of the text using TextBlob."""
    blob = TextBlob(text)
    return blob.sentiment.polarity, blob.sentiment.subjectivity

def save_enhanced_results(original_df, output_file="final.xlsx"):
    """Save all NLP analysis to Excel with multiple sheets"""
    
    # Extract processed text
    processed_text = original_df["Processed Text"].iloc[0]
    
    # Perform analysis
    analysis = analyze_text(processed_text)
    
    # Sentiment Analysis
    polarity, subjectivity = get_sentiment(processed_text)
    sentiment_df = pd.DataFrame({
        "Metric": ["Polarity", "Subjectivity"],
        "Value": [polarity, subjectivity]
    })
    
    # Convert results to DataFrames
    df_pos = pd.DataFrame(analysis["pos_tags"], 
                          columns=["Token", "POS", "Detailed_POS", "Dependency"])
    
    df_ner = pd.DataFrame(analysis["entities"], 
                          columns=["Entity", "Label"])
    
    df_lemmas = pd.DataFrame({"Lemmas": analysis["lemmas"]})
    
    df_deps = pd.DataFrame(analysis["dependencies"],
                           columns=["Token", "Dependency", "Head"])
    
    # Save all to Excel with multiple sheets
    with pd.ExcelWriter(output_file) as writer:
        original_df.to_excel(writer, sheet_name="Original Data", index=False)
        df_pos.to_excel(writer, sheet_name="POS Tags", index=False)
        df_ner.to_excel(writer, sheet_name="Named Entities", index=False)
        df_lemmas.to_excel(writer, sheet_name="Lemmas", index=False)
        df_deps.to_excel(writer, sheet_name="Dependencies", index=False)
        sentiment_df.to_excel(writer, sheet_name="Sentiment", index=False)
    
    print(f"✅ Enhanced NLP analysis saved to '{output_file}'")

# === Main Execution ===
if __name__ == "__main__":
    input_excel = "processed_text.xlsx"  # Ensure this file exists
    df = pd.read_excel(input_excel)
    save_enhanced_results(df)
