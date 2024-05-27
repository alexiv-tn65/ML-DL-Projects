from langchain_community.chat_models import GigaChat

from config import cred

chat = GigaChat(
    credentials=cred,
    verify_ssl_certs=False,
    scope='GIGACHAT_API_CORP')
print(chat.get_models())
