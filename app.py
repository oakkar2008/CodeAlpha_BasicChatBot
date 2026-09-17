# Chat Bot

user = {"hello": "Hello. How may I assist you today?",
        "how are you?": "I am functioning well, thank you for asking. How can I help you?",
        "what is your name?": "I am a rule-based chatbot designed to provide basic assistance.",
        "what can you do?": "I can respond to common greetings and simple queries based on predefined rules.",
        "can you tell me a joke?": "Certainly, Why do programmers prefer dark mode? Because light attracts bugs",
        "that is quite amusing.": "I am glad you found it entertaining",
        "what time is it?": "I do not have access to real-time clock data. Please check your device for the current time.",
        "thank you for your help.": "You are most welcome. Is there anything else I can assist you with?",
        "no, that will be all.": "Understood. Please feel free to return if you need further assistance.",
        "bye": "Goodbye. Have a productive day."
}

def get_user_input():
    user_input = input("User: ").lower()
    return user_input

def get_bot_response(user_input):
    if user_input in user:
        return user[user_input]
    else:
        return "Sorry I don't understand"


def chat():
    print("Bot: Hello!! Type 'bye' to exit\n")

    while True:
        user_input = get_user_input()

        bot_reply = get_bot_response(user_input)
        print(f'Bot: {bot_reply}\n')

        if user_input == "bye":
            break

chat()
