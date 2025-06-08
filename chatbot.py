# Simple rule-based chatbot

print("Hi! I'm ChatBot. Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    if user_input in ["hi", "hello", "hey"]:
        print("Bot: Hello! How can I help you?")
    elif user_input in ["how are you", "how are you doing"]:
        print("Bot: I'm just a bot, but I'm doing great! Thanks for asking.")
    elif user_input in ["what is your name"]:
        print("Bot: I'm your friendly chatbot.")
    elif user_input in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! Have a great day.")
        break
    else:
        print("Bot: I'm not sure how to respond to that.")
