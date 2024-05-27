import os

from dotenv import load_dotenv
from telegram import BotCommand, InputTextMessageContent
from telegram.ext import (Application, ApplicationBuilder, CommandHandler,
                          MessageHandler, filters)

import answers
from gigachat_tools.agent import ScientificAIAgent


class ScientificAssistantBot:
    def __init__(self):
        self.application = ApplicationBuilder() \
            .token(os.environ['TELEGRAM_BOT_TOKEN']) \
            .post_init(self.post_init) \
            .concurrent_updates(True) \
            .build()

        self.commands = [
            BotCommand(command='help', description="Помощь, описание."),
            BotCommand(command='start', description="Команда старт"),
        ]
        self.gigachain_agent = ScientificAIAgent()

    @staticmethod
    async def start_command(update, context):
        await update.message.reply_text(f"Привет {update.message.from_user.first_name}! " +
                                        "Я ИИ-ассистент, помогаю  в научной деятельности.")

    @staticmethod
    async def help_command(update, context):
        await update.message.reply_text("Вы можете задать вопрос по интесующей \
            Вас тематике, а я попробую найти ответ в своей базе данных или \
            обращусь за ответом к GigaChat.")

    async def handle_message(self, update, context):
        user_text_request = str(update.message.text).lower()
        response = answers.standard_answers(user_text_request)

        # Если ответ не найден, используем модель GigaChat для получения ответа
        if not response:
            response = self.gigachain_agent.response_to_user_request(
                user_id=update.message.from_user['id'],
                user_text_request=user_text_request)

        await update.message.reply_text(response)

    @staticmethod
    def error(update, context):
        print(f'Update {update} caused error: {context.error}')

    async def post_init(self, application: Application) -> None:

        await application.bot.set_my_commands(self.commands)

    def start_bot(self):
        self.application.add_handler(
            CommandHandler(
                'start', self.start_command))
        self.application.add_handler(CommandHandler('help', self.help_command))

        self.application.add_handler(
            MessageHandler(
                filters.TEXT,
                self.handle_message))

        self.application.add_error_handler(self.error)

        self.application.run_polling()


if __name__ == "__main__":
    # Read .env file
    load_dotenv()

    bot = ScientificAssistantBot()
    print('Bot started')

    bot.start_bot()
    print('Bot stopped')
