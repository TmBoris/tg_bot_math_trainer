import telebot
from telebot import types
import random
import secret
import my_math
import asyncio

RUSSIAN = 1
ENGLISH = 2
bot = telebot.TeleBot(secret.token)
dct = {"": []}
language = RUSSIAN
WAITING_FOR_TASK = False
WAITING_FOR_NAME = False
ADD = False
REMOVE = False
Name = ""

math_tasks = my_math.math_tasks
answers = my_math.answers

def GetWeather():
    t = random.randint(-30, 35)
    return t


def AddTask(name, task):
    if name not in dct:
        dct[name] = []
    dct[name].append(task)


def GetTasks(name):
    if name not in dct:
        return ["Dobby is free today"]
    return dct[name]


def ArhiveTask(name, num):
    num = int(num) - 1
    if name in dct:
        if num < len(dct[name]):
            dct[name].remove(dct[name][num])


def GetMathTask():
    t = random.randint(0, len(answers) - 1)
    return math_tasks[t], answers[t]


def RusElse(message, arg):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Погода")
    btn2 = types.KeyboardButton('Добавить задачу')
    btn3 = types.KeyboardButton("Узнать дела на сегодня")
    btn4 = types.KeyboardButton("Задача сделана")
    btn5 = types.KeyboardButton("Когда уже релаксить?!")
    btn6 = types.KeyboardButton("Хочу таску")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
    bot.send_message(message.from_user.id, arg, reply_markup=markup)


def EngElse(message, arg):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Weather")
    btn2 = types.KeyboardButton('Add task')
    btn3 = types.KeyboardButton("tasklist")
    btn4 = types.KeyboardButton("mark the task is done")
    btn5 = types.KeyboardButton("Next chill day?")
    markup.add(btn1, btn2, btn3, btn4, btn5)
    bot.send_message(message.from_user.id, arg, reply_markup=markup)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🇷🇺 Русский")
    btn2 = types.KeyboardButton('🇬🇧 English')
    markup.add(btn1, btn2)
    bot.send_message(message.from_user.id, "🇷🇺 Выберите язык / 🇬🇧 Choose your language", reply_markup=markup)


