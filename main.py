import telebot
import requests
from telebot import types
import config
from requests import get
from string import Template

bot = telebot.TeleBot(config.token)
# 1601346045:AAGJmy3cj6cIHNCfjgZStnJIhQbsB37xwaQ test
# 5624365764:AAHkqKJ9tI0oxG1fqXB57C_fBTROf1oCuXc osnova


#@bot.message_handler(commands=['start'])
@bot.message_handler(func=lambda message: message.text == "/start")
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton('❤️‍🔥РАСПИСАНИЕ❤️‍🔥')
    itembtn2 = types.KeyboardButton('🫥ЗАДАТЬ ВОПРОС🫥')
    itembtn3 = types.KeyboardButton('⚙ПРОЧЕЕ⚙️')
    itembtn4 = types.KeyboardButton('💣СОЗДАТЕЛИ💣')
    itembtn5 = types.KeyboardButton('📚📚 ЖУРНАЛ 📚📚')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5)
    msg = bot.send_message(message.chat.id,
                           '❗*ГЛАВНОЕ МЕНЮ*❗\n\nПривет, ' + message.from_user.first_name + '\nОзнакомься с моими возможностями:'
                                                                                       '\n'
                                                                                       '  \n📍 В разделе *РАСПИСАНИЕ* можно узнать расписание на всю неделю как на чётную, так '
                                                                                       'и на нечётную.'
                                                                                       '\n '
                                                                                       ' \n📍 Боту можно задать вопрос, в разделе *ЗАДАТЬ ВОПРОС*, абсолютно на любую тему,'
                                                                                       ' как по учебнопу процессу, так и по технической части бота, также тут можно оставить свои пожелания.'
                                                                                       '\n '
                                                                                       ' \n📍 '
                                                                                       'В разделе *ПРОЧЕЕ* Вы можете воспользоваться другими функциями бота.'
                                                                                       '\n'
                                                                                       '\n📍 В разделе *СОЗДАТЕЛИ* можно увидить людей которых надо знать в лицо !'
                                                                                       '\n '
                                                                                       '\n📍 В разделе *ЖУРНАЛ* можно посмотеть свои текущие оценки и посещaемость.'
                                                                                       '\n'
                                                                                        ' \nВ дальнейшем функций будет больше'
                                                                                       ,
                           reply_markup=markup, parse_mode="Markdown" )

    bot.register_next_step_handler(msg, process_select_step)


def process_select_step(message):
    try:
        if (message.text == '❤️‍🔥РАСПИСАНИЕ❤️‍🔥'):
            inlinetimetable(message)
        elif message.text == 'сокирко':
            bot.send_message(message.chat.id, 'сокирка хуисос!')
        elif message.text == 'сокирка':
            bot.send_message(message.chat.id, 'сокирка гений!')
        elif message.text == 'Дмитрий':
            bot.send_message(message.chat.id, 'спортцмен!')
        elif message.text == 'Димасик':
            bot.send_message(message.chat.id, 'хуй его знает кто это!')
        elif message.text == 'Евгений':
            bot.send_message(message.chat.id, 'калпак')
        elif message.text == 'Ярослав':
            bot.send_message(message.chat.id, 'нефр')
        elif message.text == 'Эльнур':
            bot.send_message(message.chat.id, 'профессиональный футболист')
        elif message.text == 'Александр':
            bot.send_message(message.chat.id, 'еще один админ')
        elif message.text == 'Абдо':
            bot.send_message(message.chat.id, 'Ищет каршеринг')
        elif message.text == 'Сокирко':
            bot.send_message(message.chat.id, 'Курит крэк')
        elif message.text == 'Терал':
            bot.send_message(message.chat.id, 'Его все бесит')
        elif message.text == 'Яна':
            bot.send_message(message.chat.id, 'внатуре')
        elif message.text == 'Ульяна':
            bot.send_message(message.chat.id, 'внатуре но немного другое')
        elif message.text == 'Катя':
            bot.send_message(message.chat.id, 'Очень любит математику')

        elif (message.text == '⚙ПРОЧЕЕ⚙️'):
            more(message)
        elif (message.text == '🫥ЗАДАТЬ ВОПРОС🫥'):
            qustion(message)
        elif (message.text == '💣СОЗДАТЕЛИ💣'):
            twogenius(message)
        elif (message.text == '📚📚 ЖУРНАЛ 📚📚'):
            excel(message)
        else:
            elseifstart(message)
    except Exception as e:
        bot.reply_to(message, '')


