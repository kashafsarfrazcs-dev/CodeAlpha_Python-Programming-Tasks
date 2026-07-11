def chatbot_response(user_input):
    user_input = user_input.lower().strip()

    greetings = ["hello", "hi", "hey"]
    how_are_you = ["how are you", "how are you doing", "how's it going"]
    farewells = ["bye", "goodbye", "see you"]
    thanks = ["thank you", "thanks"]
    name_questions = ["what is your name", "who are you"]

    if any(word in user_input for word in greetings):
        return "Hi there! How can I help you today?"
    elif any(phrase in user_input for phrase in how_are_you):
        return "I'm fine, thanks! How about you?"
    elif any(word in user_input for word in farewells):
        return "Goodbye! Have a great day!"
    elif any(word in user_input for word in thanks):
        return "You're welcome!"
    elif any(phrase in user_input for phrase in name_questions):
        return "I'm a simple rule-based chatbot built with Python."
    else:
        return "I'm sorry, I didn't understand that. Can you rephrase?"

def run_chatbot():
    print("Chatbot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

        if "bye" in user_input.lower():
            break

if __name__ == "__main__":
    run_chatbot()
