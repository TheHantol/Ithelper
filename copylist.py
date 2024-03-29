@bot.message_handler(commands=['info'])
def info(message):
    bot.send_message(message.chat.id,
                     f'У меня ты сможешь не только подготовиться к ЕГЭ но и еще узнать ответы на ЕГЭ, ОГЭ как диагностические работы так и экзамены только тсссс...')
    bot.send_message(message.chat.id, f'во мне заложены много программ которые помогут тебе в продвижении к 100 балам.')
    bot.send_message(message.chat.id,
                     f'я могу предоставить тебе: теории, задания, видеоуроки, ну а если тебе хочется иметь достум к материалу вне сети я могу предоставить тебе файлы с теорией и с вариантми ЕГЭ и ОГЭ')


@bot.message_handler(commands=['theory'])
def theory(message):
    bot.send_message(message.chat.id, f'На какое задание тебе нужна теория с заданиями ОГЭ или ЕГЭ?')


@bot.message_handler(commands=['EGE'])
def EGE(message):
    bot.send_message(message.chat.id, f'В моем арсенале есть теория на задание 1-27.')
    bot.send_message(message.chat.id, f'Вот тебе сайт с тиорией там есть все что тебе нужно. https://ctege.info')
    bot.send_message(message.chat.id,
                     f'Ну а если тебе нужны задания то вот сайт для практики. https://inf-ege.sdamgia.ru/?redir=1')
    bot.send_message(message.chat.id, f'Нужна будет помощь зови!')
    bot.send_message(message.chat.id, f'Удачи в подготовке!!')


@bot.message_handler(commands=['OGE'])
def OGE(message):
    bot.send_message(message.chat.id, f'В моем арсенале есть теория на задание 1-15 выбирай.')
    bot.send_message(message.chat.id,
                     f'Вот тебе сайт сайт с теорией там есть все что тебе нужно. https://ctege.info/teoriya-oge-po-informatike/sbornik-teorii-dlya-informatiki-oge.html')
    bot.send_message(message.chat.id,
                     f'Ну а если тебе нужны задания то вот сайт для практики. https://inf-oge.sdamgia.ru/')
    bot.send_message(message.chat.id, f'Нужна будет помощь зови!')
    bot.send_message(message.chat.id, f'Удачи в подготовке!!')


@bot.message_handler(commands=['video_EGE'])
def video_EGE(message):
    bot.send_message(message.chat.id, f'Я вас понял сейчас вы получите видеуроки по всем заданиям.')
    bot.send_message(message.chat.id,
                     f'Задание 1-27:https://www.youtube.com/watch?v=vJ-8xl6SpcU&list=PLa2Ie7RlCO_PmixwJMuVQiGqepMW6eAcV')
    bot.send_message(message.chat.id, f'Удачи с подготовкой!')


@bot.message_handler(commands=['video_OGE'])
def video_OGE(message):
    bot.send_message(message.chat.id, f'Я вас понял сейчас вы получите видеуроки по всем заданиям.')
    bot.send_message(message.chat.id,
                     f'Задание 1-15:https://www.youtube.com/watch?v=BvaYKV4Oa3U&list=PLa2Ie7RlCO_NSuh586_Ew7pkoFr-NZdFz')
    bot.send_message(message.chat.id, f'Удачи с подготовкой!')


@bot.message_handler(commands=['Python_lvl_1'])
def python_lvl_1(message):
    bot.send_message(message.chat.id, f'Я услышал ваш запрос.')
    bot.send_message(message.chat.id,
                     f'К вашему вниманию я предоставляю учебник по програмированнию для начинающих.https://pymanual.github.io/')
    bot.send_message(message.chat.id, f'Удачи с обучением!')


bot.infinity_polling(none_stop=True)
