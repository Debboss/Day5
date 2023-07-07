from faker import Faker
import random

print("Welcome to the Hangman game!")

start = input("Press any button to continue: ")

fake = Faker()
random_word = fake.word()

# print(random_word)

print("The word you need to guess is:")

guessed_letters = []

for letter in random_word:
    if letter in guessed_letters:
        print(letter, end=" ")
    else:
        print("_", end=" ")

quit_word = "quit"

while True:
    guess_letter = input("\nGuess a letter (or enter 'quit' to exit): ")

    if guess_letter.lower() == quit_word:
        print("You have chosen to quit the game. Goodbye!")
        break

    if len(guess_letter) != 1:
        print("Please enter a single letter or 'quit'.")
        continue

    if guess_letter in guessed_letters:
        print("You already guessed that letter. Try again.")
        continue

    if guess_letter in random_word:
        guessed_letters.append(guess_letter)
        print("Correct guess!")
    else:
        print("Wrong guess!")

    # Check if all letters have been guessed correctly
    if all(letter in guessed_letters for letter in random_word):
        print("Congratulations! You guessed the word correctly.")
        break
