import random

def hangman():
    words = ["python", "hangman", "challenge", "computer", "program"]
    word = random.choice(words)
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect = 6

    print("Welcome to Hangman!")
    print(f"You have {max_incorrect} incorrect guesses allowed.")

    while incorrect_guesses < max_incorrect:
        # Display current guessed word with underscores for missing letters
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "_"
        print("\nWord: ", " ".join(display_word))

        # Check if player has guessed all letters
        if "_" not in display_word:
            print("Congratulations! You guessed the word:", word)
            break

        guess = input("Guess a letter: ").lower()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetical letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Good guess!")
        else:
            incorrect_guesses += 1
            print(f"Wrong guess! You have {max_incorrect - incorrect_guesses} guesses left.")

    else:
        print(f"Sorry, you ran out of guesses. The word was: {word}")

if __name__ == "__main__":
    hangman()
