
def standard_answers(input):
    message = str(input).lower()

    if message in ('привет', 'здравствуй'):
        return "Привет! Я AI-ассистент для научных исследований созданный с помощью фреймворка GigaChain."

    if message in ('ты кто?', 'who are you',
                   'who are you?', 'кто ты', 'кто ты?'):
        return "Я AI-ассистент для научных исследований созданный с помощью фреймворка GigaChain."

    return ""
