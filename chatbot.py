import random
from datetime import datetime

# -------- Chatbot Data -------- #

greetings = ["Hello!", "Hi there!", "Hey!", "Hi! Nice to see you."]
farewells = ["Goodbye!", "See you later!", "Take care!"]
fallbacks = [
    "I'm not sure I understand.",
    "Can you rephrase that?",
    "That’s interesting, tell me more."
]

user_name = ""

# -------- Functions -------- #

def greet():
    return random.choice(greetings)

def ask_name():
    return "I am a rule-based chatbot created using Python."

def store_name(user_input):
    global user_name
    user_name = user_input.split("my name is")[-1].strip().title()
    return f"Nice to meet you, {user_name}!"

def recall_name():
    if user_name:
        return f"Your name is {user_name}."
    return "I don't know your name yet."

def tell_time():
    return "Current time is " + datetime.now().strftime("%H:%M:%S")

def tell_joke():
    jokes = [
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "Why did the computer get cold? Because it forgot to close Windows!",
        "Why do Python developers wear glasses? Because they can't C!"
    ]
    return random.choice(jokes)

def help_menu():
    return "Try greetings, tell me your name, ask time, or ask for a joke."

# -------- Main Program -------- #

def chatbot():
    print("Chatbot: Hello! I'm your rule-based chatbot.")
    print("Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ").lower()

        if any(word in user_input for word in ["hello", "hi", "hey"]):
            print("Chatbot:", greet())

        elif "my name is" in user_input:
            print("Chatbot:", store_name(user_input))

        elif "your name" in user_input:
            print("Chatbot:", ask_name())

        elif "what is my name" in user_input:
            print("Chatbot:", recall_name())

        elif "how are you" in user_input:
            print("Chatbot: I'm doing great! Thanks for asking.")

        elif "time" in user_input:
            print("Chatbot:", tell_time())

        elif "joke" in user_input:
            print("Chatbot:", tell_joke())

        elif "help" in user_input:
            print("Chatbot:", help_menu())

        elif "bye" in user_input:
            print("Chatbot:", random.choice(farewells))
            break

        else:
            print("Chatbot:", random.choice(fallbacks))


# -------- Run Program -------- #

if __name__ == "__main__":
    chatbot()