from groq import Groq

client = Groq(api_key="")

models = client.models.list()

for m in models.data:
    print(m.id)
