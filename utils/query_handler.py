
from utils.embedder import model, embed_query
from sklearn.cluster import KMeans
from collections import defaultdict

def handle_query(index, query):
    vec = embed_query(query)
    return index.search(vec)

def cluster_themes(results, n_clusters=2):
    texts = [r[0]['chunk'] for r in results]
    embeddings = model.encode(texts)
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    labels = kmeans.fit_predict(embeddings)

    themes = defaultdict(list)
    for label, (res, score) in zip(labels, results):
        themes[label].append({
            "text": res['chunk'],
            "meta": res['meta'],
            "score": score
        })
    return themes

def synthesize_themes(themes):
    summaries = {}
    for label, items in themes.items():
        summary = " ".join([item["text"] for item in items[:2]])
        docs = set([item["meta"].split(',')[0].split(':')[1].strip() for item in items])
        summaries[label] = {"summary": summary[:300], "docs": list(docs)}
    return summaries
