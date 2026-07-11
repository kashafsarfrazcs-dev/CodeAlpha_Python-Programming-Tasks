import random

def choose_word():
    words = ["python", "hangman", "developer", "internship", "programming"]
    return random.choice(words)

def display_progress(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def play_hangman():
    word = choose_word()
    guessed_letters = []
    attempts_left = 6

    print("Welcome to Hangman!")
    print(f"You have {attempts_left} incorrect guesses allowed.\n")

    while attempts_left > 0:
        print(display_progress(word, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.\n")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct guess!\n")
            if all(letter in guessed_letters for letter in word):
                print(f"Congratulations! You guessed the word: {word}")
                return
        else:
            attempts_left -= 1
            print(f"Wrong guess! Attempts left: {attempts_left}\n")

    print(f"Game over! The word was: {word}")

if __name__ == "__main__":
    play_hangman()
