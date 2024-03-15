
import tkinter as tk
import random
import webbrowser
import datetime
#import python_weather
import os
import asyncio

# Define a dictionary of responses for the chatbot

responses = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "how are you": ["I'm doing well, thanks for asking.", "I'm fine, how about you?"],
    "what's up": ["Nothing much, what's up with you?", "Just chilling, you?"],
    "bye": ["Goodbye!", "See you later!", "Bye!"],
    "tell me about the upcoming expo":["The expo is all about python projects and various inventions","Event where innovation meets code"],
    "date and venue":["The date of this expo is march 16th at 9'0 clock in KITE campus"],
    "main exhibitors":["The main exhibitors are students","The students of KITE campus"],
    "list of companies":["KGISL,Devfolio,Pinesphere,Nunnari labs,Interview buddy"],
    "registration process":["Attendees can register through Devfolio"],
    "feature":["The students who are participating in this expo can interact with industrial people"],
    "are there any workships during this event?":["yes"],
    "main theme":["students can improve technical knowledge","students can discover new inventions"],
    "focus areas":["Interactions with industrial people","Internships opportunities","Knowledge with technologies"],
    "awards or recognitions":["Participation certificate will be provided"],
    "duration":["The duration of the expo is 30hrs","30hrs","march 13th and 14th"],
    "how many students and mentors":["There are around 500 students and 50 mentors"],
    "how many teams":["There are 125 teams are participated in this expo","125 teams"],
    "can you explain the research or projects being showcased here":["The specific research or project being showcased would depend on the theme and foucs of the expo as well as the current trends and intersts in the scientific community"],
    "how many teams":["There are 80 teams developing software related projects and 45 teams are developing hardware related projects","80 hardware projects and 45 software projects"],
    "learning objectives":["Encourage critical thinking,problem-solving,and inquiry-based learning"],


    "default": ["I'm sorry, I didn't understand what you said.", "Could you please rephrase that?", "I'm not sure what you mean."],
}

def get_response(user_input):
    if user_input.lower()=="open youtube":
        webbrowser.open("youtube.com")
        return "Opening"
        
    elif user_input.lower()=='open facebook':
        webbrowser.open("fb.com")
        return "Opening"
    elif user_input.lower()=='open stack overflow':
        webbrowser.open("stackoverflow.com")
        return "Opening"
    elif user_input.lower()=="google":
        webbrowser.open("google.com")
        return "Opening"
    elif user_input.lower()=="open whatsapp":
        webbrowser.open("whatsapp.com")
        return "Opening"
    elif user_input.lower()in ["tell the time","what's the time"]:
        return datetime.datetime.now().strftime("%H:%M")
    
    elif user_input.lower() in responses:
        return random.choice(responses[user_input.lower()])
    else:
        return random.choice(responses["default"])

def handle_input():
    user_input = input_field.get()
    input_field.delete(0, tk.END)
    response = get_response(user_input)

    chat_history.config(state=tk.NORMAL)
    if chat_history.get("1.0", tk.END).strip() == "":
        chat_history.insert(tk.END, f"You: {user_input}\n")
    else:
        chat_history.insert(tk.END, f"\nYou: {user_input}\n")
    chat_history.insert(tk.END, f"Chatbot: {response}\n")
    chat_history.config(state=tk.DISABLED)
    chat_history.see(tk.END)

window = tk.Tk()
window.title("Chatbot")

chat_history = tk.Text(window, state=tk.DISABLED)
chat_history.pack(fill=tk.BOTH, expand=True)

input_field = tk.Entry(window)
input_field.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
submit_button = tk.Button(window, text="Send", command=handle_input)
submit_button.pack(side=tk.RIGHT)


window.mainloop()
