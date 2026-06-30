<p align="center">
  <img src="assets/ecohash-logo.png" alt="EcoHash" width="280">
</p>

<p align="center">
  <a href="https://console.ecohash.com?utm_source=github">Platform</a> •
  <a href="https://docs.ecohash.com">Docs</a> •
  <a href="https://ecohash.com">Website</a>
</p>

# EcoHash Cookbook

Runnable examples for EcoHash — OpenAI-compatible inference API.

## Installation

```bash
pip install openai requests
```

## Usage

Create an API key at [console.ecohash.com](https://console.ecohash.com?utm_source=github), then point the OpenAI SDK at EcoHash:

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.ecohash.com/v1", api_key="eco_...")
```

### Use [text generation models](https://docs.ecohash.com/platform-models/chat-completions)

```python
resp = client.chat.completions.create(
    model="llama-3.1-8b-instruct",
    messages=[{"role": "user", "content": "What is the capital of France?"}],
)
print(resp.choices[0].message.content)
```

### Use [vision models](https://docs.ecohash.com/platform-models/chat-completions)

```python
resp = client.chat.completions.create(
    model="qwen3-vl-8b-instruct",
    messages=[{"role": "user", "content": [
        {"type": "text", "text": "What is in this image?"},
        {"type": "image_url", "image_url": {"url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Cat03.jpg/640px-Cat03.jpg"}},
    ]}],
)
print(resp.choices[0].message.content)
```

### Use [text embedding models](https://docs.ecohash.com/platform-models/embeddings)

```python
resp = client.embeddings.create(
    model="jina-embeddings-v3",
    input=["EcoHash is an OpenAI-compatible inference API."],
)
print(len(resp.data[0].embedding))
```

### Use [reranker models](https://docs.ecohash.com/platform-models/reranker)

```python
import os
import requests

resp = requests.post(
    "https://api.ecohash.com/v1/rerank",
    headers={"Authorization": f"Bearer {os.environ['ECOHASH_API_KEY']}"},
    json={
        "model": "bge-reranker-v2-m3",
        "query": "how does solar power work?",
        "documents": [
            "Solar panels convert sunlight into electricity.",
            "My cat enjoys the sun but cannot generate power.",
            "Photovoltaic cells transform photons into electric current.",
        ],
        "top_n": 2,
    },
)
for item in resp.json()["results"]:
    print(item["index"], item["relevance_score"])
```

### Use [speech-to-text models](https://docs.ecohash.com/platform-models/audio-transcription)

```python
with open("audio.wav", "rb") as audio_file:
    result = client.audio.transcriptions.create(model="whisper-large-v3", file=audio_file)
print(result.text)
```

### Use [text-to-speech models](https://docs.ecohash.com/platform-models/audio-speech)

```python
with client.audio.speech.with_streaming_response.create(
    model="kokoro-82m",
    voice="af_heart",
    input="Hello from EcoHash.",
    response_format="wav",
) as response:
    response.stream_to_file("speech.wav")
```

### Use [image generation models](https://docs.ecohash.com/platform-models/image-generation)

```python
import base64

resp = client.images.generate(
    model="z-image-turbo",
    prompt="a watercolor painting of a fox in a misty forest",
    size="1024x1024",
    response_format="b64_json",
)
with open("image.png", "wb") as f:
    f.write(base64.b64decode(resp.data[0].b64_json))
```

## License

MIT — see [LICENSE](LICENSE).
