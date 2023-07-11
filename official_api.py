import openai

openai.api_key = "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"

prompt = "帮助我写一段python程序，实现冒泡排序"

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[{
    "role": "user",
    "content": prompt,
  }]
)

print(completion)
# print(completion.choices[0].message['content'])
# print(completion['usage'])