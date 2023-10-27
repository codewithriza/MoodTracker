#The provided project is a voice-enabled Mood Analyzer application that utilizes speech recognition to capture daily mood input, performs sentiment analysis, and visually represents mood data, offering real-time updates and insights into users' weekly emotional trends.
#Made By Riza,Habil,Rihan

import speech_recognition as sr
import tkinter as tk
from textblob import TextBlob
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

mood_data = {'Happy': 0, 'Sad': 0, 'Neutral': 0}
weekly_mood = []

def update_mood(text):
    global mood_data
    global weekly_mood

    analysis = TextBlob(text)
    sentiment = analysis.sentiment.polarity

    if sentiment > 0:
        mood = 'Happy'
    elif sentiment < 0:
        mood = 'Sad'
    else:
        mood = 'Neutral'

    mood_data[mood] += 1
    weekly_mood.append(mood)

def get_weekly_mood():
    week_start = datetime.now() - timedelta(days=datetime.now().weekday())
    week_mood = [mood_data[m] for m in weekly_mood if (datetime.now() - timedelta(days=datetime.now().weekday())) <= week_start]
    weekly_mood.clear()

    if not week_mood:
        return "No data"
    
    avg_mood = sum(week_mood) / len(week_mood)
    
    if avg_mood > 0:
        return 'Happy'
    elif avg_mood < 0:
        return 'Sad'
    else:
        return 'Neutral'

def record_and_analyze():
    user_input = speech_to_text()
    update_mood(user_input)
    update_gui()

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something about your day...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Speech not recognized"
    except sr.RequestError as e:
        return f"Could not request results; {e}"

def update_gui():
    pie_chart.clear()
    pie_chart.pie(mood_data.values(), labels=mood_data.keys(), autopct='%1.1f%%', startangle=140)
    pie_chart.axis('equal')
    canvas.draw()

root = tk.Tk()
root.title("Mood Analyzer")

record_button = tk.Button(root, text="Record and Analyze", command=record_and_analyze)
record_button.pack()

chart_frame = ttk.Frame(root)
chart_frame.pack()

fig = Figure(figsize=(4, 4))
pie_chart = fig.add_subplot(111)

canvas = FigureCanvasTkAgg(fig, chart_frame)
canvas.get_tk_widget().pack()

weekly_label = tk.Label(root, text="Weekly Overall Mood: " + get_weekly_mood())
weekly_label.pack()

root.mainloop()
