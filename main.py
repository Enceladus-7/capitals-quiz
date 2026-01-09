import quiz_logic

def run_quiz():
    print("Welcome to the Geography Quiz!")

    # Load the data using the filename.
    file_path = "capitals.txt"
    quiz_data = quiz_logic.load_data(file_path)

    # Check the data loaded, otherwise return an error.
    if not quiz_data:
        print("Quiz cannot start because data is missing.")
        return
    
    # Start a score counter and set the number of rounds.
    score = 0
    total_rounds = 5

    # Loop through the game rounds.
    for i in range(total_rounds):
        # Get a random question.
        question_data = quiz_logic.new_question(quiz_data)

        print(f"\nQuestion {i + 1} of {total_rounds}")
        print(f"What is the capital of {question_data['country']}?")
        print("-" * 30)

        # Display the options for the user to pick.
        labels = ["A", "B", "C", "D"]
        options = question_data['options']

        for index in range(4):
            print(f"{labels[index]}) {options[index]}")

        # Retreive user input and account for formatting.
        user_choice = input("\nYour Answer (A/B/C/D): ").upper().strip()

        # Check if user returned the correct answer.
        if user_choice in labels:
            # Find the index of the user's choice.
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