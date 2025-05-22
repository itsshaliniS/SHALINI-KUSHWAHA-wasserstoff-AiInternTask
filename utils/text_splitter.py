
from langchain.text_splitter import RecursiveCharacterTextSplitter

def split_text(text, filename="Unknown", chunk_size=500, overlap=50):
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=overlap)
    chunks = splitter.split_text(text)

    enhanced_chunks = []
    for i, chunk in enumerate(chunks):
        page = "Unknown"
        if "[Page" in chunk:
            try:
                page = chunk.split("[Page")[1].split("]")[0].strip()
            except:
                pass
        enhanced_chunks.append({
            "chunk": chunk,
            "meta": f"Doc: {filename}, Page: {page}, Para: {i+1}"
        })
    return enhanced_chunks
