from groq import Groq

client = Groq(api_key="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")

models = client.models.list()

for m in models.data:
    print(m.id)
