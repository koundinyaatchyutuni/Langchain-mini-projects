from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda
from langchain_openai import ChatOpenAI
from document_loader import PDFLoader
from dotenv import load_dotenv
import os

load_dotenv()

chat_model = ChatOpenAI(
    model="poolside/laguna-s-2.1:free",
    openai_api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
    temperature=0
)
prompt_skill_extract = PromptTemplate(
    input_variables=["resume_data"],
    template="""I am attaching my resume data.
Analyze it and provide a summary of my skills and experience.

Here is my resume data:
{resume_data}
"""
)


prompt_suggest_job = PromptTemplate(
    input_variables=["extracted_skills"],
    template="""I am attaching my extracted skills data.
Analyze it and provide skill recommendations for me to improve in my current role.

Here is my extracted skills data:
{extracted_skills}
"""
)


parser = StrOutputParser()


resume_loader = PDFLoader(
    "data/Koundinya_Atchyutuni_Resume_Updated.pdf"
)

resume_data = resume_loader.load()

resume_text = "\n".join(
    doc.page_content for doc in resume_data
)
# print(resume_text[:2000])

chain = (
    prompt_skill_extract
    | chat_model
    | parser
    | RunnableLambda(lambda x: {"extracted_skills": x})
    | prompt_suggest_job
    | chat_model
)


skills_to_update = chain.invoke({
    "resume_data": resume_text
})


print("TYPE:", type(skills_to_update))
print("OUTPUT:", skills_to_update)