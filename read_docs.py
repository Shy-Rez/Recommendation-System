import docx
import PyPDF2

print("=== DOCX CONTENT ===")
try:
    doc = docx.Document("Netflix Recommendation System for Personalized Content Discovery.docx")
    for para in doc.paragraphs:
        if para.text.strip():
            print(para.text)
except Exception as e:
    print("Error reading docx:", e)

print("\n=== PDF CONTENT ===")
try:
    with open("Netflix_Recommendation_Presentation.pdf", "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for i, page in enumerate(reader.pages):
            text = page.extract_text()
            if text.strip():
                print(f"--- Page {i+1} ---")
                print(text)
except Exception as e:
    print("Error reading pdf:", e)
