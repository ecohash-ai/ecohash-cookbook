"""Generate text embeddings with EcoHash (OpenAI-compatible)."""

import os

from openai import OpenAI

client = OpenAI(
    base_url="https://api.ecohash.com/v1",
    api_key=os.environ["ECOHASH_API_KEY"],
)

response = client.embeddings.create(
    model="jina-embeddings-v3",
    input=[
        "EcoHash is an OpenAI-compatible inference API.",
        "How do I create an API key?",
    ],
)

for i, item in enumerate(response.data):
    print(f"embedding {i}: dim={len(item.embedding)}")
