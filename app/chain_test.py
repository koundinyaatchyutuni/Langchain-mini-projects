from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel,Field
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

class Resume_data(BaseModel):
    name: str = Field(description="Name of the candidate")
    email: str = Field(description="Email address of the candidate")
    experience: str = Field(description="Work experience of the candidate")
    skills: str = Field(description="Skills of the candidate")
    job_title: str = Field(description="Job title of the candidate")
    
load_dotenv()

chat_model = llm = ChatOpenAI(
    model="openrouter/free",
    openai_api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
    temperature=0
)

prompt_skill_extract= PromptTemplate(
    input_variables=["resume_data"],
    template="""I am attaching my resumes data, please analyze it and provide a summary of my skills and experience.
    here is my resume data: {resume_data}""")

prompt_suggest_job= PromptTemplate(
    input_variables=["extracted_skills"],
    template="""I am attaching my extracted skills data, please analyze it and provide a skill recommendation for me to improve in my current role.
    here is my extracted skills data: {extracted_skills}""")
parser = StrOutputParser()

chain = prompt_skill_extract | chat_model | parser | prompt_suggest_job | chat_model | parser

skills_to_update=chain.invoke("""
MANIKYA PRASAD KOUNDINYA ATCHYUTUNI
github.com/koundinyaatchyutuni  |  leetcode.com/u/Koundinyaatchyutuni
SKILLS
Email : koundinyaatchyutuni@gmail.com
Mobile : 9393930903
○ Programming Languages: C++, Java, Python, JavaScript, C
○ Frontend: React.js, HTML5, CSS3, Vite
○ Backend: Node.js, Express.js, REST APIs, JWT Authentication, Axios
○ AI & Agentic AI: LangChain, LangGraph, LLMs, RAG, Prompt Engineering, Tool Calling, AI Agents
○ Databases: MongoDB, MySQL
○ Developer Tools & DevOps: Git, GitHub, GitHub Actions, CI/CD, Linux, Shell Scripting (Bash), Visual Studio Code (VS Code)
○ Cloud: Google Cloud Platform (GCP), Bigquery, GCP Composer, GCP Dataproc, Google Cloud Storage (GCS)
○ Core Computer Science: Data Structures & Algorithms, Object-Oriented Programming (OOP), Database Management Systems (DBMS), 
Operating Systems, Computer Networks, Basics of System Design
ACADEMIC AND EXTRACURRICULAR ACHIEVEMENTS
○ Gate 2024 DA Rank (General):  353 , APEAMCET Rank (General):  1802 , JEE Mains  94.5  percentile
○ Achieved a 1700+ contest rating and solved 750+ Data Structures & Algorithms problems on LeetCode.
○ Google cloud certified Cloud digital leader
○ Short clip making: Winner in short clip-making competition, focused on promoting cleanliness, GVPCE.
WORK EXPERIENCE
Accenture
Advanced Associate Software Engineer | Data Engineer
Nov'24 - Present
○ Contributed to the migration of legacy data pipelines for the American Express cloud modernization project by redesigning data 
workflows on Google Cloud Platform (GCP) using BigQuery, Cloud Dataproc, and Cloud Composer.
○ Developed and maintained Apache Airflow DAGs with complex workflow orchestration, dependency management, scheduling, retry 
mechanisms, and monitoring to automate large-scale data processing.
○ Optimized BigQuery SQL workloads for efficient data transformation and implemented secure handling of sensitive data using PII 
masking, access control, and data governance best practices.
○ Developed a HiveQL-to-BigQuery agent as part of an Agentic AI-based automatic code converter, automating conversion of legacy 
HiveQL queries to BigQuery SQL.
""")
print("TYPE:", type(skills_to_update))
print("OUTPUT:", repr(skills_to_update))