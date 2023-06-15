import random
import tkinter as tk
from tkinter import messagebox

# Word lists for different levels
beginners_words = ['apple', 'banana', 'cherry', 'grape', 'lemon']
moderate_words = ['elephant', 'giraffe', 'kangaroo', 'leopard', 'octopus']
expert_words = ['watermelon', 'pineapple', 'strawberry', 'blackberry', 'raspberry']

# Function to check if input is a letter
def is_letter(input):
    return input.isalpha() and len(input) == 1

# Function to validate user's guess
def validate_guess():
    guess = entry.get().lower()
    if is_letter(guess):
        return guess
    else:
        messagebox.showerror("Error", "Invalid input! Please enter a single letter.")

# Function to play the game
def play_game():
    level = level_var.get()
    if level == 'Beginner':
        words = beginners_words
        max_word_length = 5
        max_attempts = 5
    elif level == 'Moderate':
        words = moderate_words
        max_word_length = 8
        max_attempts = 7
    elif level == 'Expert':
        words = expert_words
        max_word_length = float('inf')
        max_attempts = 10
    else:
        messagebox.showerror("Error", "Invalid level!")
        return

    word = random.choice(words)
    word_length = len(word)
    attempts = 0

    output_text.set("Guess the word! It has {} letters.".format(word_length))
    while attempts < max_attempts:
        guess = validate_guess()
        attempts += 1

        if guess in word:
            if guess == word:
                messagebox.showinfo("Congratulations", "You guessed the word '{}' correctly.".format(word))
                return
            else:
                matched_positions = [i for i, letter in enumerate(word) if letter == guess]
                output_text.set("The letter '{}' appears at position(s): {}".format(guess, matched_positions))
        else:
            output_text.set("Sorry, the letter '{}' is not in the word.".format(guess))

    messagebox.showinfo("Game Over", "Out of attempts! The word was '{}'.".format(word))

# Create the main window
window = tk.Tk()
window.title("Word Guessing Game")

# Create and pack the GUI elements
level_var = tk.StringVar(window)
level_var.set("Beginner")
level_label = tk.Label(window, text="Select a level:")
level_label.pack()
level_menu = tk.OptionMenu(window, level_var, "Beginner", "Moderate", "Expert")
level_menu.pack()

guess_label = tk.Label(window, text="Enter your guess:")
guess_label.pack()
entry = tk.Entry(window)
entry.pack()

guess_button = tk.Button(window, text="Guess", command=play_game)
guess_button.pack()

output_text = tk.StringVar()
output_label = tk.Label(window, textvariable=output_text)
output_label.pack()

# Start the GUI event loop
window.mainloop()
