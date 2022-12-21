import telebot
from telebot import types
import random
import asyncio

RUSSIAN = 1
ENGLISH = 2
bot = telebot.TeleBot('5869415038:AAHiHZVEmJYjXRsCLwYBYL_Wsc9Qc3WuMnc')
dct = {"": []}
language = RUSSIAN
WAITING_FOR_TASK = False
WAITING_FOR_NAME = False
ADD = False
REMOVE = False
Name = ""

math_tasks = ["Зайцы пилят бревно. Они сделали 10 распилов. Сколько получилось чурбачков?",
              "У каждого марсианина три руки. Могут ли семь марсиан взяться за руки?",
              'Когда "послезавтра" станет "вчера", то "сегодня" будет так же далеко от воскресенья, как тот день, '
              'который был "сегодня", когда "вчера" было "завтра". Как вы думаете, какой сегодня день недели?',
              "Гена пошёл с папой в тир. Договорились, что Гена делает 5 выстрелов и за каждое попадание в цель "
              "получает право сделать ещё 2 выстрела. Всего Гена сделал 17 выстрелов. Сколько раз он попал в цель?",
              "Напишите в строчку первые 10 простых чисел. Как вычеркнуть 6 цифр, чтобы получилось наибольшее "
              "возможное число?",
              "Найдите двузначное число, которое в 5 раз больше суммы своих цифр.",
              "Десять человек захотели основать клуб. Для этого им необходимо собрать определённую сумму "
              "вступительных взносов. Если бы организаторов было на пять человек больше, то каждый из них должен был "
              "бы внести на 100 долларов меньше. Сколько денег внёс каждый?",
              "Куб со стороной 1 м распилили на кубики со стороной 1 см и положили их в ряд (по прямой). Какой длины "
              "оказался ряд?",
              "Можно ли доску размером 5×5 заполнить доминошками размером 1×2?",
              "В турнире участвовали шесть шахматистов. Каждые два участника турнира сыграли между собой по одной "
              "партии. Сколько всего было сыграно партий? Сколько партий сыграл каждый участник? Сколько очков набрали "
              "шахматисты все вместе?",
              "У учеников 5А класса было в сумме 2015 карандашей. Один из них потерял коробку с пятью карандашами, "
              "а вместо неё купил коробку, в которой 50 карандашей. Сколько теперь карандашей у учеников 5А класса?",
              "Между каждой из цифр 5 4 3 2 1 поставь знаки действий и скобки так, чтобы получился 0.",
              "Если синий карандаш толще красного, а красный толще голубого, то какой карандаш толще: голубой или "
              "синий?",
              "Одно яйцо варится 4 минуты. Сколько минут варится 5 яиц?",
              "На руках 10 пальцев. Сколько пальцев на 10 руках?",
              "Врач дал больной девочке 3 таблетки и велел принимать их через каждые полчаса. Она строго выполнила "
              "указание врача. На сколько времени хватило прописанных врачомтаблеток?",
              "Из куска проволоки согнули квадрат со стороной 6см. Затем разогнули проволоку, и согнули из неё "
              "треугольник с равными сторонами. Какова длина стороны треугольника?",
              "Коля, Вася и Боря играли в шашки. Каждый из них сыграл всего 2 партии. Сколько всего партий было "
              "сыграно?",
              "Сколько всего двузначных чисел можно составить из цифр 1,2,3 при условии, что цифры в записи числа "
              "повторяться не будут? Перечисли все эти числа.",
              "Было 9 листов бумаги. Некоторые из них разрезали на три части. Всего стало 15 листов. Сколько листов "
              "бумаги разрезали?",
              "В пятиэтажном доме Вера живёт выше Пети, но ниже Славы, а Коля живёт ниже Пети. На каком этаже живёт "
              "Вера, если Коля живёт на втором этаже?",
              "1 резинка, 2 карандаша и 3 блокнота стоят 38 руб. 3 резинки, 2 карандаша и 1 блокнот стоят 22 руб. "
              "Сколько стоит комплект из резинки, карандаша и блокнота?",
              "Нильс летел в стае на спине гуся Мартина. Он обратил внимание, что построение стаи напоминает "
              "треугольник: впереди вожак, затем 2 гуся, в третьем ряду 3 гуся и т.д. Стая остановилась на ночлег на "
              "льдине. Нильс увидел, что расположение гусей на этот раз, напоминает квадрат, состоящий из рядов, "
              "в каждом ряду одинаковое количество гусей, причём число гусей в каждом ряду равно числу рядов. Гусей в "
              "стае меньше 50. Сколько гусей в стае? "
              ]
answers = ["11 чурбачков",
           "Всего рук 21 – нечётное число\. Если бы они взялись за руки, то руки разбились бы на пары \(в каждую пару "
           "входят две пожимающие друг друга руки\), а это невозможно",
           "Среда",
           "6 раз",
           "Получится число 7317192329",
           "45",
           "300 долларов",
           "Получим 100 × 100 × 100 \= 1000000 \(см\) или 10000 м \= 10 км",
           "Общее количество клеток \(25\) не делится на 2\, а каждая доминошка покрывает две клетки",
           "15 партий\; 5 партий\; 15 очков",
           "2015 – 5 \+ 50 \= 2060",
           "На этот раз придется все сделать самому \:\)",
           "Синий",
           "4 минуты",
           "50",
           "на 1 час",
           "8см",
           "3 партии\. \(К\-В, К\-Б, В\-Б\)",
           "12\,13\, 21\,23\, 31\,32",
           "3 листа",
           "4 этаж",
           "15 руб\.\, т\.к\. 4 резинки\, 4 карандаша и 4 блокнота 38\+22\=60\(руб\.\) Один комплект стоит 60\: 4\=15\(руб\.\)",
           "36 гусей"
           ]


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
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.\n"
                                               "I don't understand you. Write /help.")


bot.polling(none_stop=True, interval=0)
