import telebot


token = "5109638445:AAE4bL7yvInnF4xy_zbkjdqXFLO-P_NL_jg"

bot = telebot.TeleBot(token)

HELP = """
/help - напечатать справку по программе.
/add - добавить задачу в список на определенную дату (введите команду в формате "/add XX.XX задача").
/show - напечатать все добавленные задачи (введите команду в формате "/show дата").
/clean - удалить все задачи на выбранную дату (введите команду в формате "/clean дата")"""

tasks = {}
random_tasks = ['Убраться дома', 'Приготовить что-нибудь вкусненькое', 'Почитать книгу', 'Посмотреть сериал', 'Начать учить что-то новое', 'Заняться йогой', 'Медитация']

def add_to_do(day, task):
    if day in tasks:
      tasks[day].append(task)
    else:
        tasks[day] = []
        tasks[day].append(task)


@bot.message_handler(commands=["add"])
def add(message):
    command = message.text.split(maxsplit=2)
    day = command[1].upper()
    task = command[2].lower().capitalize()
    add_to_do(day, task)
    text = "Задача " + task + " добавлена на дату " + day
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["clean"])
def clean(message):
    command = message.text.split(maxsplit=2)
    day = command[1].upper()
    text = ""
    if day in tasks:
        del tasks[day]
        text = "Задачи на дату " + day + " удалены"
    else:
        text = "Задач на эту дату нет"
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["show"])
def show(message):
    command = message.text.split(maxsplit=2)
    day = command[1].upper()
    text = ""
    if day in tasks:
        text = day + "\n"
        for task in tasks[day]:
            text = text + "-- " + task + "\n"
    else:
        text = "Задач на эту дату нет"
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, HELP)

bot.polling(none_stop=True)