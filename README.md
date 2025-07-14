Here's a complete, professional `README.md` file for your project that explains:

* What your project does (NLP pipeline)
* How to set it up and run it on **Windows** and **Kali Linux**
* What each script does
* How to use the tool effectively

---

## 📄 README.md

````markdown
# 🧠 NLP Text Analysis Tool (POS, NER, Lemmatization, Sentiment)

This is a multi-step **Natural Language Processing (NLP)** pipeline that allows users to:

1. Input and save text via CLI (`user_data.py`)
2. Preprocess the text (cleaning, tokenizing, lemmatizing) and export to Excel (`text_processing.py`)
3. Perform advanced NLP analysis including:
   - POS Tagging
   - Named Entity Recognition (NER)
   - Lemmatization
   - Dependency Parsing
   - Sentiment Analysis (polarity and subjectivity)

---

## 📂 Project Structure

```bash
📁 your-project-folder/
├── user_data.py            # Accepts user input and saves to a Word doc
├── text_processing.py      # Preprocesses the Word doc and saves to Excel
├── NER & POS.py            # Performs full NLP + sentiment analysis and saves to final Excel
├── requirements.txt        # All required Python dependencies
├── user_text.docx          # Generated from step 1
├── processed_text.xlsx     # Output from step 2
└── final.xlsx              # Final NLP output (multi-sheet Excel)
````

---

## ⚙️ Requirements

Python version: **Python 3.9+ recommended**

All dependencies are listed in `requirements.txt`:

```text
spacy==3.7.4
textblob==0.17.1
pandas==2.1.4
python-docx==0.8.11
nltk==3.8.1
spellchecker==0.7.1
openpyxl==3.1.2
```

---

## 🖥️ How to Run

### ✅ On **Windows**:

1. Open PowerShell and navigate to your project folder:

   ```powershell
   cd "C:\path\to\your\project"
   ```

2. Create a virtual environment (optional but recommended):

   ```powershell
   python -m venv .env
   .\.env\Scripts\activate
   ```

3. Install dependencies:

   ```powershell
   pip install -r requirements.txt
   python -m nltk.downloader punkt stopwords wordnet
   python -m textblob.download_corpora
   python -m spacy download en_core_web_sm
   ```

4. Run scripts step-by-step:

   ```powershell
   python user_data.py            # Step 1: Input and save text
   python text_processing.py      # Step 2: Preprocess text
   python "NER & POS.py"          # Step 3: NLP + Sentiment → final.xlsx
   ```

---

### ✅ On **Kali Linux**:

1. Open Terminal and navigate to your project folder:

   ```bash
   cd /path/to/your/project
   ```

2. (Optional) Create virtual environment:

   ```bash
   python3 -m venv .env
   source .env/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   python3 -m nltk.downloader punkt stopwords wordnet
   python3 -m textblob.download_corpora
   python3 -m spacy download en_core_web_sm
   ```

4. Run the workflow:

   ```bash
   python3 user_data.py
   python3 text_processing.py
   python3 "NER & POS.py"
   ```

---

## 📊 Output

Final output will be saved as:

📄 **`final.xlsx`** with these sheets:

* Original Data
* POS Tags
* Named Entities
* Lemmas
* Dependencies
* Sentiment (polarity & subjectivity)

---

## 🔍 Features

* Input limit: max **1000 words**
* Spell correction using `pyspellchecker`
* Lemmatization using both NLTK & spaCy
* Export to clean Excel format using `pandas`
* Sentiment Analysis using `TextBlob`

---

## 🛠 Troubleshooting

* If you get **ModuleNotFoundError**, make sure virtual environment is activated.
* If spaCy model not found, run:

  ```bash
  python -m spacy download en_core_web_sm
  ```

---

## 📜 License

This project is for educational and research use. You can modify it freely.

---

## 🤝 Contributions

PRs and suggestions are welcome!

---

## ✍️ Author

Developed by \[Your Name or GitHub Username]

```

---

Would you like this content saved as a ready-to-use `README.md` file so you can push it directly to GitHub?
```
