
import os
import fitz  # PyMuPDF
from PIL import Image
import pytesseract

def extract_text_from_pdf(path):
    doc = fitz.open(path)
    text = []
    for page_num, page in enumerate(doc):
        content = page.get_text()
        text.append(f"[Page {page_num+1}]\n{content}")
    return "\n".join(text)

def extract_text_from_image(path):
    img = Image.open(path).convert('RGB')
    return pytesseract.image_to_string(img)

def save_uploaded_file(file, save_dir="uploads"):
    os.makedirs(save_dir, exist_ok=True)
    path = os.path.join(save_dir, file.name)
    with open(path, "wb") as f:
        f.write(file.getbuffer())
    return path
