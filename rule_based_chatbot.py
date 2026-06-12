print("🤖 StudentBot: Hello! I am your rule-based AI chatbot.")
print("Type 'help' to see what I can do. Type 'bye' to exit.\n")

while True:
    user_input = input("You: ").lower().strip()

    if user_input in ["hi", "hello", "hey"]:
        print("StudentBot: Hello! How can I help you today?")

    elif user_input in ["how are you", "how are you?"]:
        print("StudentBot: I am just code, but I am running perfectly!")

    elif user_input == "help":
        print("StudentBot: You can ask me about AI, internship, Python, project, or college.")

    elif user_input == "ai":
        print("StudentBot: AI means Artificial Intelligence. It helps machines think and respond smartly.")

    elif user_input == "python":
        print("StudentBot: Python is a beginner-friendly programming language used in AI and automation.")

    elif user_input == "internship":
        print("StudentBot: This internship helps you build projects and improve your practical skills.")

    elif user_input == "project":
        print("StudentBot: Your first project is a rule-based chatbot using if-else logic.")

    elif user_input == "college":
        print("StudentBot: College life is the best place to build skills, projects, and confidence.")

    elif user_input in ["bye", "exit", "quit"]:
        print("StudentBot: Goodbye! Keep learning and building. 🚀")
        break

    else:
        print("StudentBot: Sorry, I don't understand that. Type 'help' to see available commands.")