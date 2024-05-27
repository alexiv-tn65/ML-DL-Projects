import os

import numpy as np
from dotenv import load_dotenv
from gensim import corpora, models
from langchain.chains import RetrievalQA
from langchain.vectorstores.chroma import Chroma
from langchain_community.chat_models import GigaChat
from langchain_community.embeddings.gigachat import GigaChatEmbeddings

load_dotenv()

dialog_context = {}

def is_retrievable_from_database(prompt):
    # Проводим проверку, доступен ли ответ на данный запрос в базе данных
    # Возвращаем True, если ответ доступен в базе данных, и False в противном случае
    if "запрос" in prompt: 
        return True
    else:
        return False

# Функция для поиска ближайшего соответствия в источнике

def retrieve_from_database(prompt, vectordb):
    dictionary = corpora.Dictionary([list(vectordb.keys())])
    similarity_matrix = models.WordEmbeddingSimilarityIndex(model)
    query = dictionary.doc2bow(prompt.split())
    index = similarity_matrix[query]

    best_match = ''
    highest_similarity = 0
    for question in vectordb:
        question_bow = dictionary.doc2bow(question.split())
        sim = index.inner_product(question_bow, normalized=True)  # Используем inner_product для вычисления сходства
        if sim > highest_similarity:
            highest_similarity = sim
            best_match = question
    return vectordb[best_match]


async def context_aware_agent(prompt, credentials, scope):
    previous_dialog = dialog_context.get('previous_dialog')
    previous_prompt = previous_dialog['prompt'] if previous_dialog else None
    previous_response = previous_dialog['response'] if previous_dialog else None
    full_prompt = f"{previous_prompt} {previous_response}" if previous_prompt else prompt

    if is_retrievable_from_database(prompt):  
        result = retrieve_from_database(full_prompt, vectordb)  # используем vectordb для поиска ближайшего ответа  
    else:
        embeddings = GigaChatEmbeddings(
            credentials=os.environ['GIGACHAT_CRED'], 
            verify_ssl_certs=False, scope='GIGACHAT_API_CORP'
        )

        vectordb = Chroma(persist_directory="./data", embedding_function=embeddings)

        llm = GigaChat(credentials=os.environ['GIGACHAT_CRED'], 
        verify_ssl_certs=False, scope='GIGACHAT_API_CORP')

        query = {"query": full_prompt} #NEW

        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=vectordb.as_retriever(search_kwargs={'k': 18}),
            return_source_documents=True,
        )

        result = qa_chain.invoke({'query': full_prompt})

    dialog_context['previous_dialog'] = {'prompt': prompt, 'response': result['result']}

    return result['result']
