# Voice agent

A single-turn voice agent built on three EcoHash endpoints with one API key:
speech-to-text (`whisper-large-v3`) → LLM (`llama-3.1-8b-instruct`) → text-to-speech (`kokoro-82m`).
It reads a `.wav`, prints the transcript and the reply, and writes `reply.wav`.

```bash
pip install openai
export ECOHASH_API_KEY=eco_...   # create one at console.ecohash.com
python agent.py input.wav
```

This is the single-turn pipeline; a real-time streaming version is a natural next step.
