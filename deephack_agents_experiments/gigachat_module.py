# Работа с чатом через GigaChain
from langchain.chat_models.gigachat import GigaChat
from langchain.schema import HumanMessage, SystemMessage

# Авторизация в сервисе GigaChat
cred = 'Yjg4MTQzMmUtNDAwMS00NDk0LThjOGUtNmU5ZWQ2YzQ4NDQ2OmQ4MWMxZGZiLTFmNGYtNDk5NS05OGQzLTBiMzYyYWJmNjk3OA=='

chat = GigaChat(
    credentials=cred,
    verify_ssl_certs=False,
    scope='GIGACHAT_API_CORP')

messages = [
    SystemMessage(
        content="Ты ИИ-ассистент, который помогает находить исследования по заданной области"
    )
]

while (True):
    user_input = input("User: ")
    messages.append(HumanMessage(content=user_input))
    res = chat(messages)
    messages.append(res)
    print("Bot: ", res.content)
