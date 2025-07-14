from docx import Document

def get_user_input():
    print("Enter your text (maximum 1000 words). Type 'END' on a new line to finish:")
    text_lines = []
    
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        text_lines.append(line)
    
    full_text = " ".join(text_lines)
    words = full_text.split()
    
    if len(words) > 1000:
        full_text = " ".join(words[:1000])
        print("Warning: Your input exceeded 1000 words and has been truncated.")
    
    return full_text

def save_to_word(text, filename="user_text.docx"):
    doc = Document()
    doc.add_paragraph(text)
    doc.save(filename)
    print(f"Text saved successfully in {filename}")

def main():
    user_text = get_user_input()
    save_to_word(user_text)

if __name__ == "__main__":
    main()
