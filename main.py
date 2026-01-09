# Imports the custom logic module containing file handling and game mechanics.
import quiz_logic
# Used to shuffle the list of questions.
import random

def run_quiz():
    """
    Main function to run the grography quiz loop.
    Handles user input, scoring, and display.
    """
    print("Welcome to the Geography Quiz!")

    file_path = "capitals.txt"
    quiz_data = quiz_logic.load_data(file_path)

    # Check the data loaded, overwise return an error.
    if not quiz_data:
        print("Quiz cannot start because data is missing.")
        return
    
    # Create a copy of the data and shuffle it.
    question_pool = quiz_data[:]
    random.shuffle(question_pool)

    # Ensure we don't ask more questions than we have available.
    total_rounds = 5
    if total_rounds > len(question_pool):
        total_rounds = len(question_pool)

    score = 0

    for i in range(total_rounds):
        # Remove one country from the pool so it cannot be asked again.
        current_target = question_pool.pop()

        question_data = quiz_logic.generate_question(current_target, quiz_data)

        print(f"\nQuestion {i + 1} of {total_rounds}")
        print(f"What is the capital of {question_data['country']}?")
        print("-" * 30)

        labels = ["A", "B", "C", "D"]
        options = question_data['options']

        for index in range(4):
            print(f"{labels[index]}) {options[index]}")

        # Retreive user input and account for formatting.
        user_choice = input("\nYour Answer (A/B/C/D): ").upper().strip()

        if user_choice in labels:
            choice_index = labels.index(user_choice)
            selected_city = options[choice_index]

            if selected_city == question_data['correct_answer']:
                print("Correct! +1 Point")
                score += 1
            else:
                print(f"Incorrect. The correct answer was: {question_data['correct_answer']}")
        else:
            print(f"Invalid input. The correct answer was: {question_data['correct_answer']}")
    
    # Show End Game Summary.
    print("\n" + "=" * 30)
    print(f"Game Over")
    print(f"Your Final Score: {score} / {total_rounds}")
    print("=" *30)

run_quiz()