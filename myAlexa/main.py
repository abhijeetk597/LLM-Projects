import speech_recognition as sr
import pyttsx3
import pywhatkit
# from pywhatkit import sendwhatmsg
import datetime
import wikipedia
import pandas as pd
from dotenv import load_dotenv
from langchain_openai import OpenAI

load_dotenv()

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

llm = OpenAI(model_name = "gpt-3.5-turbo-instruct")


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "alexa" in command:
                command = command.replace("alexa ", "")
                print(command)
                return command
    except:
        pass


def get_birthday():
    bd_df = pd.read_csv(r"C:\Users\abhirav\Desktop\birthday.csv")
    bd_df.date = pd.to_datetime(bd_df.date, format="%d-%m-%Y")
    birthday = bd_df[
        (bd_df.date.dt.month == datetime.datetime.today().month)\
        & (bd_df.date.dt.day == datetime.datetime.today().day)]
    return birthday


def run_alexa():
    command = take_command()
    # print(command)
    if "play" in command:
        song = command.replace("play", "")
        talk("playing " + song)
        pywhatkit.playonyt(song)
    elif "is time" in command or "is the time" in command or "the time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        print(time)
        talk(f"current time is {time}")
    elif command.startswith("who is") or command.startswith("what is"):
        if command.startswith("who is"):
            entity = command.replace("who is", "")
        if command.startswith("what is"):
            entity = command.replace("what is", "")
        try:
            info = wikipedia.summary(entity, 2)
        except:
            info = llm.invoke(command)
        print(info)
        talk(info)
    elif command.startswith("how") or "chat gpt" in command:
        if "ask chat gpt" in command:
            command = command.replace("ask chat gpt", "")
        talk("asking chat gpt " + command)
        info = llm.invoke(command)
        talk(info)
    elif "birthday today" in command:
        birthday = get_birthday()
        if len(birthday) == 0:
            talk("There isn't any birthday today")
        if len(birthday) == 1:
            talk(f"It's {birthday.name[0]}'s birthday, today")
        if len(birthday) > 1:
            talk(f"Today is birthday of {list(birthday.name)}")
    else:
        talk("Hey, I didn't understand. Could you please repeat?")

# while True:
#     run_alexa()

"""
------------My Alexa-------------
Functionalities:
1) Play a song on youtube
2) Check current time
3) Search wikipedia for "who is?" and "what is?" questions
4) Ask ChatGPT
5) Search today's birthdays in my contacts
"""