import os

from dotenv import load_dotenv
from langchain.chains import RetrievalQA
from langchain.vectorstores.chroma import Chroma
from langchain_community.chat_message_histories import FileChatMessageHistory
from langchain_community.chat_models import GigaChat
from langchain_community.embeddings.gigachat import GigaChatEmbeddings

load_dotenv()

embeddings = GigaChatEmbeddings(
    credentials=os.environ['GIGACHAT_CRED'],
    verify_ssl_certs=False, scope='GIGACHAT_API_CORP'
)

vectordb = Chroma(persist_directory="./data", embedding_function=embeddings)

llm = GigaChat(credentials=os.environ['GIGACHAT_CRED'],
               verify_ssl_certs=False, scope='GIGACHAT_API_CORP')

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    # retriever=ensemble_retriever,
    retriever=vectordb.as_retriever(search_kwargs={'k': 18}),
    return_source_documents=True,
)

# Теперь можно выполнять запросы к нашей цепочке вопросов и ответов
result = qa_chain.invoke({'query': "В каком году изобрели технологию производства \
    гидрофуранатетрааммония678триуксуснокислого? И где?"})


print("result:  ", result['result'])
