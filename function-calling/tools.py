"""Tool / function calling with EcoHash (OpenAI-compatible)."""

import json
import os

from openai import OpenAI

client = OpenAI(
    base_url="https://api.ecohash.com/v1",
    api_key=os.environ["ECOHASH_API_KEY"],
)

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get the current weather for a city.",
            "parameters": {
                "type": "object",
                "properties": {"city": {"type": "string"}},
                "required": ["city"],
            },
        },
    }
]

response = client.chat.completions.create(
    model="llama-3.1-8b-instruct",
    messages=[{"role": "user", "content": "What's the weather in Dallas?"}],
    tools=tools,
)

message = response.choices[0].message
if message.tool_calls:
    call = message.tool_calls[0]
    print("tool:", call.function.name)
    print("arguments:", json.loads(call.function.arguments))
else:
    print(message.content)
