from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from telegram.ext import Application, CommandHandler, ContextTypes, CallbackQueryHandler
import random
from DataBaseManager import DataBaseManager
from CredentialsVault import CredentialsVault


class SergeantPainBot:
    def __init__(self):
        self.cred_vault = CredentialsVault()
        self.cred_reference = self.cred_vault.app_name
        self.telegram_token = self.cred_vault.retrive_credential(self.cred_reference)
        if self.telegram_token is None or self.telegram_token == "":
            print("Please add a Telegram bot token and try again!")
            return

        self.db = DataBaseManager()
        self.application = Application.builder().token(self.telegram_token).build()
        self._register_handlers()
        self.max_button_length = 50  # Fill question/answer string with spaces to adjust button lenght

    def _register_handlers(self):
        self.application.add_handler(CommandHandler("start", self.start))
        self.application.add_handler(CallbackQueryHandler(self.handle_button_click))

    def pad_text(self, text):
        # Workaround to change the button length
        return text + ' ' * self.max_button_length

    def get_active_user_count(self):
        # Count the number of active users
        return len(self.application.user_data)

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        context.user_data['asked_questions'] = set()  # Initialize asked questions set for the user
        await self.show_main_menu(update)

    async def handle_button_click(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        query = update.callback_query
        await query.answer()

        if query.data == "adjust_session":
            await query.edit_message_text(text="Diese Funktion ist noch nicht implementiert.")
            await self.show_main_menu(query)
        elif query.data == "start_round":
            context.user_data['asked_questions'].clear()  # Clear the asked questions set for a new session
            await self.send_random_question(query, context)
        elif query.data == "show_answer":
            question = context.user_data.get('current_question')
            if question:
                keyboard = [
                    [InlineKeyboardButton(self.pad_text("NÄCHSTE FRAGE"), callback_data="next_question")],
                    [InlineKeyboardButton(self.pad_text("SITZUNG BEENDEN"), callback_data="end_session")]
                ]
                reply_markup = InlineKeyboardMarkup(keyboard)
                text = f"Frage: {question['frage']}\n\nAntwort: {question['antwort']}"
                await query.edit_message_text(text=text, reply_markup=reply_markup)
        elif query.data == "next_question":
            await self.send_random_question(query, context)
        elif query.data == "end_session":
            await self.end_session(query, context)

    def get_random_question(self, context):
        rows = self.db.get_all_fragen_antworten()
        asked_questions = context.user_data['asked_questions']
        available_questions = [row for row in rows if row[0] not in asked_questions]
        if available_questions:
            question = random.choice(available_questions)
            asked_questions.add(question[0])
            context.user_data['current_question'] = {"id": question[0], "frage": question[1], "antwort": question[2]}
            return context.user_data['current_question']
        else:
            return None

    async def send_random_question(self, query, context):
        question = self.get_random_question(context)
        if question:
            context.user_data['current_question'] = question
            keyboard = [
                [InlineKeyboardButton(self.pad_text("ZEIGE ANTWORT"), callback_data="show_answer")],
                [InlineKeyboardButton(self.pad_text("SITZUNG BEENDEN"), callback_data="end_session")]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            await query.edit_message_text(text=question['frage'], reply_markup=reply_markup)
        else:
            await self.show_main_menu(query.message, message="Sitzung beendet.")

    async def end_session(self, query, context):
        context.user_data['asked_questions'].clear()  # Reset the asked questions set
        await self.show_main_menu(query)

    async def show_main_menu(self, entity, message="Aktive Nutzer"):
        user_count = self.get_active_user_count()
        keyboard = [
            [InlineKeyboardButton(self.pad_text("SITZUNG ANPASSEN"), callback_data="adjust_session"),
             InlineKeyboardButton(self.pad_text("STARTE FRAGERUNDE"), callback_data="start_round")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        if isinstance(entity, Update):
            await entity.message.reply_text(text=f"{message}: {user_count}", reply_markup=reply_markup)
        elif isinstance(entity, CallbackQuery):
            await entity.edit_message_text(text=f"{message}: {user_count}", reply_markup=reply_markup)

    def run(self):
        self.application.run_polling()


if __name__ == '__main__':
    bot = SergeantPainBot()
    bot.run()
