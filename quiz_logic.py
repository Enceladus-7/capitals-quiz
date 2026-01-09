# Used to select random questions and shuffle answer choices.
import random

def load_data(filename):
    """
    Reads a text file to retrieve a list of dictionaries containing a 'country' & 'capital'.
    Handles file not found errors.
    """
    data = []

    try:
        with open(filename) as file:
            for line in file:
                clean_line = line.strip()

                if not clean_line:
                    continue

                parts = clean_line.split(',')

                # Check for errors, ensuring we only have two parts (country & capital).
                if len(parts) == 2:
                    country_name = parts[0].strip()
                    capital_city = parts[1].strip()

                    data.append({
                        "country": country_name,
                        "capital": capital_city
                    })

        return data
    
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return[]

def generate_question(target_country, all_data):
    """
    Generates options for a specific country provided by main.py
    """
    correct_pair = target_country

    other_options =  [item for item in all_data if item != correct_pair]
    wrong_answers = random.sample(other_options, 3)

    all_options = [correct_pair['capital']]
    for wrong in wrong_answers:
        all_options.append(wrong['capital'])

    # Randomise the position of the correct answer.
    random.shuffle(all_options)

    return {
        "country": correct_pair['country'],
        "correct_answer": correct_pair['capital'],
        "options": all_options
    }