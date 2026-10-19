from openai import OpenAI
import os

# for backward compatibility, you can still use `https://api.deepseek.com/v1` as `base_url`.
client = OpenAI(
    api_key=os.environ.get("DEEPSEEK_API_KEY"), base_url="https://api.deepseek.com"
)

response = client.chat.completions.create(
    model="deepseek-flash",
    messages=[
        {
            "role": "system",
            "content": "你是一个清纯可爱的Ai助手，你的名字叫小团团，请使用中文回答问题。",
        },
        {"role": "user", "content": "Hello，你是谁？"},
    ],
    max_tokens=1024,
    temperature=0.7,
    stream=False,
)

print(response.choices[0].message.content)
print(response)
