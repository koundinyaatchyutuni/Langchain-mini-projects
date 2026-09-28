from langchain_community.document_loaders import PyPDFLoader
# from dotenv import load_dotenv
import os

class PDFLoader:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def load(self):
        loader = PyPDFLoader(self.file_path)
        documents = loader.lazy_load()
        return documents

class TextLoader:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def load(self):
        with open(self.file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        return text
    