@bot.message_handler(func=lambda message: message.text == "/excel")
def excel(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    itembtn1 = types.KeyboardButton('🔙Назад🔙')
    markup.add(itembtn1)
    bot.send_message(message.chat.id, '*📚📚 ЖУРНАЛ 📚📚*\n'
                     , reply_markup=markup, parse_mode="Markdown")
    msg = bot.send_message(message.chat.id, 
                                            '\nПерейдите по этой ссылке для попадания в журнал!\n 9103 - https://docs.google.com/spreadsheets/d/1mM_U_w1RFo0Eor6Ac08yigOBkp5ohyhKUvO20ybJvaM/edit#gid=0 '
                                            '\n \nЖурнал для всех групп - https://vk.com/doc302315531_649072069?hash=tX3yKpyiZpgncm3FVqGap32EyZAkVaoQVB1KXgV2A8w&dl=rZz8PK9JARycEZphlCs7sr9zzziY8cvYfHCEOqaZz2z '
                                            , reply_markup=markup)
    bot.register_next_step_handler(msg, process_select_create_excel)


def process_select_create_excel(message):
    try:
        if (message.text == '🔙Назад🔙'):
            start(message)
        else:
            elseifstart(message)
    except Exception as e:
        bot.reply_to(message, '')


#@bot.message_handler(commands=['qustion'])
@bot.message_handler(func=lambda message: message.text == "/qustion")
def qustion(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    itembtn1 = types.KeyboardButton('🔙НАЗАД🔙')
    markup.add(itembtn1)
    msg = bot.send_message(message.chat.id, '\n*🫥ЗАДАТЬ ВОПРОС🫥*\n \n Здесть ты можешь задать свой вопрос!\n \n '
                                            'Если хочешь вернуться назад нажми кнопку *🔙НАЗАД🔙*!'
                                            '\n \n Напишите ваш вопрос: '
                                            , reply_markup=markup, parse_mode="Markdown")
    bot.register_next_step_handler(msg, process_select_create_request)


def process_select_create_request(message):
    try:
        if (message.text == '🔙НАЗАД🔙'):
            start(message)
        else:
            create_request(message)
    except Exception as e:
        bot.reply_to(message, '')


def create_request(message):
    bot.send_message(message.chat.id, 'Ваш вопрос отправлен\nВ ближайшее время с вами свяжутся')
    bot.forward_message(config.chat_id, message.chat.id, message.message_id)
    msg = bot.send_message(config.chat_id, 'ВОПРОС : \n{0}\n ОТ :\n{1}\n{2}'.format(message.text, message.from_user.first_name, message.from_user.last_name))
    bot.register_next_step_handler(msg, start)


#@bot.message_handler(commands=['twogenius'])
@bot.message_handler(func=lambda message: message.text == "/twogenius")
def twogenius(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    itembtn1 = types.KeyboardButton('🔙Назад🔙')
    itembtn2 = types.KeyboardButton('⚠️Дополнительные возможности⚠️')
    markup.add(itembtn2, itembtn1)
    bot.send_message(message.chat.id,
                     '*💣СОЗДАТЕЛИ💣*\n\nТы знал что этот бот был создан благодаря этим двум гениям?',
                     reply_markup=markup, parse_mode="Markdown")
    msg = bot.send_message(message.chat.id,
                           '\n Разработчик - https://vk.com/eugene.alpatov \n ',
                           reply_markup=markup)
    #bot.send_photo(message.chat.id, get(
     #   "https://sun9-62.userapi.com/impg/eiLfQcUNWsU26WjX4nPcmpBT3G-wBiHWVUqltw/_ppKmyUl3AQ.jpg?size=1279x1600&quality=95&sign=81b87e53e51f5b2a308cebf5b469014b&type=album").content)
    bot.send_photo(message.chat.id, open('pic/eugene.jpg', 'rb'))
    bot.send_message(message.chat.id,
                     '\n Мерчендайзер, промоутер - https://vk.com/sashavarz')
    # bot.send_photo(message.chat.id, get(
    #     "https://sun9-48.userapi.com/impg/64zc9ZEYyHcUtrpxJYWAV6A1MSusT0jlWAb3VA/gDmX3iSStA8.jpg?size=1280x960&quality=95&sign=50cf2058f85069dab9c1e4fb97f27ecc&type=album").content)
    bot.send_photo(message.chat.id, open('pic/sashawar.jpg', 'rb'))
    bot.register_next_step_handler(msg, process_select_twogenius)


def process_select_twogenius(message):
    try:
        if (message.text == '🔙Назад🔙'):
            start(message)
        elif (message.text == '⚠️Дополнительные возможности⚠️'):
            special(message)
        else:
            elseifstart(message)
    except Exception as e:
        bot.reply_to(message, '')
#     bot.send_message(message.chat.id, '/start - вернуться назад\n')


def special(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    itembtn1 = types.KeyboardButton('🔙Назад🔙')
    markup.add(itembtn1)
    msg = bot.send_message(message.chat.id,
                           'Введите пароль: \n\n\n\nУ вас 1 попытка...',
                           reply_markup=markup)
    bot.register_next_step_handler(msg, process_select_special)


def process_select_special(message):
    try:
        if (message.text == '🔙Назад🔙'):
            twogenius(message)
        elif (message.text == 'rihbs23'):
            special_main(message)
        else:
            bot.send_message(message.chat.id, 'пароль не верный')
            start(message)
    except Exception as e:
        bot.reply_to(message, '')


def special_main(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    itembtn1 = types.KeyboardButton('🔙Назад🔙')
    markup.add(itembtn1)
    msg = bot.send_message(message.chat.id,
                           'Секретная страница \nЧто тут делать, Александр?',
                           reply_markup=markup)
    bot.register_next_step_handler(msg, process_select_special_main)


def process_select_special_main(message):
    try:
        if (message.text == '🔙Назад🔙'):
            special(message)
        else:
            elseifstart(message)
    except Exception as e:
        bot.reply_to(message, '')


#@bot.message_handler(commands=["timetable"])
@bot.message_handler(func=lambda message: message.text == "/timetable")
def inlinetimetable(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton('⬆️Верхняя⬆️')
    itembtn2 = types.KeyboardButton('⬇️Нижняя⬇️')
    itembtn3 = types.KeyboardButton('🔙Назад🔙')
    markup.add(itembtn1, itembtn2, itembtn3)
    msg = bot.send_message(message.chat.id,
                           '*❤️‍🔥РАСПИСАНИЕ❤️‍🔥*\n'
                           '\nРасписание для группы *9103*\n'
                           '\nПривет, ' + message.from_user.first_name + ', выбери неделю!',
                           reply_markup=markup, parse_mode="Markdown")
    bot.register_next_step_handler(msg, process_select_week)


def process_select_week(message):
    try:
        if (message.text == '⬆️Верхняя⬆️'):
            topweek(message)
        elif (message.text == '⬇️Нижняя⬇️'):
            bottonweek(message)
        elif (message.text == '🔙Назад🔙'):
            start(message)
        else:
            elseifstart(message)
    except Exception as e:
        bot.reply_to(message, 'Error 404')


def topweek(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton('Понедельник')
    itembtn2 = types.KeyboardButton('Вторник')
    itembtn3 = types.KeyboardButton('Среда')
    itembtn4 = types.KeyboardButton('Четверг')
    itembtn5 = types.KeyboardButton('Пятница')
    itembtn6 = types.KeyboardButton('Суббота')
    itembtn7 = types.KeyboardButton('🔙Назад🔙')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6, itembtn7)
    msg = bot.send_message(message.chat.id,
                           'Привет, ' + message.from_user.first_name + ',выбери кнопку и нажми её!',
                           reply_markup=markup)
    bot.register_next_step_handler(msg, process_select_topweek)


def process_select_topweek(message):
    try:
        if (message.text == 'Понедельник'):
            mondaytop(message)
        elif (message.text == 'Вторник'):
            tuesdaytop(message)
        elif (message.text == 'Среда'):
            sredatop(message)
        elif (message.text == 'Четверг'):
            fourdaytop(message)
        elif (message.text == 'Пятница'):
            freedaytop(message)
        elif (message.text == 'Суббота'):
           sutarday(message)
        elif (message.text == '🔙Назад🔙'):
           inlinetimetable(message)
        else:
            elseifstart(message)
    except Exception as e:
        bot.reply_to(message, 'Error 404')


def mondaytop(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton('🔙Назад🔙')
    markup.add(itembtn1)
    msg = bot.send_message(message.chat.id,
                           '❗️Верхняя неделя❗️\n1. (Пр.) Английский язык 12-14 \n2. (Пр.) Конституционное право 13-05 \n3. (Пр.) Теория государства и права 11-03 \n4. (Л.) Конституционное право 32-11',
                           reply_markup=markup)
    bot.register_next_step_handler(msg, process_select_back)


def tuesdaytop(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton('🔙Назад🔙')
    markup.add(itembtn1)
    msg = bot.send_message(message.chat.id,
                           '❗️Верхняя неделя❗️\n1. (Пр.) Математика 11-04 \n2. (Л.) ИГИПЗС 11-19 \n3. - \n4. -',
                           reply_markup=markup)
    bot.register_next_step_handler(msg, process_select_back)


def sredatop(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton('🔙Назад🔙')
    markup.add(itembtn1)
    msg = bot.send_message(message.chat.id,
                           '❗️Верхняя неделя❗️\n1. - \n2. (Л.) Уголовное право 32-11 \n3. - \n4. (Л.) Гражданское право 32-13 \n5. (Пр.) Гражданское право 11-10',
                           reply_markup=markup)
    bot.register_next_step_handler(msg, process_select_back)


def fourdaytop(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton('🔙Назад🔙')
    markup.add(itembtn1)
    msg = bot.send_message(message.chat.id,
                           '❗️Верхняя неделя❗️\n1. (Л.) Теория государства и права 11-19 \n2. (Л.) История 11-10 \n3. (Пр.) История 31-01 \n4. -',
                           reply_markup=markup)
    bot.register_next_step_handler(msg, process_select_back)


def freedaytop(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton('🔙Назад🔙')
    markup.add(itembtn1)
    msg = bot.send_message(message.chat.id,
                           '❗️Верхняя неделя❗️\n1. (Пр.) Математика 11-04 \n2. (Пр.) Психология 11-09 \n3. (Л.) Психология 11-19 \n4. (Л.) Римское право 11-10',
                           reply_markup=markup)
    bot.register_next_step_handler(msg, process_select_back)


def sutarday(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton('🔙Назад🔙')
    markup.add(itembtn1)
    msg = bot.send_message(message.chat.id,
                           '1. (Пр.) ИГИПЗС 11-09 \n2. (Пр.) Физкультура  \n3. (Л.) ИГИПЗС 11-10 \n4.-',
                           reply_markup=markup)
    bot.register_next_step_handler(msg, process_select_back)


def process_select_back(message):
    try:
        if (message.text == '🔙Назад🔙'):
            topweek(message)
        else:
            elseifstart(message)
    except Exception as e:
        bot.reply_to(message, '')


def bottonweek(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton('Понедельник')
    itembtn2 = types.KeyboardButton('Вторник')
    itembtn3 = types.KeyboardButton('Среда')
    itembtn4 = types.KeyboardButton('Четверг')
    itembtn5 = types.KeyboardButton('Пятница')
    itembtn6 = types.KeyboardButton('Суббота')
    itembtn7 = types.KeyboardButton('🔙Назад🔙')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6, itembtn7)
    msg = bot.send_message(message.chat.id,
                           'Привет, ' + message.from_user.first_name + ',выбери кнопку и нажми её!',
                           reply_markup=markup)
    bot.register_next_step_handler(msg, process_select_bottonweek)


def process_select_bottonweek(message):
    try:
        if (message.text == 'Понедельник'):
            mondaybotton(message)
        elif (message.text == 'Вторник'):
            tuesdaybotton(message)
        elif (message.text == 'Среда'):
            sredabotton(message)
        elif (message.text == 'Четверг'):
            fourdaybotton(message)
        elif (message.text == 'Пятница'):
            freedaybotton(message)
        elif (message.text == 'Суббота'):
           sutarday(message)
        elif (message.text == '🔙Назад🔙'):
           inlinetimetable(message)
        else:
            elseifstart(message)
    except Exception as e:
        bot.reply_to(message, 'Error 404')


def mondaybotton(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton('🔙Назад🔙')
    markup.add(itembtn1)
    msg = bot.send_message(message.chat.id,
                           '❗️Нижняя неделя❗\n1. (Пр.) Английский язык 12-14 \n2. (Пр.) Конституционное право 13-05  \n3. - \n4. (Л.) Конституционное право 32-11',
                           reply_markup=markup)
    bot.register_next_step_handler(msg, process_select_backbotton)


def tuesdaybotton(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton('🔙Назад🔙')
    markup.add(itembtn1)
    msg = bot.send_message(message.chat.id,
                           '❗️Нижняя неделя❗\n1. (Пр.) Математика 11-04 \n2. - \n3. - \n4. -',
                           reply_markup=markup)
    bot.register_next_step_handler(msg, process_select_backbotton)


def sredabotton(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton('🔙Назад🔙')
    markup.add(itembtn1)
    msg = bot.send_message(message.chat.id,
                           '❗️Нижняя неделя❗\n1. - \n2. (Л.) Уголовное право 32-11 \n3. (Пр.) Уголовное право 11-10 \n4. (Л.) Гражданское право 32-13 \n5. (Пр.) Гражданское право 11-10',
                           reply_markup=markup)
    bot.register_next_step_handler(msg, process_select_backbotton)


def fourdaybotton(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton('🔙Назад🔙')
    markup.add(itembtn1)
    msg = bot.send_message(message.chat.id,
                           '❗️Нижняя неделя❗\n1. (Л.) Теория государства и права 11-19 \n2. (Л.) История 11-10 \n3. (Пр.) Теория государства и права 11-04 \n4. -',
                           reply_markup=markup)
    bot.register_next_step_handler(msg, process_select_backbotton)


def freedaybotton(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton('🔙Назад🔙')
    markup.add(itembtn1)
    msg = bot.send_message(message.chat.id,
                           '❗️Нижняя неделя❗\n️1. (Пр.) Математика 11-04 \n2. - \n3. (Л.) Психология 11-19 \n4. (Л.) Римское право 11-10',
                           reply_markup=markup)
    bot.register_next_step_handler(msg, process_select_backbotton)


def process_select_backbotton(message):
    try:
        if (message.text == '🔙Назад🔙'):
            bottonweek(message)
        else:
            elseifstart(message)
    except Exception as e:
        bot.reply_to(message, '')


@bot.message_handler(func=lambda m: True)
def message(message):
    if message.text == 'Привет':
        bot.send_message(message.chat.id, 'Привет,друг!')
    elif message.text == 'hi':
        bot.send_message(message.chat.id, 'Hi again!')
    elif message.text == 'сокирко':
        bot.send_message(message.chat.id, 'соирка хуисос!')
    elif message.text == 'Пока':
        bot.send_message(message.chat.id, 'До свидания! Хорошего дня!)')
    elif message.text == 'Hi':
        bot.send_message(message.chat.id, 'Hi again! , ' + message.from_user.first_name + '!How are you?!')
    elif message.text == 'привет':
        bot.send_message(message.chat.id, 'ПРИВЕТ! , ' + message.from_user.first_name)

    else:
        elseifstart(message)


@bot.message_handler(func=lambda message: message.text == "/elseifstart")
def elseifstart(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    itembtn1 = types.KeyboardButton('⚜ МЕНЮ ️⚜')
    markup.add(itembtn1)
    msg = bot.send_message(message.chat.id, ' ⚠*ПОХОЖЕ ЧТО-ТО ПОШЛО НЕ ТАК*!️⚠️'
                                            '\n '
                                            '\n ♻️Ничего страшного, просто нажмите кнопку ниже чтобы перейти в *ГЛАВНОЕ МЕНЮ*! ️'
                                            '\n'
                                            '\n⚙️🛠 *PS*: Такое происходит из-за сбоев на сервере либо из-за ввода неверных команд '
                                            '\n'
                                            '\n🎉 В последствие мы постараемся уменьшить колличество таких сбоев, спасибо за понимание', reply_markup=markup, parse_mode="Markdown")
    bot.register_next_step_handler(msg, process_select_create_elseif)


def process_select_create_elseif(message):
    try:
        if (message.text == '⚜ МЕНЮ ️⚜'):
            start(message)
        else:
            elseifstart(message)
    except Exception as e:
        bot.reply_to(message, '')


@bot.message_handler(commands=['more'])
def more(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    itembtn1 = types.KeyboardButton('🔙Назад🔙')
    itembtn2 = types.KeyboardButton('🍻💉Расписание других групп💊🩸')
    markup.add(itembtn2, itembtn1)
    msg = bot.send_message(message.chat.id, '*⚙ПРОЧЕЕ⚙️* \n'
                                            '\nВ этом разделе находятся дополнительные возможности! '
                                            '\n'
                                            '\n *РАСПИСАНИЕ ДРУГИХ ГРУПП* - содержит распиание других групп', reply_markup=markup, parse_mode="Markdown")
    bot.register_next_step_handler(msg, process_select_create_more)


def process_select_create_more(message):
    try:
        if (message.text == '🔙Назад🔙'):
            start(message)
        elif (message.text == '🍻💉Расписание других групп💊🩸'):
            morePlanning(message)
        else:
            elseifstart(message)
    except Exception as e:
        bot.reply_to(message, '')


@bot.message_handler(commands=['morePlanning'])
def morePlanning(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    itembtn1 = types.KeyboardButton('9️⃣1️⃣0️⃣1️⃣')
    itembtn2 = types.KeyboardButton('9️⃣1️⃣0️⃣2️⃣')
    itembtn3 = types.KeyboardButton('9️⃣1️⃣0️⃣3️⃣')
    itembtn4 = types.KeyboardButton('🔙Назад🔙')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4)
    msg = bot.send_message(message.chat.id, 'Выберете вашу группу!', reply_markup=markup)
    bot.register_next_step_handler(msg, process_select_create_morePlanning)


def process_select_create_morePlanning(message):
    try:
        if (message.text == '🔙Назад🔙'):
            more(message)
        elif (message.text == '9️⃣1️⃣0️⃣1️⃣'):
            inlinetimetable9101(message)
        elif (message.text == '9️⃣1️⃣0️⃣2️⃣'):
            inlinetimetable9102(message)
        elif (message.text == '9️⃣1️⃣0️⃣3️⃣'):
            inlinetimetable(message)
        else:
            elseifstart(message)
    except Exception as e:
        bot.reply_to(message, '')


@bot.message_handler(commands=["timetable9101"])
def inlinetimetable9101(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton('⬆️Верхняя⬆️')
    itembtn2 = types.KeyboardButton('⬇️Нижняя⬇️')
    itembtn3 = types.KeyboardButton('🔙Назад🔙')
    markup.add(itembtn1, itembtn2, itembtn3)
    msg = bot.send_message(message.chat.id,
                           'Привет, ' + message.from_user.first_name + ', выбери неделю!',
                           reply_markup=markup)
    bot.register_next_step_handler(msg, process_select_week9101)


def process_select_week9101(message):
    try:
        if (message.text == '⬆️Верхняя⬆️'):
            topweek9101(message)
        elif (message.text == '⬇️Нижняя⬇️'):
            bottonweek9101(message)
        elif (message.text == '🔙Назад🔙'):
            morePlanning(message)
        else:
            elseifstart(message)
    except Exception as e:
        bot.reply_to(message, 'Error 404')


def topweek9101(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton('Понедельник')
    itembtn2 = types.KeyboardButton('Вторник')
    itembtn3 = types.KeyboardButton('Среда')
    itembtn4 = types.KeyboardButton('Четверг')
    itembtn5 = types.KeyboardButton('Пятница')
    itembtn6 = types.KeyboardButton('Суббота')
    itembtn7 = types.KeyboardButton('🔙Назад🔙')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6, itembtn7)
    msg = bot.send_message(message.chat.id,
                           'Привет, ' + message.from_user.first_name + ',выбери кнопку и нажми её!',
                           reply_markup=markup)
    bot.register_next_step_handler(msg, process_select_topweek9101)


def process_select_topweek9101(message):
    try:
        if (message.text == 'Понедельник'):
            mondaytop9101(message)
        elif (message.text == 'Вторник'):
            tuesdaytop9101(message)
        elif (message.text == 'Среда'):
            sredatop9101(message)
        elif (message.text == 'Четверг'):
            fourdaytop9101(message)
        elif (message.text == 'Пятница'):
            freedaytop9101(message)
        elif (message.text == 'Суббота'):
           sutarday9101(message)
        elif (message.text == '🔙Назад🔙'):
           inlinetimetable9101(message)
        else:
            elseifstart(message)
    except Exception as e:
        bot.reply_to(message, 'Error 404')


def mondaytop9101(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton('Назад')
    markup.add(itembtn1)
    msg = bot.send_message(message.chat.id,
                           '❗️Верхняя неделя❗️\n1. - \n2. - \n3.(Л) Математика \n4. (Л.) Конституционное право \n 5. (Пр.) Конституционное право',
                           reply_markup=markup)
    bot.register_next_step_handler(msg, process_select_back9101)


def tuesdaytop9101(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton('🔙Назад🔙')
    markup.add(itembtn1)
    msg = bot.send_message(message.chat.id,
                           '❗️Верхняя неделя❗️\n1. - \n2. (Л.) ИГИПЗС 11-19 \n3. (Пр) Математика \n4. -',
                           reply_markup=markup)
    bot.register_next_step_handler(msg, process_select_back9101)


def sredatop9101(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton('🔙Назад🔙')
    markup.add(itembtn1)
    msg = bot.send_message(message.chat.id,
                           '❗️Верхняя неделя❗️\n1. (Пр) Уголовное право \n2. (Л.) Уголовное право 32-11 \n3. (Пр) Математика \n4. (Л.) Гражданское право 32-13 \n5. -',
                           reply_markup=markup)
    bot.register_next_step_handler(msg, process_select_back9101)


def fourdaytop9101(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton('🔙Назад🔙')
    markup.add(itembtn1)
    msg = bot.send_message(message.chat.id,
                           '❗️Верхняя неделя❗️\n1. (Л.) Теория государства и права 11-19 \n2. (Л.) История 11-10 \n3. (Пр) Теория государства и права \n4. (Л) Гражданское право',
                           reply_markup=markup)
    bot.register_next_step_handler(msg, process_select_back9101)


def freedaytop9101(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton('🔙Назад🔙')
    markup.add(itembtn1)
    msg = bot.send_message(message.chat.id,
                           '❗️Верхняя неделя❗️\n1. - \n2. (Л) Иностранный язык \n3. (Л.) Психология 11-19 \n4. (Л.) Римское право 11-10',
                           reply_markup=markup)
    bot.register_next_step_handler(msg, process_select_back9101)


def sutarday9101(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton('🔙Назад🔙')
    markup.add(itembtn1)
    msg = bot.send_message(message.chat.id,
                           '1. - \n2. (Пр.) Физкультура  \n3. (Л.) ИГИПЗС 11-10 \n4.-',
                           reply_markup=markup)
    bot.register_next_step_handler(msg, process_select_back9101)


def process_select_back9101(message):
    try:
        if (message.text == '🔙Назад🔙'):
            topweek9101(message)
        else:
            elseifstart(message)
    except Exception as e:
        bot.reply_to(message, '')


def bottonweek9101(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton('Понедельник')
    itembtn2 = types.KeyboardButton('Вторник')
    itembtn3 = types.KeyboardButton('Среда')
    itembtn4 = types.KeyboardButton('Четверг')
    itembtn5 = types.KeyboardButton('Пятница')
    itembtn6 = types.KeyboardButton('Суббота')
    itembtn7 = types.KeyboardButton('🔙Назад🔙')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6, itembtn7)
    msg = bot.send_message(message.chat.id,
                           'Привет, ' + message.from_user.first_name + ',выбери кнопку и нажми её!',
                           reply_markup=markup)
    bot.register_next_step_handler(msg, process_select_bottonweek9101)


def process_select_bottonweek9101(message):
    try:
        if (message.text == 'Понедельник'):
            mondaybotton9101(message)
        elif (message.text == 'Вторник'):
            tuesdaybotton9101(message)
        elif (message.text == 'Среда'):
            sredabotton9101(message)
        elif (message.text == 'Четверг'):
            fourdaybotton9101(message)
        elif (message.text == 'Пятница'):
            freedaybotton9101(message)
        elif (message.text == 'Суббота'):
           sutarday9101(message)
        elif (message.text == '🔙Назад🔙'):
           inlinetimetable9101(message)
        else:
            elseifstart(message)
    except Exception as e:
        bot.reply_to(message, 'Error 404')


def mondaybotton9101(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton('🔙Назад🔙')
    markup.add(itembtn1)
    msg = bot.send_message(message.chat.id,
                           '❗️Нижняя неделя❗\n1. - \n2. -  \n3. (Пр) Теория государства и права \n4. (Л.) Конституционное право 32-11 \n 5. (Пр) Конституционное',
                           reply_markup=markup)
    bot.register_next_step_handler(msg, process_select_backbotton9101)


def tuesdaybotton9101(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton('🔙Назад🔙')
    markup.add(itembtn1)
    msg = bot.send_message(message.chat.id,
                           '❗️Нижняя неделя❗\n1. - \n2. - \n3. - \n4. -',
                           reply_markup=markup)
    bot.register_next_step_handler(msg, process_select_backbotton9101)


def sredabotton9101(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton('🔙Назад🔙')
    markup.add(itembtn1)
    msg = bot.send_message(message.chat.id,
                           '❗️Нижняя неделя❗\n1. - \n2. (Л.) Уголовное право 32-11 \n3. (Л) Математика \n4. (Л.) Гражданское право 32-13 \n5. -',
                           reply_markup=markup)
    bot.register_next_step_handler(msg, process_select_backbotton9101)


def fourdaybotton9101(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton('🔙Назад🔙')
    markup.add(itembtn1)
    msg = bot.send_message(message.chat.id,
                           '❗️Нижняя неделя❗\n1. (Л.) Теория государства и права 11-19 \n2. (Л.) История 11-10 \n3. (Пр.) (Л) Математика \n4. (Пр) Гражданское право \n 5. (Пр) История государства и права зарубежных стран',
                           reply_markup=markup)
    bot.register_next_step_handler(msg, process_select_backbotton9101)


def freedaybotton9101(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton('🔙Назад🔙')
    markup.add(itembtn1)
    msg = bot.send_message(message.chat.id,
                           '❗️Нижняя неделя❗\n️1. (Пр) Психология \n2. (Л) Иностранный язык \n3. (Л.) Психология 11-19 \n4. (Л.) Римское право 11-10',
                           reply_markup=markup)
    bot.register_next_step_handler(msg, process_select_backbotton9101)


def process_select_backbotton9101(message):
    try:
        if (message.text == '🔙Назад🔙'):
            bottonweek9101(message)
        else:
            elseifstart(message)
    except Exception as e:
        bot.reply_to(message, '')


@bot.message_handler(commands=["timetable9102"])
def inlinetimetable9102(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton('⬆️Верхняя⬆️')
    itembtn2 = types.KeyboardButton('⬇️Нижняя⬇️')
    itembtn3 = types.KeyboardButton('🔙Назад🔙')
    markup.add(itembtn1, itembtn2, itembtn3)
    msg = bot.send_message(message.chat.id,
                           'Привет, ' + message.from_user.first_name + ', выбери неделю!',
                           reply_markup=markup)
    bot.register_next_step_handler(msg, process_select_week9102)


def process_select_week9102(message):
    try:
        if (message.text == '⬆️Верхняя⬆️'):
            topweek9102(message)
        elif (message.text == '⬇️Нижняя⬇️'):
            bottonweek9102(message)
        elif (message.text == '🔙Назад🔙'):
            morePlanning(message)
        else:
            elseifstart(message)
    except Exception as e:
        bot.reply_to(message, 'Error 404')


def topweek9102(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton('Понедельник')
    itembtn2 = types.KeyboardButton('Вторник')
    itembtn3 = types.KeyboardButton('Среда')
    itembtn4 = types.KeyboardButton('Четверг')
    itembtn5 = types.KeyboardButton('Пятница')
    itembtn6 = types.KeyboardButton('Суббота')
    itembtn7 = types.KeyboardButton('🔙Назад🔙')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6, itembtn7)
    msg = bot.send_message(message.chat.id,
                           'Привет, ' + message.from_user.first_name + ',выбери кнопку и нажми её!',
                           reply_markup=markup)
    bot.register_next_step_handler(msg, process_select_topweek9102)


def process_select_topweek9102(message):
    try:
        if (message.text == 'Понедельник'):
            mondaytop9102(message)
        elif (message.text == 'Вторник'):
            tuesdaytop9102(message)
        elif (message.text == 'Среда'):
            sredatop9102(message)
        elif (message.text == 'Четверг'):
            fourdaytop9102(message)
        elif (message.text == 'Пятница'):
            freedaytop9102(message)
        elif (message.text == 'Суббота'):
           sutarday9102(message)
        elif (message.text == '🔙Назад🔙'):
           inlinetimetable9102(message)
        else:
            elseifstart(message)
    except Exception as e:
        bot.reply_to(message, 'Error 404')


def mondaytop9102(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton('🔙Назад🔙')
    markup.add(itembtn1)
    msg = bot.send_message(message.chat.id,
                           '❗️Верхняя неделя❗️\n1. (Л) История 11-10 \n2. (Пр) Физическая культура \n3.(Пр) Иностранный язык 31-01 ',
                           reply_markup=markup)
    bot.register_next_step_handler(msg, process_select_back9102)


def tuesdaytop9102(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton('🔙Назад🔙')
    markup.add(itembtn1)
    msg = bot.send_message(message.chat.id,
                           '❗️Верхняя неделя❗️\n1. - \n2. (Л) Теория государства и права 11-10 \n3. (Пр) Математика \n4. (Пр) Теория государства и права 11-07',
                           reply_markup=markup)
    bot.register_next_step_handler(msg, process_select_back9102)


def sredatop9102(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton('🔙Назад🔙')
    markup.add(itembtn1)
    msg = bot.send_message(message.chat.id,
                           '❗️Верхняя неделя❗️\n1. - \n2. (Л.) Уголовное право 32-11 \n3. (Пр) Психология 12-14 \n4. (Л.) Гражданское право 32-13 \n5. -',
                           reply_markup=markup)
    bot.register_next_step_handler(msg, process_select_back9102)


def fourdaytop9102(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton('🔙Назад🔙')
    markup.add(itembtn1)
    msg = bot.send_message(message.chat.id,
                           '❗️Верхняя неделя❗️\n1. (Пр) История государства и права зарубежных стран 11-17 \n2. (Л) Психология 11-19 \n3. (Пр) Гражданское право 11-04 \n4. (Пр) История 12-14',
                           reply_markup=markup)
    bot.register_next_step_handler(msg, process_select_back9102)


def freedaytop9102(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton('🔙Назад🔙')
    markup.add(itembtn1)
    msg = bot.send_message(message.chat.id,
                           '❗️Верхняя неделя❗️\n1. (Пр) Конституционное право 11-03 \n2. (Пр) Математика 11-04 \n3. (Л) Конституционное право 32-11 '
                           '\n4. (Л.) Римское право 11-10',
                           reply_markup=markup)
    bot.register_next_step_handler(msg, process_select_back9102)


def sutarday9102(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton('🔙Назад🔙')
    markup.add(itembtn1)
    msg = bot.send_message(message.chat.id,
                           '1. - \n2. (Л) История государства и права зарубежных стран 11-19  \n3. (Пр) Уголовное право 11-09 \n4.-',
                           reply_markup=markup)
    bot.register_next_step_handler(msg, process_select_back9102)


def process_select_back9102(message):
    try:
        if (message.text == '🔙Назад🔙'):
            topweek9102(message)
        else:
            elseifstart(message)
    except Exception as e:
        bot.reply_to(message, '')


def bottonweek9102(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton('Понедельник')
    itembtn2 = types.KeyboardButton('Вторник')
    itembtn3 = types.KeyboardButton('Среда')
    itembtn4 = types.KeyboardButton('Четверг')
    itembtn5 = types.KeyboardButton('Пятница')
    itembtn6 = types.KeyboardButton('Суббота')
    itembtn7 = types.KeyboardButton('🔙Назад🔙')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6, itembtn7)
    msg = bot.send_message(message.chat.id,
                           'Привет, ' + message.from_user.first_name + ',выбери кнопку и нажми её!',
                           reply_markup=markup)
    bot.register_next_step_handler(msg, process_select_bottonweek9102)


def process_select_bottonweek9102(message):
    try:
        if (message.text == 'Понедельник'):
            mondaybotton9102(message)
        elif (message.text == 'Вторник'):
            tuesdaybotton9102(message)
        elif (message.text == 'Среда'):
            sredabotton9102(message)
        elif (message.text == 'Четверг'):
            fourdaybotton9102(message)
        elif (message.text == 'Пятница'):
            freedaybotton9102(message)
        elif (message.text == 'Суббота'):
           sutarday9102(message)
        elif (message.text == '🔙Назад🔙'):
           inlinetimetable9102(message)
        else:
            elseifstart(message)
    except Exception as e:
        bot.reply_to(message, 'Error 404')


def mondaybotton9102(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton('🔙Назад🔙')
    markup.add(itembtn1)
    msg = bot.send_message(message.chat.id,
                           '❗️Нижняя неделя❗\n1. (Л) История 11-10 \n2. (Пр) Физическая культура  \n3. (Пр) Иностранный язык 31-01 '
                           ,
                           reply_markup=markup)
    bot.register_next_step_handler(msg, process_select_backbotton9102)


def tuesdaybotton9102(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton('🔙Назад🔙')
    markup.add(itembtn1)
    msg = bot.send_message(message.chat.id,
                           '❗️Нижняя неделя❗\n1. - \n2. (Л) Теория государства и права 11-10 \n3. (Пр) Математика 11-04 \n4. (Л) История государства и права зарубежных стран 11-10',
                           reply_markup=markup)
    bot.register_next_step_handler(msg, process_select_backbotton9102)


def sredabotton9102(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton('🔙Назад🔙')
    markup.add(itembtn1)
    msg = bot.send_message(message.chat.id,
                           '❗️Нижняя неделя❗\n1. - \n2. (Л.) Уголовное право 32-11 \n3. (Пр) Теория государства и права 12-14 \n4. (Л.) Гражданское право 32-13 \n5. -',
                           reply_markup=markup)
    bot.register_next_step_handler(msg, process_select_backbotton9102)


def fourdaybotton9102(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton('🔙Назад🔙')
    markup.add(itembtn1)
    msg = bot.send_message(message.chat.id,
                           '❗️Нижняя неделя❗\n1. (Пр) История государства и права зарубежных стран 11-17 \n2. (Л) Психология 11-19 \n3. (Пр) Гражданское право 11-10',
                           reply_markup=markup)
    bot.register_next_step_handler(msg, process_select_backbotton9102)


def freedaybotton9102(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton('🔙Назад🔙')
    markup.add(itembtn1)
    msg = bot.send_message(message.chat.id,
                           '❗️Нижняя неделя❗\n️1. (Пр) Конституционное право 11-03 \n2. (Пр) Математика 11-04 \n3. (Л) Конституционное право 32-11 \n4. (Л.) Римское право 11-10',
                           reply_markup=markup)
    bot.register_next_step_handler(msg, process_select_backbotton9102)


def process_select_backbotton9102(message):
    try:
        if (message.text == '🔙Назад🔙'):
            bottonweek9102(message)
        else:
            elseifstart(message)
    except Exception as e:
        bot.reply_to(message, '')


bot.polling()
