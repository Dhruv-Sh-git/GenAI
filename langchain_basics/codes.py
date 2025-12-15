from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import SystemMessage, HumanMessage

# Initialize Gemini chat model
llm = ChatGoogleGenerativeAI(
    model="models/gemini-1.5-flash",   # or models/gemini-1.5-pro
    google_api_key="YOUR_API_KEY",
    temperature=0.3
)

# Define messages
messages = [
    SystemMessage(content="You are a helpful AI assistant that explains concepts clearly."),
    HumanMessage(content="Explain LangChain in simple terms with an example.")
]

# Invoke the model
response = llm.invoke(messages)

# Print output
##############################################################################
print(response.content)
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate

# Initialize Gemini model
llm = ChatGoogleGenerativeAI(
    model="models/gemini-1.5-flash",   # or models/gemini-1.5-pro
    google_api_key="YOUR_API_KEY",
    temperature=0.3
)

# Create chat prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI assistant. Answer concisely."),
    ("human", "Explain {topic} in simple terms with an example.")
])

# Combine prompt + model (LCEL style)
chain = prompt | llm

# Invoke the chain
response = chain.invoke({
    "topic": "LangChain"
})

# Output
print(response.content)

