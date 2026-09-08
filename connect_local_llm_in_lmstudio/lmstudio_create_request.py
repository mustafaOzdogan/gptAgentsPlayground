from openai import OpenAI

# Point to the local server
client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")

completion = client.chat.completions.create(
  model="local-model",  # this field is currently unused
  messages=[
    {"role": "system", "content": "Always answer just in one sentence."},
    {"role": "user", "content": "What is biggest football team in Turkey?"}
  ],
  temperature=0.7,
)

print(completion.choices[0].message.content)
