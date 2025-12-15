#model setup
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model="models/gemini-1.5-flash",   # or models/gemini-1.5-pro
    google_api_key="YOUR_API_KEY",
    temperature=0.7
)
#story generation chain
from langchain.prompts import ChatPromptTemplate
from langchain.output_parsers import StrOutputParser

story_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a creative storyteller."),
    ("human", "Write a short story about {character} in a {setting} with a {tone} tone.")
])

story_chain = story_prompt | llm | StrOutputParser()
#analysis chain
analysis_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a literary analyst."),
    ("human", 
     "Analyze the following story.\n\n"
     "Story:\n{story}\n\n"
     "Provide:\n"
     "1. Main theme\n"
     "2. Character traits\n"
     "3. Emotional tone\n"
     "4. One improvement suggestion"
    )
])

analysis_chain = analysis_prompt | llm | StrOutputParser()
#running both together
# Step 1: Generate story
story = story_chain.invoke({
    "character": "a young robot",
    "setting": "a futuristic city",
    "tone": "inspiring"
})

# Step 2: Analyze the story
analysis = analysis_chain.invoke({
    "story": story
})

print("📖 STORY:\n", story)
print("\n🔍 ANALYSIS:\n", analysis)

analysis_chain = (
    ChatPromptTemplate.from_messages([
        ("system", "You are an analyst."),
        ("human", "Analyze this text:\n{text}")
    ])
    | llm
    | StrOutputParser()
)
#pipeline
from langchain.schema.runnable import RunnablePassthrough

# Story chain
story_chain = story_prompt | llm | StrOutputParser()

# Analysis chain
analysis_chain = analysis_prompt | llm | StrOutputParser()
##############we can also use runnable lambda for passing story text to a function that puts it in the analysis prompt
# Combined chain: generate → analyze
story_analysis_chain = (
    {"story": story_chain}    # output of story_chain becomes {story}
    | 
    
analysis_chain
)
# Run the combined chain
result = story_analysis_chain.invoke({
    "character": "a young robot",
    "setting": "a futuristic city",
    "tone": "inspiring"
})

print("🔍 ANALYSIS:\n", result)


