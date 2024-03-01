from customtkinter import *
import matplotlib.pyplot as plt
import math, json, random, numpy as np, os
from datetime import datetime
from PIL import Image

import tkinter as tk
import tkinterDnD
from tkinter import filedialog

os.system('cls')

#image:path`s

iconPath = 'res\\icons\\dodecahedron.ico'
dndLight = 'res\\icons\\dndLight.png'
dndDark  = 'res\\icons\\dndDark.png'

#constants:
friendTasks = False
Theme = get_appearance_mode()

set_default_color_theme = 'blue'

Language = "RUS"
testing = False
Difficult = ["Easy", "Peaceful", "Normal", "Hard", "HARDCORE", "MIND"]
taskPause = False
TimeClock = 0
taskcount = 0
realTaskPosition = 0
correctTaskCount = 0
Score = 0
answStatus = ''
Question = ''
AllTasks = ''
result = ''
filename = 'DefaultTask'

minute = 15
seconds = 00

################################################

def start():
    global app
    app=CTk()
    try:
        app.iconbitmap(iconPath)
    except:
        pass

    app.overrideredirect(False)
    app.title("Математическое тестирование | Версия: 2F02")
    app.geometry("900x600")
    app.minsize(900, 600)
    app.resizable(False,False)

    helloloop()
    app.mainloop()

def switch_Theme():
    global ThemeButton,Theme
    theme = "Light" if switch_var.get() == "on" else "Dark"
    if theme == "Light": set_appearance_mode("Dark"); Theme='Dark'
    else: set_appearance_mode("Light"); Theme='Light'

    ThemeButton.configure(text=Theme)


def helloloop():
    global panel_L,panel_R,Theme,ThemeButton,switch_var,DifficultVar,QuestionF
    global AllTasks,Score,taskcount,correctTaskCount,testing,realTaskPosition
    testing = False
    realTaskPosition = 1
    QuestionF = ''

    try:
        DragAndDropFrame.forget()
        downFrame.forget()
        backbutton.forget()
    except:
        pass

    try:
        LeftFrame.forget()
        RightFrame.forget()
    except:
        pass
    
    try:
        pLeftFrame.forget()
        pRightFrame.forget()
    except:
        pass

    try:
        upperFrame.forget()
        bottomFrame.forget()
        
        AllTasks = ''
        Score = 0
        taskcount = 0
        correctTaskCount = 0

    except:
        pass

    #LEFT FRAME
    panel_L = CTkFrame(app, height=600, width=550,corner_radius=10)
    panel_L.pack(side=LEFT,padx=10,pady=10)
    panel_L.pack_propagate(0)

    logoBG = CTkFrame(panel_L, height=70, width=550,corner_radius=10)
    logoBG.pack(side=TOP,padx=10,pady=10)
    logoBG.pack_propagate(0)

    logoLabel = CTkLabel(logoBG,text="MΔTH TΣSTΣR", font=('courier new',50))
    logoLabel.pack(padx=10,pady=10)

    TesterButton = CTkButton(panel_L, height=70, width=510,corner_radius=10,text="Начать тестирование",font=('courier new',20),
                             command=tester)
    TesterButton.pack(padx=10,pady=10)
    TesterButton.place(relx=0.5, rely=0.42,anchor='n')
    TesterButton.pack_propagate(0)
    
    CreateButton = CTkButton(panel_L, height=70, width=160,corner_radius=10,text="Создать билет",font=('courier new',20),command=createloop)
    CreateButton.pack(padx=10,pady=10)
    CreateButton.place(relx=0.36, rely=0.7,anchor='se')
    CreateButton.pack_propagate(0)

    GraphButton = CTkButton(panel_L, height=70, width=160,corner_radius=10,text=" Прорешать готовый билет ",font=('courier new',20),command=openTestFile)
    GraphButton.pack(padx=10,pady=10)
    GraphButton.place(relx=0.38, rely=0.7,anchor='sw')
    GraphButton.pack_propagate(0)

    versionLabel = CTkLabel(panel_L,text='Version: 2F02 | Created by @slide36',font=('Courier new',12))
    versionLabel.pack(side=BOTTOM)
    #RIGTH FRAME
    panel_R = CTkFrame(app, height=600, width=350,corner_radius=10)
    panel_R.pack(side=LEFT,padx=10,pady=10)
    panel_R.pack_propagate(0)

    infoDock = CTkFrame(panel_R, height=70, width=350,corner_radius=10)
    infoDock.pack(padx=10,pady=10)
    infoDock.pack_propagate(0)

    infoLabel = CTkLabel(infoDock,text="НАСТРОЙКИ",font=('courier new',50))
    infoLabel.pack(padx=10,pady=10)

    ThemeDock =  CTkFrame(panel_R, height=70, width=350,corner_radius=10)
    ThemeDock.pack(padx=10,pady=10)
    ThemeDock.pack_propagate(0)

    ThemeLabel = CTkLabel(ThemeDock, text="Выбранная тема:", font=('consolas',12))
    ThemeLabel.pack(padx=20,side=LEFT)

    switch_var = StringVar(value="on")
    ThemeButton = CTkSwitch(ThemeDock, text=Theme, command=switch_Theme,
                                 variable=switch_var, onvalue="on", offvalue="off", font=('consolas',12))
    ThemeButton.pack(padx=20,side=RIGHT)

    DifficultDock = CTkFrame(panel_R, height=70, width=350,corner_radius=10)
    DifficultDock.pack(padx=10,pady=10)
    DifficultDock.pack_propagate(0)

    DifficultLabel = CTkLabel(DifficultDock, text="Сложность:", font=('consolas', 12))
    DifficultLabel.pack(padx=20, side=LEFT)

    DifficultVar = StringVar(value=Difficult)
    def optionmenu_callback(choice):
        DifficultVar.set(choice)

    DifficultVar.set("Easy")

    DifficultButton = CTkOptionMenu(DifficultDock, width=120, font=('consolas', 12), values=["Easy", "Peaceful", "Normal", "Hard"],#, "HARDCORE", "MIND"],
                                            command=optionmenu_callback, variable=DifficultVar)
    DifficultButton.pack(padx=20, side=RIGHT)


    SinfoDock = CTkFrame(panel_R, height=70, width=350,corner_radius=10)
    SinfoDock.pack(padx=10,pady=10)
    SinfoDock.pack_propagate(0)

    SinfoLabel = CTkLabel(SinfoDock,text="ОГРАНИЧЕНИЯ",font=('courier new',36))
    SinfoLabel.pack(padx=10,pady=24)
    

    def timePlus():
        global minute,seconds

        minute,seconds=int(minute),int(seconds)

        TimeDisplay.delete(0, 'end')
        seconds+=15

        if (seconds>= 60):
            minute += 1
            seconds = 0
        if (minute > 99):
            minute = 5
            seconds = 0

        TimeDisplay.insert('end',"{minute:02}:{seconds:02}m".format(minute=minute, seconds=seconds))

        pass

    def timeMinus():
        global minute,seconds

        minute,seconds=int(minute),int(seconds)

        TimeDisplay.delete(0, 'end')
        seconds-=15

        if seconds < 0:
            seconds = 45
            minute = minute - 1
        if minute < 5:
            seconds = 0
            minute = 99

        TimeDisplay.insert('end',"{minute:02}:{seconds:02}m".format(minute=minute, seconds=seconds))

        pass

    TestTiming = CTkFrame(panel_R,width=350,height=70)
    TestTiming.pack(padx=10,pady=10)
    TestTiming.pack_propagate(0)

    TimeLabel = CTkLabel(TestTiming, text='Длительность:',font=('consolas', 12))
    TimeLabel.pack(padx=20, side=LEFT)

    TimePlus = CTkButton(TestTiming, width=30, text='+',command=timePlus)
    TimePlus.pack()
    TimePlus.place(relx=0.83,rely=0.3)

    TimeMinus = CTkButton(TestTiming, width=30, text='-',command=timeMinus)
    TimeMinus.pack()
    TimeMinus.place(relx=0.72,rely=0.3)
    
    TimeDisplay = CTkEntry(TestTiming, width=60,placeholder_text='15:00m')
    TimeDisplay.pack()
    TimeDisplay.place(relx=0.50,rely=0.3)

    TimeDisplay.insert('end',"{minute:02}:{seconds:02}m".format(minute=minute, seconds=seconds))
