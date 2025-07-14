# NLP-Assistant
For Windows:
Install Python (3.8 or higher)

Install requirements:
pip install -r requirements.txt
python -m spacy download en_core_web_sm

Run the project:
# First run user_data.py to input your text
python user_data.py

# Then process the text
python text_processing.py

# Finally run the NLP analysis
python "NER & POS.py"
For Kali Linux:
Install Python (if not already installed):

bash
sudo apt update
sudo apt install python3 python3-pip
Install requirements:

bash
pip3 install -r requirements.txt
python3 -m spacy download en_core_web_sm
Run the project:

bash
# First run user_data.py to input your text
python3 user_data.py

# Then process the text
python3 text_processing.py

# Finally run the NLP analysis
python3 "NER & POS.py"
Project Workflow
Start with user_data.py to input your text (saves to user_text.docx)

Run text_processing.py to clean the text (saves to processed_text.xlsx)

Run NER & POS.py for advanced NLP analysis (saves to final.xlsx)

Notes
For Kali Linux, you might need to install additional dependencies:

bash
sudo apt install libenchant-2-2
The Word document path in text_processing.py needs to match your system's path

All generated files will be created in the same directory as the scripts

For large texts, processing might take some time

Troubleshooting
If you get spaCy model errors:

bash
python -m spacy validate
If spellchecker fails on Linux:

bash
sudo apt install libenchant-2-dev
pip3 install pyenchant
For any missing NLTK data:

bash
python3 -m nltk.downloader all
