import random

print("🤖 AI Chatbot")
print("Type 'exit' to end the conversation.")

while True:
    message = input("You: ").lower().strip()

    if message in ["hi", "hello", "hey"]:
        responses = [
            "Hello! 👋",
            "Hi! How can I help you?",
            "Hey! Nice to meet you!"
        ]
        print("Bot:", random.choice(responses))

    elif "what can you do" in message:
        print("Bot: I can chat with you, answer simple questions, and help you.")

    elif "help" in message:
        print("Bot: You can say hello, ask what I can do, or type exit.")

    elif message in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! 👋")
        break

    else:
        print("Bot: Sorry, I don't understand that yet.")
