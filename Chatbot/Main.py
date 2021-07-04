from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
import pyttsx3 as pp
import speech_recognition as s
import threading



engine= pp.init()
voices= engine.getProperty('voices')
print(voices)
engine.setProperty('voice',voices[1].id)


# rate = engine.getProperty('rate')
# engine.setProperty('rate', rate-10)
# print(rate)
# engine.say('The quick brown fox jumped over the lazy dog.')
# engine.runAndWait()

def speak(word):
    engine.say(word)
    engine.runAndWait()


# from PIL import ImageTk

bot = ChatBot("My Bot")

convo =[
    "Hello",
    "Hi there",
    "What is your name?",
    "My name is bot, I am created by Vikas",
    "what is your name?",
    "My name is bot, I am created by Vikas",
    "How are you",
    "I am good"
]

trainer = ListTrainer(bot)

trainer.train(convo)
#
# # answer = bot.get_response("How are you")
# # print(answer)

# print("Talk to bot")
# while True:
#     query = input()
#     if query == "exit":
#         break
#     answer = bot.get_response(query)
#     print("bot : ", answer)

main=Tk()
main.geometry("500x450")
main.title("My Chatbot")
img = PhotoImage(file="bot2.png")
# img = PhotoImage(file="bot1.jpg")
photol = Label(image=img)
photol.pack()


# it takes query from user in audio form
def takeQuery():
    sr=s.Recognizer()
    sr.pause_threshold=1
    print("your bot is listening , "
          "please try to communicate with him")
    with s.Microphone() as m:
         try:
            audio=sr.listen(m)
            query=sr.recognize_google(audio,language='eng-in')
            print(query)
            textF.delete(0,END)
            textF.insert(0,query)
            ask_from_bot()
         except Exception as e:
             print(e)
             print("Sorry I did not get that")
             # answer="Sorry I did not get that"
             # textF.delete(0, END)
             # msgs.insert(END,"bot :" + str(answer))
             # speak(answer)
             # textF.delete(0, END)
             # msgs.yview(END)


def ask_from_bot():
    query = textF.get()
    answer= bot.get_response(query)
    msgs.insert(END,"you :"+query)
    msgs.insert(END,"bot :" + str(answer))
    speak(answer)
    textF.delete(0,END)
    msgs.yview(END)



frame = Frame(main)
sc = Scrollbar(frame)
msgs = Listbox(frame, width=80, height=10 , yscrollcommand=sc.set)
sc.pack(side=RIGHT, fill=Y)
msgs.pack(side=LEFT, fill=BOTH, pady=10)

frame.pack()

# creating test feild
textF = Entry(main, font=("verdana",20))
textF.pack(fill=X, pady=10)

btn = Button(main, text="Ask from bot", font=("verdana", 20),
             command=ask_from_bot)
btn.pack()

# creating a function


def enterfunction(event):
    btn.invoke()


# going to bind main window with enter key
main.bind('<Return>', enterfunction)


def repeatListening():
    while True:
        takeQuery()


t = threading.Thread(target=repeatListening)
t.start()

main.mainloop()



