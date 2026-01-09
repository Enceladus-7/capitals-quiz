# Python Capital Cities Quiz

## Description
This is a text-based geography quiz application written in Python. It reads country and capital city data from a text file, processes it, and presents a multiple-choice quiz to the user in the terminal.

## User Documentation (How to Use)
1. **Prerequisites:** Ensure you have Python 3 installed on your computer.
2. **Download:** Download the three files ('main.py', 'quiz_logic.py', 'capitals.txt') and place them in the same folder.
3. **Run:** Open your terminal/command prompt, navigate to the folder, and type:
  python main.py
4. **Play:**
   - The game will ask you "What is the capital of [Country]?" and give you four options to pick from.
   - Type the letter (A, B, C, or D) corresponding to your answer.
   - The game tracks your score and displays it at the end.

## Technical Documentation (How it Works)
The project utilises a modular design split into two Python files and one data file.

### Files
* **main.py:** The entry point. It manages the game loop, keeps track of the deck of available questions to prevent duplicates, and handles user input.
* **quiz_logic.py:** Contains the backend logic. It handles parsing the text file and generating random wrong answers for each question.
*  **capitals.txt:** A comma-delimited text file ('Country,Capital') serving as the database.

### Key Features
* **Duplicate Prevention:** The program loads all questions into a pool and shuffles them once at the start. Questions are removed (`.pop()`) one by one as they are asked, ensuring the user never sees the same country twice in one game.
* **File Handling:** Uses 'with open()' and string parsing ('strip', 'split') to process raw data without external CSV libraries.
* **Error Handling:** Includes 'try/except' blocks to handle 'FileNotFoundError' if the data file is missing.
* **Scalability:** New questions can be added simply by editing the '.txt' file. No code changes are required.
