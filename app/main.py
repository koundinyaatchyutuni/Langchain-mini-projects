from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate


load_dotenv()
standard_prompt = PromptTemplate(
    input_variables=["resume_data"],
    template="""I am attaching my resumes data, please analyze it and provide a summary of my skills and experience.
    here is my resume data: {resume_data}"""
    )

model = ChatGoogleGenerativeAI(
    model="gemini-3.7-flash",
    temperature=0
)

user_prompt= input("Enter your prompt: ")
response = model.invoke(user_prompt)

print(response.content[0]['text'])