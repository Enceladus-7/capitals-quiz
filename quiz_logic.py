import random

# Reads a text file to retreive a list of dictionaries containing a 'country' & 'capital'.
def load_data(filename):
    
    data = []

    try:
        with open(filename) as file:
            for line in file:
                # Remove any unwanted characters.
                clean_line = line.strip()

                # Check if line is empty and if so skip it.
                if not clean_line:
                    continue

                # Split the line at the comma.
                parts = clean_line.split(',')

                # Check for errors, ensuring we only have two parts (country & capital).
                if len(parts) == 2:
                    country_name = parts[0].strip()
                    capital_city = parts[1].strip()

                    # Add to our list as a dictionary.
                    data.append({
                        "country": country_name,
                        "capital": capital_city
                    })

        return data
    
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return[]

# Picks a random country and 3 incorrect choices.
# Returns a dictionary containing the question and shuffled answers.
def new_question(data_list):
    # Select the correct answer.
    correct_pair = random.choice(data_list)

    # Create a list of incorrect answer options.
    other_options =  [item for item in data_list if item != correct_pair]
    wrong_answers = random.sample(other_options, 3)

    # Create a list of all options to pick from.
    all_options = [correct_pair['capital']]

    # Add the wrong answers to the list of all answers.
    for wrong in wrong_answers:
        all_options.append(wrong['capital'])

    # Shuffle the answers so it's not always the same one.
    random.shuffle(all_options)

    return {
        "country": correct_pair['country'],
        "correct_answer": correct_pair['capital'],
        "options": all_options
    }