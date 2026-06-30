"""Single-turn voice agent on EcoHash: speech-to-text -> LLM -> text-to-speech, one key."""

import os
import sys

from openai import OpenAI

client = OpenAI(
    base_url="https://api.ecohash.com/v1",
    api_key=os.environ["ECOHASH_API_KEY"],
)

audio_in = sys.argv[1] if len(sys.argv) > 1 else "input.wav"

# 1. Speech to text
with open(audio_in, "rb") as audio_file:
    user_text = client.audio.transcriptions.create(model="whisper-large-v3", file=audio_file).text
print("User:", user_text)

# 2. LLM reply
reply = client.chat.completions.create(
    model="llama-3.1-8b-instruct",
    messages=[{"role": "user", "content": user_text}],
).choices[0].message.content
print("Assistant:", reply)

# 3. Text to speech
with client.audio.speech.with_streaming_response.create(
    model="kokoro-82m",
    voice="af_heart",
    input=reply,
    response_format="wav",
) as response:
    response.stream_to_file("reply.wav")
print("Wrote reply.wav")
