from groq_client import client


response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[
        {
            "role": "user",
            "content": "Explain what an API is in one sentence."
        }
    ]
)

print(response.choices[0].message.content)