import asyncio
import os

from dotenv import load_dotenv

from agent_diff import context_aware_agent

load_dotenv()

credentials = os.environ['GIGACHAT_CRED']
scope = 'GIGACHAT_API_CORP'


async def interact_with_agent():
    while True:
        prompt = input("Введите ваш вопрос: ")
        if prompt.lower() in ['exit', 'quit', 'q']:
            print("До свидания!")
            break

        # Вызываем агента и получаем результат
        response = await context_aware_agent(prompt, credentials, scope)
        print(f"Ответ: {response}\n")

# запускаем взаимодействие с агентом
asyncio.run(interact_with_agent())
