from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:1234/v1",
    api_key="lmstudio"
)

response = client.chat.completions.create(
    model="llama3",
    messages=[
        {"role": "system", "content": "あなたは親切なアシスタントです。"},
        {"role": "user", "content": "日本のことわざをひとつ教えて。"}
    ],
    temperature=0.7
)

print(response.choices[0].message.content)