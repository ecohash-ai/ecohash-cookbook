# Reranker

Reorder candidate documents by relevance to a query (great for RAG).
Model: `bge-reranker-v2-m3`. Endpoint: `POST /v1/rerank`.

```bash
pip install requests
export ECOHASH_API_KEY=eco_...   # create one at console.ecohash.com
python rerank.py
```
