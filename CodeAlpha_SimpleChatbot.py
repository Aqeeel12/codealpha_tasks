def chatbot():
    print("Alpha is online. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ").lower().strip()

        if user_input in ["hello", "hi", "hey"]:
            print("Alpha: Hey there! Great to see you. How can I assist you today?")
        elif user_input in ["how are you", "how are you doing", "how's it going"]:
            print("Alpha: I'm doing fantastic! Thanks for asking. What about you?")
        elif user_input in ["i'm fine", "i am good", "doing well", "good"]:
            print("Alpha: That's awesome to hear! How can I help you today?")
        elif user_input in ["what's your name", "who are you"]:
            print("Alpha: I'm Alpha, your friendly chatbot assistant. Nice to meet you!")
        elif user_input in ["thank you", "thanks", "thanks a lot"]:
            print("Alpha: You're very welcome! Happy to help anytime.")
        elif user_input in ["bye", "goodbye", "see you"]:
            print("Alpha: Goodbye! Take care and have an amazing day ahead!")
            break
        else:
            print("Alpha: Hmm, I’m not sure I understand that. Could you please rephrase?")

if __name__ == "__main__":
    chatbot()