def timeloop():
    global testing, minute, seconds, TimeClock

    minut = minute
    second = seconds

    if testing:
        if minut == 0 and second == 0:
            endTasks()
        else:
            if second == 0:
                minut -= 1
                second = 59
            else:
                second -= 1
            
            TimeClock = f'До конца testOирования:\n{minut:02}:{second:02}\n! Время идёт !'
            app.after(1000, timeloop)  # Вызываем функцию снова через 1 секунду
def tester():
    global Score,Question,TimeClock,LeftFrame,RightFrame,QuestionLabel, answerInput,scoreLabel, taskcount, _result, correctTaskCount
    global taskPause,timerClock,testing, minute, seconds
    testing = True
    taskPause = False

    timeloop()
    taskcount = 0
    correctTaskCount = 0
    _result = 0

    panel_L.forget()
    panel_R.forget()

    LeftFrame = CTkFrame(app, height=600, width=600,corner_radius=10)
    LeftFrame.pack(side=LEFT,padx=10,pady=10)
    LeftFrame.pack_propagate(0)

    missionFrame = CTkFrame(LeftFrame, height=200, width=650,corner_radius=10)
    missionFrame.pack(padx=10,pady=10)
    missionFrame.pack_propagate(0)
    
    QuestionLabel = CTkLabel(missionFrame, height=200, width=650,corner_radius=10,text='', font=('consolas',20))
    QuestionLabel.pack(padx=10,pady=10)
    QuestionLabel.pack_propagate(0)

    generateQuestion()
    answerFrame = CTkFrame(LeftFrame, height=60, width=650,corner_radius=10)
    answerFrame.pack(padx=10,pady=10)
    answerFrame.pack_propagate(0)

    answerInput = CTkEntry(answerFrame, height=60, width=450,placeholder_text="Введите ответ...")
    answerInput.pack(padx=10,pady=10,side=LEFT)

    sendAnswerButton = CTkButton(answerFrame, text='Ответить',height=60,width=90, font=('consolas',12),command=checkAnswer)
    sendAnswerButton.pack(padx=10,pady=10,side=RIGHT)

    RightFrame = CTkFrame(app, height=600, width=300,corner_radius=10)
    RightFrame.pack(side=LEFT,padx=10,pady=10)
    RightFrame.pack_propagate(0)

    timerFrame = CTkFrame(RightFrame, height=200, width=300,corner_radius=10)
    timerFrame.pack(padx=10,pady=10)
    timerFrame.pack_propagate(0)

    timerClock = CTkLabel(timerFrame, height=200, width=300,corner_radius=10, text=TimeClock, font=('consolas',12))
    timerClock.pack(padx=10,pady=10)
    timerClock.pack_propagate(0)

    scoreFrame = CTkFrame(RightFrame, height=60, width=300,corner_radius=10)
    scoreFrame.pack(padx=10,pady=10)
    scoreFrame.pack_propagate(0)

    scoreLabel = CTkLabel(scoreFrame, text="Score: {}".format(Score), height=100, width=300,corner_radius=10, font=('consolas',12))
    scoreLabel.pack(padx=10,pady=10)
    scoreLabel.pack_propagate(0)

    bottomFrame = CTkFrame(RightFrame,height=80, width=330,corner_radius=10)
    bottomFrame.pack(padx=10,pady=10,side=BOTTOM)
    bottomFrame.pack_propagate(0)

    exitBeforeTimer = CTkButton(bottomFrame, height=60, width=100, corner_radius=10, text='Завершить\nдосрочно', font=('consolas',12), command=endTasks)
    exitBeforeTimer.pack(padx=10,pady=10,side=LEFT)

    backButton = CTkButton(bottomFrame, height=60, width=100, corner_radius=10, text='Назад', font=('consolas',12), command=helloloop)
    backButton.pack(padx=10,pady=10,side=LEFT)
