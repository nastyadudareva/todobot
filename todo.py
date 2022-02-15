import telebot
import random

token = "5109638445:AAE4bL7yvInnF4xy_zbkjdqXFLO-P_NL_jg"

bot = telebot.TeleBot(token)

HELP = """
/help - напечатать справку по программе.
/add - добавить задачу в список на опредленную дату (введите задачу в формате "/add XX.XX задача").
/show - напечатать все добавленные задачи (введите дату в формате "/show дата").
/random - добавить случайную задачу на дату Сегодня
/clean - удалить все задачи на выбранную дату"""

tasks = {}
random_tasks = ['Убраться дома', 'Приготовить что-нибудь вкусненькое', 'Почитать книгу', 'Посмотреть сериал', 'Начать учить что-то новое', 'Заняться йогой', 'Медитация']

def add_to_do(date, task):
    if date in tasks:
      tasks[date].append(task)
    else:
        tasks[date] = []
        tasks[date].append(task)

@bot.message_handler(commands=["add"])
def add(message):
    command = message.text.split(maxsplit=2)
    date = command[1].lower().capitalize()
    task = command[2].lower().capitalize()
    add_to_do(date, task)
    text = "Задача " + task + " добавлена на дату " + date
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["random"])
def random_add(message):
    date = "сегодня".lower().capitalize()
    task = random.choice(random_tasks)
    add_to_do("Сегодня", task)
    text = "Задача " + task + " добавлена на дату " + date
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["clean"])
def clean(message):
    command = message.text.split(maxsplit=2)
    date = command[1].lower().capitalize()
    text = ""
    if date in tasks:
        del tasks[date]
        text = "Задачи на дату " + date + " удалены"
    else:
        text = "Задач на эту дату нет"
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["show"])
def show(message):
    command = message.text.split(maxsplit=2)
    date = command[1].lower().capitalize()
    text = ""
    if date in tasks:
        text = date + "\n"
        for task in tasks[date]:
            text = text + "-- " + task + "\n"
    else:
        text = "Задач на эту дату нет"
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, HELP)

bot.polling(none_stop=True)