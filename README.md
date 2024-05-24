Sergeant Pain - Dein freundlicher IHK-Prüfer

I created the Telegram bot "@Sergeant_Pain_Bot" to help you prepare for the final oral exam (Fachgespräch) for IT specialists in application development (in Germany). By pressing the button "STARTE FRAGERUNDE," you can access the most common questions and answers that might appear in the exam. The bot presents a question, and by clicking the "ZEIGE ANTWORT" button, the answer is displayed. You can then proceed to the next question by pressing "NÄCHSTE FRAGE." The question round can be closed any time using the "SITZUNG BEENDEN" button.

Currently, the database contains only questions and answers relevant to IT specialists in application development. However, you can populate it with data from other fields relevant to you and use it as a supportive measure for your exam preparation.

If you notice errors or would like to add more data to the question/answer pool, let me know :)

You can see the bot in action here: https://t.me/Sergeant_Pain_Bot


How to use:

1. Create a Telegram bot via 'https://t.me/BotFather'.
2. Go to the AddTelegramTokenToWCM.py file.
3. Add your Telegram bot token from BotFather to " telegram_token = 'ADD_HERE' ".
4. Run the AddTelegramTokenToWCM.py file once. If you see the token output in the terminal and both the saved and retrieved Telegram tokens are exactly the same as from BotFather, you are good to go.
5. Run the file 'SergeantPain.py'.
6. You can now start your Telegram bot.


Add questions/answers to the SQLite database:

1. Go to 'AddQandA.py' file.
2. Add the question and answer to db_manager.insert_frage_antwort("ADD_HERE_QUESTION", "ADD_HERE_ANSWER").
3. Run the file.
4. For each question, add a new db_manager.insert_frage_antwort("...", "...").
5. Watch out for duplicates; there are no UNIQUE constraints.