@bot.message_handler(content_types=['text', 'document', 'audio'])
def get_text_messages(message):
    global WAITING_FOR_TASK
    global Name
    global language
    global WAITING_FOR_NAME
    global ADD
    global REMOVE
    if message.text == "🇷🇺 Русский":
        language = RUSSIAN
        WAITING_FOR_NAME = True
        bot.send_message(message.from_user.id, "Как тебя зовут?")
    elif message.text == "🇬🇧 English":
        language = ENGLISH
        WAITING_FOR_NAME = True
        bot.send_message(message.from_user.id, "What's your name?")
    elif WAITING_FOR_TASK:
        if ADD:
            AddTask(Name, message.text)
            ADD = False
        if REMOVE:
            ArhiveTask(Name, message.text)
            REMOVE = False
        WAITING_FOR_TASK = False
        if language == RUSSIAN:
            RusElse(message, "Еще что-нибудь интересует?")
        else:
            EngElse(message, "Anything else?")
    elif WAITING_FOR_NAME:
        Name = message.text
        WAITING_FOR_NAME = False
        if language == RUSSIAN:
            ans = "Ура ура, привет " + str(Name) + "! На данный момент ты можешь\n" \
                                                   "1) Узнать температуру за окном\n" \
                                                   "2) Добавить задачу в список\n" \
                                                   "3) Узнать какие дела запланированны на сегодня\n" \
                                                   "4) Внести пометку, что задача сделана" \
                                                   "4) Узнать когда ближайший выходной\n" \
                                                   "5) Попросить интересную задачку по математике"
            bot.send_message(message.from_user.id, ans)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Погода")
            btn2 = types.KeyboardButton('Добавить задачу')
            btn3 = types.KeyboardButton("Узнать дела на сегодня")
            btn4 = types.KeyboardButton("Задача сделана")
            btn5 = types.KeyboardButton("Когда уже релаксить?!")
            btn6 = types.KeyboardButton("Хочу таску")
            markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
            bot.send_message(message.from_user.id, "Чем займемся?", reply_markup=markup)
        else:
            ans = "Hello," + str(Name) + " ! Now you can\n" \
                                         "1) Ask me about outside weather\n" \
                                         "2) Add a task to your list of tasks\n" \
                                         "3) Ask me about your plans\n" \
                                         "4) Mark that the task is done\n" \
                                         "5) Ask me about next day off"
            bot.send_message(message.from_user.id, ans)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Weather")
            btn2 = types.KeyboardButton('Add task')
            btn3 = types.KeyboardButton("tasklist")
            btn4 = types.KeyboardButton("mark the task is done")
            btn5 = types.KeyboardButton("Next chill day?")
            markup.add(btn1, btn2, btn3, btn4, btn5)
            bot.send_message(message.from_user.id, "So?", reply_markup=markup)

    elif message.text == "Погода" or message.text == "Weather":
        temp = GetWeather()
        if language == RUSSIAN:
            ans = "Температура за окном " + str(temp) + " градусов Цельсия"
            bot.send_message(message.from_user.id, ans)
            RusElse(message, "Еще что-нибудь интересует?")
        else:
            ans = "The temperature outside the window is " + str(temp) + " degrees Celsius"
            bot.send_message(message.from_user.id, ans)
            EngElse(message, "Anything else?")
    elif message.text == "Добавить задачу" or message.text == "Add task":
        WAITING_FOR_TASK = True
        ADD = True
        if language == RUSSIAN:
            bot.send_message(message.from_user.id, "Давай задачу")
        else:
            bot.send_message(message.from_user.id, "Give me your task")
    elif message.text == "Узнать дела на сегодня" or message.text == "tasklist":
        arr = GetTasks(Name)
        if language == RUSSIAN:
            ans = "Список задач: \n"
            for i, task in enumerate(arr):
                ans += str(i + 1) + ") " + task + "\n"
            bot.send_message(message.from_user.id, ans)
            RusElse(message, "Еще что-нибудь интересует?")
        else:
            ans = "Tasks: \n"
            for i, task in enumerate(arr):
                ans += str(i + 1) + ") " + task + "\n"
            bot.send_message(message.from_user.id, ans)
            EngElse(message, "Anything else?")
    elif message.text == "Задача сделана" or message.text == "mark the task is done":
        WAITING_FOR_TASK = True
        REMOVE = True
        if language == RUSSIAN:
            bot.send_message(message.from_user.id, "Какую?(номер)")
        else:
            bot.send_message(message.from_user.id, "Which one?(number)")
    elif message.text == "Когда уже релаксить?!" or message.text == "Next chill day?":
        if language == RUSSIAN:
            bot.send_message(message.from_user.id, "Кризис в стране, фигачить нужно, а не отдыхать!")
            RusElse(message, "Еще что-нибудь интересует?")
        else:
            bot.send_message(message.from_user.id, "Never maaaan, you have to do your best every fucking day!")
            EngElse(message, "Anything else?")
    elif message.text == "Хочу таску":
        math_task, answer = GetMathTask()
        bot.send_message(message.from_user.id, math_task)
        answer = "||" + answer + "||"
        bot.send_message(message.from_user.id, answer, parse_mode='MarkdownV2')
    elif message.text == "/help":
        if language == RUSSIAN:
            bot.send_message(message.from_user.id, "Как жаль, что ты опять забыл мой функционал. Ну ничего вот "
                                                   "напоминалка:")
            RusElse(message, "Выбирай")
        else:
            bot.send_message(message.from_user.id, "Uh, you forget how to use my bot, here you can see possible "
                                                   "options: ")
            EngElse(message, "Choose")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.\n"
                                               "I don't understand you. Write /help.")


bot.polling(none_stop=True, interval=0)
