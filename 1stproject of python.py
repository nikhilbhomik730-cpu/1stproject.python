# Rule-based chatbot
print("Hello! Welcome to your AI chatbot.")
print("Ask me basic questions. Type 'Bye' to exit.")

responses = {
    "hello": "Hi, welcome. How can I help you?",
    "how are you": "I am very fine. Thank you!",
    "who are you": "I am a smart AI chatbot.",
    "motivate me": "Keep going. Every bug in your project makes you a better developer.",
    "happy": "Great to hear that!",
    "what is functions": (
        "A function in Python is a named, reusable block of code designed "
        "to perform a specific task."
    ),
    "what is python": (
        "Python is a high-level, general-purpose programming language known "
        "for its simple, readable syntax. It was created by Guido van Rossum "
        "and first released in 1991."
    ),
    "who is the developer of this ai chat bot": "Nikhil Bhomik",
    "what is lists in python": (
        "A list in Python is a built-in data structure used to store an "
        "ordered, changeable (mutable) collection of items."
    ),
}

def get_response(user_question):
    question = user_question.strip().lower().rstrip("?!.")
    return responses.get(
        question,
        "I am not able to tell you that yet. I will learn this soon.",
    )


while True:
    user_input = input("Please ask your question: ")
    if user_input.strip().lower() == "bye":
        print("Goodbye!")
        break
    print("Bot response:", get_response(user_input))