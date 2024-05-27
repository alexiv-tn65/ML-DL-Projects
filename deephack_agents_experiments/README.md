# Разработка ИИ-ассистента для помощи в научной деятельности

Проект подготовлен командой '56' в рамках хакатона DeepHack.Agents
- Дарья Кашина
- Алексей Фирсов
- Александр Иваненков

## Задача

На основании возможностей, которые предоставляют GigaChat и его [SDK GigaChain](https://github.com/ai-forever/gigachain/tree/master), разработать собственного ИИ-ассистента, помогающего в научной деятельности. 

## Наша идея

При работе над новым исследованием аспирантам/научным сотрудникам необходимо делать обзор уже существующих исследований. Как правило это делается при помощи баз типа Google Scholar по ключевым словам. 

[Здесь](https://girlsinstem.org/ewgis-course/week2) можно подробнее прочитать о том, как и где делается обзор исследований. Помимо [Google Scholar](https://scholar.google.com) есть такие источники как: 
- [PubMed](https://pubmed.ncbi.nlm.nih.gov),
- [IEEE Xplore](https://ieeexplore.ieee.org/Xplore/home.jsp),
- [Web of Science](https://clarivate.com/cis/solutions/web-of-science/),
- [Scopus](https://www.scopus.com/home.uri),
- [Semantic Scholar](https://www.semanticscholar.org/product/api?),
- [arXiv.org](arXiv.org)  

Из большинства источников можно получить информацию по API (за исключением Google Scholar и Scopus). 

**Поэтому мы решили создать ИИ-ассистента, который при помощи агента и RAG-технологии мог бы искать информацию сначала в векторной БД/по API и давать ссылки на источники, а если ответ не найден, обращался бы к LLM GigaChat. Задача реализована частично, но имея работающий MVP у нас есть возможность в дальнейшем развить его в полноценный и многофункциональный продукт.** 
  
Второстепенной задачей было оповещение о грантах и конкурсах по заданной тематике (например, с сайта [fasie.ru](fasie.ru)), чтобы молодые ученые могли своевременно узнавать о событиях, связанными с их темой. Данная задача не была реализована.


## Реализация

Мы создали ИИ-ассистента в виде телеграм-бота, который может отвечать на запрос пользователя через агента. Агент для ответа использует векторную БД Chroma (для MVP мы наполнили базу статьями по квантовой физике, а также выдуманной информацией из области химии, чтобы у нас была возможность проверить, что ИИ-ассистент действительно обращается в базу данных, а не к LLM), а если ответа в БД нет, обращается к LLM GigaChat. Тем самым может отвечать не только на научные, но и на общие вопросы.  
  
Демонстрация готового продукта:  

- [Telegram bot &#34;ScientificAIConsultantBot&#34;](https://t.me/ScientificAIConsultantBot)
- Презентация [key](https://disk.yandex.ru/d/0ypxH6_8hkusaw)/[pdf](https://disk.yandex.ru/i/0wYMAUrQsLsgdQ)
- [Видео-демонстрация](https://disk.yandex.ru/i/XSB-jRQTC5M1pQ)

ИИ-ассистент реализован в виде бота, открывается по [ссылке](https://t.me/ScientificAIConsultantBot) и запускается командой */start*. 
Также дополнительно можно узнать, как работать с ИИ-ассистентом, используя команду */help*

<details><summary><b>Установка и запуск чат-бота через терминал</b></summary>

- Склонируйте репозиторий  `https://github.com/daria-kashina/AI-assistant.git`
- Создайте новое виртуальное окружение `python3 -m venv название_окружения`
- Активируйте его `source название_окружения/bin/activate` (mac)
- Установите зависимости `pip install -r requirements.txt`
- Запустите чат-бота `python3 -m main`

</details>

<details><summary><b>Структура</b></summary>  
  
Prod:  
[agent.py](https://github.com/daria-kashina/AI-assistant/blob/main/gigachat_tools/agent.py) - скрипт запуска агента  
[database_preparation.py](https://github.com/daria-kashina/AI-assistant/blob/main/gigachat_tools/database_preparation.py) - скрипт для подготовки векторной БД  
[example.txt](https://github.com/daria-kashina/AI-assistant/blob/main/gigachat_tools/example.txt) - текстовый файл для наполнения БД  
[main.py](https://github.com/daria-kashina/AI-assistant/blob/main/main.py) - скрипт запуска ИИ-ассистента в Telegram  
[requirements.txt](https://github.com/daria-kashina/AI-assistant/blob/main/requirements.txt) - файл с зависимостями проекта  
  
Файлы наработок (не используются в текущей prod-версии):  
[agent_diff.py](https://github.com/daria-kashina/AI-assistant/blob/main/agent_diff.py) - агент с попыткой добавления учета контекста диалога и поиска ближайшего подходящего ответа в векторной БД  
[agent_check.py](https://github.com/daria-kashina/AI-assistant/blob/main/agent_check.py) - проверка agent_diff.py в терминале  
  
</details>
