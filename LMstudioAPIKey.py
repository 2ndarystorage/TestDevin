import openai

openai.api_base = "http://localhost:1234/v1"
openai.api_key = "lmstudio"

response = openai.ChatCompletion.create(
    model="llama3",
    messages=[
        {"role": "system", "content": "あなたは親切な日本語アシスタントです。"},
        {"role": "user", "content": "今日の天気は？"}
    ],
    temperature=0.7,
)

print(response["choices"][0]["message"]["content"])