def generateQuestion():
    global correctAnswer, answerInput, AllTasks, Question, taskcount
    try:
        answerInput.delete(0, 'end')
    except:
        pass

    line = ''

    correctAnswer = 0
    Diff = DifficultVar.get()

    numbMax = 4
    numb = 4

    expo = random.randint(-5, 5)

    if Diff == 'Easy':
        numbMin = -5
        numbMax = 20
        numbers = list(range(int(numbMin), int(numbMax) + 1))

    elif Diff == 'Peaceful':
        numbMin = -5
        numbMax = 40
        numbers = list(range(int(numbMin), int(numbMax) + 1))

    elif Diff == 'Normal':
        numbMin = -50.0
        numbMax = 499.9
        numbers = [round(numbMin + 0.5 * i, 2) for i in range(int((numbMax - numbMin) / 0.5) + 1)]

    elif Diff == 'Hard':
        numbMin = -50.00
        numbMax = 999.99
        numbers = [round(numbMin + 0.05 * i, 2) for i in range(int((numbMax - numbMin) / 0.05) + 1)]


    operators = ['+', '-', '*', '/']#, '√']

    num_numbers = random.randint(2, numb)
    num_operators = num_numbers - 1

    prev_operator = ''
    for i in range(num_numbers + num_operators):
        if i % 2 == 0:
            line += str(random.choice(numbers))
        else:
            operator = random.choice(operators)
            if operator == '√' and prev_operator == '^{}'.format(expo):
                operator = random.choice(['+', '-', '*', '/'])
            line += ' ' + operator + ' '
            prev_operator = operator

    if '√' in line:
        line = line.replace('√', '√(') + ')'
    elif '^{}'.format(expo) in line:
        line = line.replace('^{}'.format(expo), '(' + str(expo) + ')')

    if '√' in line:
        number_to_sqrt = int(line.split('√')[1].strip('()'))  # Получаем число из корня
        line = 'math.sqrt({})'.format(number_to_sqrt)
    else:
        evoline = line

    try:
        correctAnswer = round(eval(evoline),2)
        print(correctAnswer)
        if not taskPause:
            taskcount+=1
    except ZeroDivisionError:
        # Обработка деления на ноль, если оно случится
        generateQuestion()

    Task = 'Задача #{}\n\n'.format(taskcount)
    
    line += '='

    Question = Task+line
    QuestionLabel.configure(text=Question)
def checkAnswer():
    global Score, AllTasks, correctTaskCount

    if answerInput.get() == '':
        my_answ = -9999999996
        

    else: 
        my_answ = float(answerInput.get())
        print(my_answ)
    if my_answ == float(correctAnswer):
        answStatus = 'Верно'
        Score+=1;correctTaskCount += 1
    else:
        answStatus = 'Неверно'



    scoreLabel.configure(text="Score: {}".format(Score))
    AllTasks += '{}: {}\n----------------------\n'.format(Question,answStatus)
    
    generateQuestion()
