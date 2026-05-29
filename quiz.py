# Project: Interactive Vocabulary Quiz Game
# Data Structure: Python Dictionary (Key-Value Pairs)
# Description: Displays definitions and prompts the user to guess the matching word

import random

# A dictionary mapping words (Keys) to their exact definitions (Values)
vocabulary_dict = {
    "variable": "A named storage location in computer memory that holds a data value.",
    "dictionary": "A data structure that stores information in key-value pairs.",
    "algorithm": "A step-by-step set of instructions or rules followed to solve a problem.",
    "loop": "A programming construct that repeats a block of code until a condition is met.",
    "function": "A reusable block of code designed to perform a single, specific action."
}

print("=== COMPUTER ENGINEERING VOCABULARY QUIZ ===")
print("(Type 'quit' at any time to exit the game)\n")

# Convert the dictionary keys into a list so we can pick random words from it
word_list = list(vocabulary_dict.keys())

score = 0
total_questions = 0

while True:
    # Pick a random word from our list
    random_word = random.choice(word_list)
    # Fetch the definition attached to that random word
    definition = vocabulary_dict[random_word]
    
    # Present the meaning to the user
    print(f"Definition: {definition}")
    user_guess = input("What word matches this definition? ")
    
    # Check if the user wants to quit
    if user_guess.lower() == 'quit':
        print(f"\nGame Over! Your final score is {score}/{total_questions}.")
        print("Thanks for playing!")
        break
        
    total_questions += 1
    
    # Check if the user input matches the correct word (ignoring upper/lower case)
    if user_guess.lower() == random_word.lower():
        score += 1
        print("✅ Correct! Brilliant job.\n")
    else:
        print(f"❌ Incorrect. The correct word was: '{random_word}'\n")
