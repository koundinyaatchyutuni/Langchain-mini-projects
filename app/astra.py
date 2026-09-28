from langchain_openai import ChatOpenAI

model = ChatOpenAI(
    model="gpt-6-astra",
    temperature=0
)

response = model.invoke("Explain LangChain in simple terms.")

print(response.content)