def endTasks():
    global upperFrame, bottomFrame, _result,saveButton
    global Score, AllTasks, correctTaskCount, taskPause,testing,friendTasks
    _result = 0
    testing = False
    taskPause = True

    
    if friendTasks == True:
        AnswerTest()
    else:
        checkAnswer()
    
    if taskcount >=10:
        _result = (correctTaskCount/taskcount)


        if _result <= 0.2:
            message = random.choice([
                "Ваш результат очень низкий. \nРекомендуем потренироваться еще немного! 📚",
                "Уровень вашей математики очень низкий. \nПочитайте математическую литературу для улучшения знаний. 📖",
                "Вам нужно больше практики. \nСосредоточьтесь на основах математики, \nчтобы улучшить результаты. 💪"
            ])
        elif 0.2 < _result <= 0.4:
            message = random.choice([
                "Продолжайте работать над собой. \nПрактика поможет вам улучшить результаты. 🏋️‍♂️",
                "Ваши результаты могут быть лучше. \nПостарайтесь больше времени уделять учебе. 🤓",
                "Не теряйте мотивацию. С постоянными тренировками \nвы достигнете желаемых результатов. 💡"
            ])
        elif 0.4 < _result <= 0.6:
            message = random.choice([
                "Вы на верном пути, однако есть место для улучшений. \nНе останавливайтесь! 🚀",
                "У вас есть потенциал для роста. \nПродолжайте работать над собой и учиться. 💪",
                "Не ограничивайте себя. \nСтремитесь к большему и у вас все получится! 🎯"
            ])
        elif 0.6 < _result <= 0.8:
            message = random.choice([
                "Ваши результаты хороши, но есть место для совершенствования. \nНе останавливайтесь на достигнутом! 🌟",
                "Отличная работа! Продолжайте в том же духе \nи вы достигнете новых высот. 👍",
                "Вы уже добились многого, но не забывайте, \nчто всегда есть возможность стать еще лучше. 🚀"
            ])
        elif 0.8 < _result <= 0.9:
            message = random.choice([
                "Ваши результаты впечатляют! \nПродолжайте двигаться квершинам! 🚀",
                "Вы близки к отличным результатам! \nПродолжайте в том же духе! 💪",
                "Ваш успех близок! Продолжайте так же \nстарательно работать, чтобы достичь своих целей! 🌟"
            ])
        elif 0.9 < _result <= 1.0:
            message = random.choice([
                "Поздравляем с отличными результатами! Вы молодец! 🎉",
                "Прекрасно справляетесь! Так держать! 💪",
                "Вы на вершине успеха! Продолжайте в том же духе! 🌟"
            ])


        result = 'Краткая статистика: \nВерно выполненых задач: {} из {}\nПроцентное соотношение: {}\n\n{}'.format(correctTaskCount,taskcount,_result,message)
    
    else:
        result = 'Вы выполнили меньше 10 задач, \nмы не можем предоставить достоверную статистику'

    try:
        LeftFrame.forget()
        RightFrame.forget()
    except:
        pass
    
    upperFrame = CTkFrame(app,height=450,width=900)
    upperFrame.pack(padx=10,pady=10,side=TOP)
    upperFrame.pack_propagate(0)

    upLeftFrame = CTkScrollableFrame(upperFrame, height=450, width=250, label_text="Пройденные задачи {}".format(taskcount))
    upLeftFrame.pack(padx=10,pady=10,side=LEFT)

    upLeftLabel = CTkLabel(upLeftFrame,width=250,font=('consolas',12),text=AllTasks)
    upLeftLabel.pack(padx=10,pady=10)

    upRightFrame = CTkFrame(upperFrame,height=450,width=650)
    upRightFrame.pack(padx=10,pady=10,side=RIGHT)
    upRightFrame.pack_propagate(0)

    upRtopLabel = CTkLabel(upRightFrame, text='Тестирование завершенно',height=20,width=650)
    upRtopLabel.pack(side=TOP,padx=10,pady=10)

    RightLabel = CTkLabel(upRightFrame,height=140,width=650,text=result,font=('consolas',16))
    RightLabel.pack(padx=10,pady=10)

    bottomFrame = CTkFrame(app,height=450,width=900)
    bottomFrame.pack(padx=10,pady=10,side=BOTTOM)
    bottomFrame.pack_propagate(0)

    leftBottomFrame = CTkFrame(bottomFrame,height=450,width=270)
    leftBottomFrame.pack(padx=10,pady=10,side=LEFT)
    leftBottomFrame.pack_propagate(0)

    saveButton = CTkButton(leftBottomFrame,height=450,width=270,text='Сохранить результат',font=('consolas',16),command=saveData)
    saveButton.pack(padx=8,pady=8)
    saveButton.pack_propagate(0)

    rigthBottomFrame = CTkFrame(bottomFrame,height=450,width=650)
    rigthBottomFrame.pack(padx=10,pady=10,side=RIGHT)
    rigthBottomFrame.pack_propagate(0)

    menuButtom = CTkButton(rigthBottomFrame,height=450,width=270,text='Вернуться в меню',font=('consolas',16),command=helloloop)
    menuButtom.pack(padx=8,pady=8,side=RIGHT)
    menuButtom.pack_propagate(0)

    shareButton = CTkButton(rigthBottomFrame,height=450,width=270,text='Отправить отчёт',font=('consolas',16),command='share')
    shareButton.pack(padx=8,pady=8,side=RIGHT)
    shareButton.pack_propagate(0)

    pass
