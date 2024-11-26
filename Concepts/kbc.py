# Kaun Banega Crorepati (KBC) Game
import sys

# Questions, options, and answers
questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. Delhi", "C. Kolkata", "D. Chennai"],
        "answer": "B"
    },
    {
        "question": "Which is the largest planet in our Solar System?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"],
        "answer": "C"
    },
    {
        "question": "What is the square root of 64?",
        "options": ["A. 6", "B. 8", "C. 10", "D. 12"],
        "answer": "B"
    },
    {
        "question": "Who wrote the national anthem of India?",
        "options": [
            "A. Rabindranath Tagore",
            "B. Mahatma Gandhi",
            "C. Subhash Chandra Bose",
            "D. Jawaharlal Nehru"
        ],
        "answer": "A"
    },
    {
        "question": "Which element is denoted by the symbol 'O' in the periodic table?",
        "options": ["A. Gold", "B. Oxygen", "C. Osmium", "D. Ozone"],
        "answer": "B"
    },
]

# Prize money for each question
prizes = [1000, 5000, 10000, 50000, 100000]

# Lifelines
lifelines_used = {
    "50-50": False
}

# Function to use the 50-50 lifeline
def use_50_50(question, answer):
    if lifelines_used["50-50"]:
        print("\nYou have already used the 50-50 lifeline.")
        return None
    
    lifelines_used["50-50"] = True
    correct_option = answer
    wrong_options = [opt[0] for opt in question["options"] if opt[0] != correct_option]
    reduced_options = [correct_option, wrong_options[0]]  # Keep 1 wrong and 1 correct
    print("\n50-50 Lifeline Activated! Here are the options:")
    for opt in reduced_options:
        for full_opt in question["options"]:
            if full_opt.startswith(opt):
                print(full_opt)

# KBC Game Logic
def play_kbc():
    print("\nWelcome to Kaun Banega Crorepati!")
    print("Answer the following questions to win exciting prizes!\n")

    total_prize = 0
    for i, question in enumerate(questions):
        print(f"Question {i + 1} for Rs. {prizes[i]}:")
        print(question["question"])
        for option in question["options"]:
            print(option)

        # Ask for input
        while True:
            print("\nEnter your answer (A/B/C/D) or type 'lifeline' for 50-50:")
            user_input = input().strip().upper()

            if user_input == "LIFELINE":
                use_50_50(question, question["answer"])
                continue  # Allow the user to answer after using lifeline
            elif user_input in ["A", "B", "C", "D"]:
                break
            else:
                print("Invalid input. Please try again.")

        # Check the answer
        if user_input == question["answer"]:
            total_prize += prizes[i]
            print(f"Correct! You have won Rs. {total_prize}.\n")
        else:
            print(f"Wrong answer! The correct answer was {question['answer']}.")
            print(f"You leave with Rs. {total_prize}.")
            sys.exit()  # End the game if the answer is wrong

    print(f"Congratulations! You have won the grand prize of Rs. {total_prize}.")

# Start the game
play_kbc()
