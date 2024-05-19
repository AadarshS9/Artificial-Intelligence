import random

def guess_word(word):
    max_attempts = 7
    attempts = 0
    guessed_word = "_" * len(word)
   
    while attempts < max_attempts and "_" in guessed_word:
        print("\nWord to guess:", guessed_word)
        guess = input("Guess a character: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetic character.")
            continue

        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    guessed_word = guessed_word[:i] + guess + guessed_word[i+1:]
            print("Correct guess!")
        else:
            print("Incorrect guess.")
            attempts += 1

    if "_" not in guessed_word:
        print("Congratulations, you guessed the word:", word)
    else:
        print("\nSorry, you couldn't guess the word. The word was:", word)

words = ["rajagiri", "school", "of", "engineering", "and", "technology"] 
selected_word = random.choice(words)
name=input("Kindly enter your name: ")
print("\nNOTE! You have a maximum of 7 lives to guess the word")
guess_word(selected_word)
