import telebot
from telebot import types
from bs4 import BeautifulSoup as b

bot = telebot.TeleBot('5454173826:AAGGgpAv5anMc6JvdoLuhJxLmjGRzr7pMQ8')
listphoto = ['1.PNG','2.PNG','3.PNG','4.PNG', '5.PNG','6.PNG','7.PNG']
listinstr = ['t1.PNG', 't2.PNG', 't3.PNG', 't5.PNG', 't6.PNG', 't7.PNG']

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    yes = types.KeyboardButton('/go')
    no = types.KeyboardButton('/notnow')
    markup.add(yes, no)
    bot.send_message(message.chat.id, 'Привет, красотка! Ты готова посвятить время себе любимой? ', reply_markup=markup)

@bot.message_handler(commands=['notnow'])
def notnow(message):
    notnow = 'Надеюсь, Вы скоро вернетесь ко мне и мы приступим улучшать вашу кожу.'
    bot.send_message(message.chat.id, notnow)

@bot.message_handler(commands=['go'])
def go(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    day_1 = types.KeyboardButton('Первый день')
    day_2 = types.KeyboardButton('Второй день')
    day_3 = types.KeyboardButton('Третий день')
    day_4 = types.KeyboardButton('Четвертый день')
    day_5 = types.KeyboardButton('Пятый день')
    day_6 = types.KeyboardButton('Шестой день')
    day_7 = types.KeyboardButton('Седьмой день')
    more = types.KeyboardButton('/start')
    markup.add(day_1, day_2, day_3, day_4, day_5, day_6, day_7, more)
    bot.send_message(message.chat.id, 'Нажмите на кнопку, которая соответствует дню вашей программы по уходу за кожей', reply_markup=markup)

instr1 = 'Поздравляю, ведь самое трудное - это НАЧАТЬ. Завтра выберите следующий день.'
instr2 = 'Вы прекрасно справляетесь, с каждым днем ваша кожа становится более здоровой.'
instr3 = 'Ох уж эти прекрасные ощущения чистоты и свежести на коже. До завтра.'
instr4 = 'Половина пути пройдена, вы умница.'
instr5 = 'Если бы кожа могла говорить, она бы сказала: "БЛАГОДАРЮ"!'
instr6 = 'Надеюсь, вы будете повторять все действия и в дальнейшем.Завтра выберете следующий день.'
instr7 = 'Последний день вместе, так не хочется прощаться. До новых встреч!'
#instr8 = 'Как здорово, попробуй еще раз'


@bot.message_handler()
def days(message):
    if message.text == 'Первый день':
        photo = open('1.PNG', 'rb')
        bot.send_photo(message.chat.id, photo)
        photo1 = open('t1.PNG', 'rb')
        bot.send_photo(message.chat.id, photo1)
        bot.send_message(message.chat.id, instr1)
    if message.text == 'Второй день':
        photo = open('2.PNG', 'rb')
        bot.send_photo(message.chat.id, photo)
        photo1 = open('t2.PNG', 'rb')
        bot.send_photo(message.chat.id, photo1)
        bot.send_message(message.chat.id, instr2)
    if message.text == 'Третий день':
        photo = open('3.PNG', 'rb')
        bot.send_photo(message.chat.id, photo)
        photo1 = open('t3.PNG', 'rb')
        bot.send_photo(message.chat.id, photo1)
        bot.send_message(message.chat.id, instr3)
    if message.text == 'Четвертый день':
        photo = open('4.PNG', 'rb')
        bot.send_photo(message.chat.id, photo)
        photo1 = open('t4.PNG', 'rb')
        bot.send_photo(message.chat.id, photo1)
        bot.send_message(message.chat.id, instr4)
    if message.text == 'Пятый день':
        photo = open('5.PNG', 'rb')
        bot.send_photo(message.chat.id, photo)
        photo1 = open('t5.PNG', 'rb')
        bot.send_photo(message.chat.id, photo1)
        bot.send_message(message.chat.id, instr5)
    if message.text == 'Шестой день':
        photo = open('6.PNG', 'rb')
        bot.send_photo(message.chat.id, photo)
        photo1 = open('t6.PNG', 'rb')
        bot.send_photo(message.chat.id, photo1)
        bot.send_message(message.chat.id, instr6)
    if message.text == 'Седьмой день':
        photo = open('7.PNG', 'rb')
        bot.send_photo(message.chat.id, photo)
        photo1 = open('t7.PNG', 'rb')
        bot.send_photo(message.chat.id, photo1)
        bot.send_message(message.chat.id, instr7)
    #if message.text == 'Еще раз':
    #    bot.send_message(message.chat.id, instr8)


    elif message.text == '/help':
        bot.send_message(message.chat.id, 'Бот поможет сделать ритуалы красоты.'
                                              'Введи название дня: Первый день, Второй день, Третий день, Четвертый день, Пятый день, Шестой день, Седьмой день')


bot.polling(none_stop=True)