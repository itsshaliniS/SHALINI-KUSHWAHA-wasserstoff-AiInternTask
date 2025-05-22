
# 📄 GenAI Document Research Chatbot

Welcome to the **GenAI Document Chatbot** — a smart assistant designed to extract insights and identify themes across large sets of documents. This project was developed as part of the Wasserstoff AI Internship Task and aims to demonstrate real-world implementation of document understanding and semantic search using modern AI tools.

---

## What This App Does

This chatbot helps you:
- Upload **PDFs or scanned images** (like reports, legal orders, etc.)
- Extract high-quality text using **OCR**
- Break documents into **paragraph-level chunks**
- **Embed, index, and search** content using semantic vectors
- Answer **natural language questions**
- Identify **cross-document themes**
- Provide **precise citations** including document name, page, and paragraph

---

## Technologies Used

| Tool | Purpose |
|------|---------|
| **Python** | Core programming |
| **Streamlit** | Frontend UI |
| **FAISS** | Vector similarity search |
| **Sentence Transformers** | Embeddings (MiniLM-L6-v2) |
| **Tesseract OCR** | Extract text from scanned documents |
| **PyMuPDF** | PDF text extraction |
| **LangChain** | Text splitting |
| **Scikit-Learn** | KMeans clustering for themes |

---

## Features

✅ Upload multiple documents (PDFs and images)  
✅ OCR support for scanned documents  
✅ Document chunking with page & paragraph tagging  
✅ Query interface with semantic search  
✅ Document-level and paragraph-level **citations**  
✅ Theme clustering across documents  
✅ Simple, clean web interface

---

## How to Use

1. **Upload Documents**: Drag and drop your PDFs or images
2. **Processing**: The app automatically extracts and processes text
3. **Ask Questions**: Use natural language to query your documents
4. **Get Insights**: Receive answers with precise citations
5. **Explore Themes**: Discover common themes across documents


## Project Structure

```
├── app.py                 # Main Streamlit application
├── utils/
│   ├── document_loader.py # PDF and image processing
│   ├── embedder.py       # Text embedding functionality
│   ├── query_handler.py  # Search and retrieval logic
│   ├── text_splitter.py  # Document chunking
│   └── vector_store.py   # FAISS vector operations
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

---