def saveData():
    # Генерация даты и времени пользователя

    now = datetime.now()
    user_datetime = now.strftime("%d/%m/%Y, %H:%M:%S")

    # Загрузка существующих данных из файла, если они есть
    try:
        with open('result.json', 'r') as file:
            data = json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        data = {}

    # Добавление новых данных с пользовательской датой и временем в качестве ключа
    data[user_datetime] = {
        "Result": str('{}'.format(_result)),
        "Tasks": str('{}'.format(taskcount)),
        "CorrectAnswers": str('{}'.format(correctTaskCount))
    }

    # Сохранение обновленных данных в файл
    with open('result.json', 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    
    print('Данные сохранены в файл result.json')
    saveButton.configure(text='Данные успешно сохранены!',state=DISABLED)

def createloop():
    global Score,PositionQA,Label,QuestionLabel,answerInput,saveTaskName,LeftFrame,RightFrame,LabelLog,scoreLabel

    PositionQA = 1
    panel_L.forget()
    panel_R.forget()

    LeftFrame = CTkFrame(app, height=600, width=600,corner_radius=10)
    LeftFrame.pack(side=LEFT,padx=10,pady=10)
    LeftFrame.pack_propagate(0)

    missionFrame = CTkFrame(LeftFrame, height=200, width=650,corner_radius=10)
    missionFrame.pack(padx=10,pady=10)
    missionFrame.pack_propagate(0)
    
    QuestionLabel = CTkTextbox(missionFrame, height=200, width=650,
                             corner_radius=10,
                             font=('consolas',20),
                             wrap=WORD)
    
    QuestionLabel.pack(padx=10,pady=10)
    QuestionLabel.pack_propagate(0)

    answerFrame = CTkFrame(LeftFrame, height=60, width=650,corner_radius=10)
    answerFrame.pack(padx=10,pady=10)
    answerFrame.pack_propagate(0)

    answerInput = CTkEntry(answerFrame, height=60, width=370,placeholder_text="Введите ответ...")
    answerInput.pack(padx=10,pady=10,side=LEFT)

    sendAnswerButton = CTkButton(answerFrame, text='Сохранить и продолжить',height=60,width=180, font=('consolas',12),command=add_QA_in_test)
    sendAnswerButton.pack(padx=10,pady=10,side=RIGHT)

    leftBottom = CTkFrame(LeftFrame, height=60, width=600,corner_radius=10)
    leftBottom.pack(padx=10,pady=10,side=BOTTOM)
    leftBottom.propagate(0)

    LabelLog = CTkLabel(LeftFrame,height=300, width=600,corner_radius=10,text='Первый номер добавлен в стек!')
    LabelLog.pack(padx=10,pady=10)
    LabelLog.propagate(0)

    TaskName = CTkEntry(leftBottom, height=60, width=370,placeholder_text="Наименование теста...")
    TaskName.pack(padx=10,pady=10,side=LEFT)

    def saveFileName():
        global filename
        filename = TaskName.get()

        if filename == '':
            filename = 'DefaultTask'

        TaskName.configure(state=DISABLED)
        saveTaskName.configure(state=DISABLED)

    def back_to_previous_question():
        global PositionQA, filename

        # Уменьшаем позицию задания на 1
        PositionQA -= 1

        if PositionQA < 1:
            PositionQA = 1

        # Обновляем Label с номером задания
        Label.configure(text=PositionQA)

        # Загружаем данные о предыдущем вопросе и ответе из файла, если они доступны, и заполняем соответствующие поля
        try:
            with open('{}.json'.format(filename), 'r') as file:
                data = json.load(file)
                if str(PositionQA) in data:
                    current_data = data[str(PositionQA)]
                    QuestionLabel.delete('0.0', 'end')
                    QuestionLabel.insert('0.0', current_data["question"])
                    answerInput.delete(0, 'end')
                    answerInput.insert(0, current_data["answer"])

        except (FileNotFoundError, json.decoder.JSONDecodeError):
            # Обработка исключений в случае отсутствия файла или неправильного формата JSON
            pass
    def move_to_next_question():
        global Score, PositionQA, filename

        # Проверяем, что текущая realTaskPosition не превышает общее количество заданий
        if PositionQA < Score:
            # Увеличиваем позицию задания на 1
            PositionQA += 1

            # Обновляем Label с номером задания
            Label.configure(text=PositionQA)

            # Загружаем данные о следующем вопросе и ответе из файла, если они доступны, и заполняем соответствующие поля
            try:
                with open('{}.json'.format(filename), 'r') as file:
                    data = json.load(file)
                    if str(PositionQA) in data:
                        current_data = data[str(PositionQA)]
                        QuestionLabel.delete('0.0', 'end')
                        QuestionLabel.insert('0.0', current_data["question"])
                        answerInput.delete(0, 'end')
                        answerInput.insert(0, current_data["answer"])

            except (FileNotFoundError, json.decoder.JSONDecodeError):
                # Обработка исключений в случае отсутствия файла или неправильного формата JSON
                pass

    saveTaskName = CTkButton(leftBottom, text='Сохранить',height=60,width=180, font=('consolas',12),command=saveFileName)
    saveTaskName.pack(padx=10,pady=10,side=BOTTOM)

    RightFrame = CTkFrame(app, height=600, width=300,corner_radius=10)
    RightFrame.pack(side=LEFT,padx=10,pady=10)
    RightFrame.pack_propagate(0)

    NaBFrame = CTkFrame(RightFrame, height=200, width=300,corner_radius=10)
    NaBFrame.pack(padx=10,pady=10)
    NaBFrame.pack_propagate(0)

    BackButton = CTkButton(NaBFrame,width=80,height=200, corner_radius=10,text='<',command=back_to_previous_question)
    BackButton.pack(padx=10,pady=10, side=LEFT)
    BackButton.pack_propagate(0)

    Label = CTkLabel(NaBFrame,text=PositionQA)
    Label.pack()
    Label.place(relx=0.5,rely=0.5,anchor=CENTER)
    Label.pack_propagate(0)

    NextButton = CTkButton(NaBFrame,width=80,height=200, corner_radius=10,text='>',command=move_to_next_question)
    NextButton.pack(padx=10,pady=10,side=RIGHT)
    NextButton.pack_propagate(0)


    scoreFrame = CTkFrame(RightFrame, height=60, width=300,corner_radius=10)
    scoreFrame.pack(padx=10,pady=10)
    scoreFrame.pack_propagate(0)

    scoreLabel = CTkLabel(scoreFrame, text=f"Заданий всего: {Score}", height=100, width=300,corner_radius=10, font=('consolas',12))
    scoreLabel.pack(padx=10,pady=10)
    scoreLabel.pack_propagate(0)

    bottomFrame = CTkFrame(RightFrame,height=80, width=330,corner_radius=10)
    bottomFrame.pack(padx=10,pady=10,side=BOTTOM)
    bottomFrame.pack_propagate(0)

    exitBeforeTimer = CTkButton(bottomFrame, height=60, width=100, corner_radius=10, text='Завершить\nбилет', font=('consolas',12), command=saveAndOpen)
    exitBeforeTimer.pack(padx=10,pady=10,side=LEFT)

    backButton = CTkButton(bottomFrame, height=60, width=100, corner_radius=10, text='Меню', font=('consolas',12), command=helloloop)
    backButton.pack(padx=10,pady=10,side=LEFT)
def add_QA_in_test():
    global Score, PositionQA,filename

    # Создаем JSON файл для хранения вопросов и ответов
    data = {}

    # Определяем номер задания
    task_number = PositionQA

    # Получаем введенное условие задачи и ответ
    question = QuestionLabel.get('0.0','end')
    answer = answerInput.get()
    
    # Загрузка существующих данных из файла, если они есть
    try:
        with open('{}.json'.format(filename), 'r') as file:
            data = json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        data = {}

    # Добавляем вопрос и ответ в JSON данные
    data[task_number] = {
        "question": question,
        "answer": answer,
    }

    # Сохраняем JSON данные в файл
    with open(f'{filename}.json', 'w') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    # Увеличиваем позицию задания на 1
    PositionQA += 1
    Score+=1

    # Обновляем Label с номером задания
    scoreLabel.configure(text=f'Заданий всего: {Score}')
    Label.configure(text=PositionQA)

    # Сбрасываем текстовые поля для следующего вопроса и ответа
    QuestionLabel.delete('0.0','end')
    answerInput.delete(0,'end')

    # Если завершено создание всех заданий, можно выполнить какие-то действия (если нужно)

    # Пример проверки завершения создания всех заданий
    if PositionQA > Score:
        LabelLog.configure(text='\nЗадание {} добавленно в сток!'.format(PositionQA))
        print("Задание {} добавленно в сток!".format(PositionQA))
def saveAndOpen():
    try:
        os.system(f'start {filename}.json')
    except:
        pass
    helloloop()
    pass
def open_file_dialog(entry_widget):
    global realTaskPosition, filename
    realTaskPosition = 1

    file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
    entry_widget.delete(0, tk.END)
    entry_widget.insert(tk.END, file_path)
    openButton.configure(state=DISABLED)
    pathInput.configure(state=DISABLED)

    filename = os.path.relpath(file_path)
    app.after(100, friendTest)
def openTestFile():
    global DragAndDropFrame,downFrame,backbutton,pathInput,openButton

    try:
        DragAndDropFrame.forget()
        downFrame.forget()
        backbutton.forget()
        LeftFrame.forget()
        RightFrame.forget()

    except:
        panel_L.forget()
        panel_R.forget()

    DragAndDropFrame = CTkFrame(app, height=300, width=500)
    DragAndDropFrame.pack(padx=10, pady=50, side=TOP)
    DragAndDropFrame.pack_propagate(0)

    DADlabele = CTkLabel(DragAndDropFrame,height=70,width=128,
                        text='Укажите путь до файла \nили закиньте его в это поле.',
                        font=('consolas',16))
    DADlabele.pack(side=BOTTOM,pady=10)
    DADlabele.pack_propagate(0)

    try:
        DADimage = CTkImage(light_image=Image.open(dndLight),
                            dark_image=Image.open(dndDark),
                            size=(128,128))

        DADlabel = CTkLabel(DragAndDropFrame,height=60,width=60,
                        image=DADimage,text='')
        DADlabel.pack(padx=10,pady=40)
        DADlabel.pack_propagate(0)
        
    except:

        DADlabel = CTkLabel(DragAndDropFrame,height=60,width=60,
                        text='Невозможно прогрузить изображение!')
        DADlabel.pack(padx=10,pady=40)
        DADlabel.pack_propagate(0)

        pass

    downFrame = CTkFrame(app, height=50, width=500)
    downFrame.pack(pady=10)
    downFrame.pack_propagate(0)

    pathInput = CTkEntry(downFrame, height=30, width=300)
    pathInput.pack(padx=10, pady=10, side=LEFT)    

    openButton = CTkButton(downFrame, width=200, text='Выбрать файл', command=lambda: open_file_dialog(pathInput))
    openButton.pack(side=RIGHT, padx=10, pady=10)

    backbutton = CTkButton(app,width=500, text='Назад в меню', command=helloloop)
    backbutton.pack(side=BOTTOM, padx=10, pady=10)
def friendTest():
    global answerInput,QuestionLabel,scoreLabel,PositionLabel
    global pLeftFrame,pRightFrame

    DragAndDropFrame.forget()
    downFrame.forget()
    backbutton.forget()

    panel_L.forget()
    panel_R.forget()

    pLeftFrame = CTkFrame(app, height=600, width=600,corner_radius=10)
    pLeftFrame.pack(side=LEFT,padx=10,pady=10)
    pLeftFrame.pack_propagate(0)

    missionFrame = CTkFrame(pLeftFrame, height=200, width=650,corner_radius=10)
    missionFrame.pack(padx=10,pady=10)
    missionFrame.pack_propagate(0)
    
    QuestionLabel = CTkLabel(missionFrame, height=200, width=650,corner_radius=10,text='', font=('consolas',20))
    QuestionLabel.pack(padx=10,pady=10)
    QuestionLabel.pack_propagate(0)

    answerFrame = CTkFrame(pLeftFrame, height=60, width=650,corner_radius=10)
    answerFrame.pack(padx=10,pady=10)
    answerFrame.pack_propagate(0)

    answerInput = CTkEntry(answerFrame, height=60, width=450,placeholder_text="Введите ответ...")
    answerInput.pack(padx=10,pady=10,side=LEFT)

    sendAnswerButton = CTkButton(answerFrame, text='Ответить',height=60,width=90, font=('consolas',12),command=AnswerTest)
    sendAnswerButton.pack(padx=10,pady=10,side=RIGHT)

    pRightFrame = CTkFrame(app, height=600, width=300,corner_radius=10)
    pRightFrame.pack(side=LEFT,padx=10,pady=10)
    pRightFrame.pack_propagate(0)

    PositionFrame = CTkFrame(pRightFrame, height=200, width=300,corner_radius=10)
    PositionFrame.pack(padx=10,pady=10)
    PositionFrame.pack_propagate(0)

    PositionLabel = CTkLabel(PositionFrame, height=200, width=300,corner_radius=10, text=TimeClock, font=('consolas',12))
    PositionLabel.pack(padx=10,pady=10)
    PositionLabel.pack_propagate(0)

    scoreFrame = CTkFrame(pRightFrame, height=60, width=300,corner_radius=10)
    scoreFrame.pack(padx=10,pady=10)
    scoreFrame.pack_propagate(0)

    scoreLabel = CTkLabel(scoreFrame, text=f"Score: {Score}", height=100, width=300,corner_radius=10, font=('consolas',12))
    scoreLabel.pack(padx=10,pady=10)
    scoreLabel.pack_propagate(0)

    bottomFrame = CTkFrame(pRightFrame,height=80, width=330,corner_radius=10)
    bottomFrame.pack(padx=10,pady=10,side=BOTTOM)
    bottomFrame.pack_propagate(0)

    exitBeforeTimer = CTkButton(bottomFrame, height=60, width=100, corner_radius=10, text='Завершить\nдосрочно', font=('consolas',12), command=FriendTestEnd)
    exitBeforeTimer.pack(padx=10,pady=10,side=LEFT)

    backButton = CTkButton(bottomFrame, height=60, width=100, corner_radius=10, text='Назад', font=('consolas',12), command=helloloop)
    backButton.pack(padx=10,pady=10,side=LEFT)
    
    pickQuestion()
    pass
def pickQuestion():
    global realTaskPosition,trueAnswer
    print(f'Path: {filename}')
    
    try:
        with open(f'{filename}', 'r') as file:
            data = json.load(file)
            if str(realTaskPosition) in data:
                    current_data = data[str(realTaskPosition)]
                    QuestionLabel.configure(text=current_data["question"])
                    answerInput.delete(0, 'end')
                    trueAnswer = (current_data["answer"])
            else:
                FriendTestEnd()

    except FileNotFoundError:
        print('File not found error. Please check the file path.')
        openTestFile()
    except json.decoder.JSONDecodeError:
        print('JSON decode error. Please check if the file contains valid JSON.')
        openTestFile()

def AnswerTest():
    global realTaskPosition, answerInput, QuestionLabel, correctTaskCount, taskcount

    if str(answerInput.get()) == str(trueAnswer):
        scoreLabel.configure(text=f"Score: {correctTaskCount}")
        correctTaskCount += 1

    taskcount += 1
    realTaskPosition += 1
    pickQuestion()

def FriendTestEnd():
    pLeftFrame.forget()
    pRightFrame.forget()
    
    try:
        _result = (correctTaskCount/taskcount)
    except:
        _result = 0

    if _result <= 0.2:
        message = random.choice([
            "Ваш результат очень низкий. \nРекомендуем потренироваться еще немного! 📚",
            "Уровень вашей математики очень низкий. \nПочитайте математическую литературу для улучшения знаний. 📖",
            "Вам нужно больше практики. \nСосредоточьтесь на основах математики, \nчтобы улучшить результаты. 💪"
        ])
    elif 0.2 < _result <= 0.4:
        message = random.choice([
            "Продолжайте работать над собой. \nПрактика поможет вам улучшить результаты. 🏋️‍♂️",
            "Ваши результаты могут быть лучше. \nПостарайтесь больше времени уделять учебе. 🤓",
            "Не теряйте мотивацию. С постоянными тренировками \nвы достигнете желаемых результатов. 💡"
        ])
    elif 0.4 < _result <= 0.6:
        message = random.choice([
            "Вы на верном пути, однако есть место для улучшений. \nНе останавливайтесь! 🚀",
            "У вас есть потенциал для роста. \nПродолжайте работать над собой и учиться. 💪",
            "Не ограничивайте себя. \nСтремитесь к большему и у вас все получится! 🎯"
        ])
    elif 0.6 < _result <= 0.8:
        message = random.choice([
            "Ваши результаты хороши, но есть место для совершенствования. \nНе останавливайтесь на достигнутом! 🌟",
            "Отличная работа! Продолжайте в том же духе \nи вы достигнете новых высот. 👍",
            "Вы уже добились многого, но не забывайте, \nчто всегда есть возможность стать еще лучше. 🚀"
        ])
    elif 0.8 < _result <= 0.9:
        message = random.choice([
            "Ваши результаты впечатляют! \nПродолжайте двигаться квершинам! 🚀",
            "Вы близки к отличным результатам! \nПродолжайте в том же духе! 💪",
            "Ваш успех близок! Продолжайте так же \nстарательно работать, чтобы достичь своих целей! 🌟"
        ])
    elif 0.9 < _result <= 1.0:
        message = random.choice([
            "Поздравляем с отличными результатами! Вы молодец! 🎉",
            "Прекрасно справляетесь! Так держать! 💪",
            "Вы на вершине успеха! Продолжайте в том же духе! 🌟"
        ])


    result = 'Краткая статистика: \nВерно выполненых задач: {} из {}\nПроцентное соотношение: {}\n\n{}'.format(correctTaskCount,taskcount,_result,message)
    
    FTE_top = CTkFrame(app,height=450,width=900)
    FTE_top.pack(padx=10,pady=10,side=TOP)
    FTE_top.pack_propagate(0)

    TOPleft = CTkScrollableFrame(FTE_top, height=450, width=250, label_text="Пройденные задачи {}".format(taskcount))
    TOPleft.pack(padx=10,pady=10,side=LEFT)

    TOPleftLabel = CTkLabel(TOPleft,width=250,font=('consolas',12),text=AllTasks)
    TOPleftLabel.pack(padx=10,pady=10)

    TOPright = CTkFrame(FTE_top,height=450,width=650)
    TOPright.pack(padx=10,pady=10,side=RIGHT)
    TOPright.pack_propagate(0)

    TOPrightLabel = CTkLabel(TOPright, text='Тестирование завершенно',height=20,width=650)
    TOPrightLabel.pack(side=TOP,padx=10,pady=10)

    RightLabel = CTkLabel(TOPright,height=140,width=650,text=result,font=('consolas',16))
    RightLabel.pack(padx=10,pady=10)

    FTE_bott = CTkFrame(app,height=450,width=900)
    FTE_bott.pack(padx=10,pady=10,side=BOTTOM)
    FTE_bott.pack_propagate(0)

    leftBottomFrame = CTkFrame(FTE_bott,height=450,width=270)
    leftBottomFrame.pack(padx=10,pady=10,side=LEFT)
    leftBottomFrame.pack_propagate(0)

    saveButton = CTkButton(leftBottomFrame,height=450,width=270,text='Сохранить результат',font=('consolas',16),command=saveData)
    saveButton.pack(padx=8,pady=8)
    saveButton.pack_propagate(0)

    rigthBottomFrame = CTkFrame(FTE_bott,height=450,width=650)
    rigthBottomFrame.pack(padx=10,pady=10,side=RIGHT)
    rigthBottomFrame.pack_propagate(0)

    menuButtom = CTkButton(rigthBottomFrame,height=450,width=270,text='Вернуться в меню',font=('consolas',16),command=helloloop)
    menuButtom.pack(padx=8,pady=8,side=RIGHT)
    menuButtom.pack_propagate(0)

    shareButton = CTkButton(rigthBottomFrame,height=450,width=270,text='Отправить отчёт',font=('consolas',16),command='share')
    shareButton.pack(padx=8,pady=8,side=RIGHT)
    shareButton.pack_propagate(0)

    pass

start()