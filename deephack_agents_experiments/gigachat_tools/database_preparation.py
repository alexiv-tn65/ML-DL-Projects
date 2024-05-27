import os

from chromadb.config import Settings
from dotenv import load_dotenv
from langchain.chat_models.gigachat import GigaChat
from langchain.document_loaders.text import TextLoader
from langchain.schema import HumanMessage
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores.chroma import Chroma
from langchain_community.embeddings.gigachat import GigaChatEmbeddings

# Read .env file
load_dotenv()


# Изменить encoding при необходимости
loader = TextLoader(
    "./example.txt",
    encoding='utf-8'
)
documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=0,
)
documents = text_splitter.split_documents(documents)

embeddings = GigaChatEmbeddings(
    credentials=os.environ['GIGACHAT_CRED'],
    verify_ssl_certs=False, scope='GIGACHAT_API_CORP'
)

db = Chroma.from_documents(
    documents,
    embeddings,
    # client_settings=Settings(anonymized_telemetry=False),
    persist_directory='./data'
)

db.persist()

print("База данных успешно создана и сохранена.")
print(f"Место нахождения базы данных: {db._persist_directory}")
