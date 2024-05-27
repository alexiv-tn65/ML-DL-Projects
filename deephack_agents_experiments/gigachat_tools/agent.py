import os

from dotenv import load_dotenv
from langchain.chains import RetrievalQA
from langchain.prompts import load_prompt
from langchain.schema import HumanMessage, SystemMessage
from langchain.vectorstores.chroma import Chroma
from langchain_community.chat_models import GigaChat
from langchain_community.embeddings.gigachat import GigaChatEmbeddings

load_dotenv()


class ScientificAIAgent:
    def __init__(self):
        self.credentials = os.environ['GIGACHAT_CRED']
        self.embeddings = GigaChatEmbeddings(
            credentials=self.credentials,
            verify_ssl_certs=False,
            scope='GIGACHAT_API_CORP')
        self.llm = GigaChat(credentials=self.credentials,
                            verify_ssl_certs=False,
                            scope='GIGACHAT_API_CORP')

    def response_to_user_request(
            self, user_id: int, user_text_request: str) -> str:
        vectordb = Chroma(
            persist_directory="./data",
            embedding_function=self.embeddings)

        qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=vectordb.as_retriever(search_kwargs={'k': 12}),
            return_source_documents=True)

        result = qa_chain.invoke({'query': user_text_request})

        return result['result']
