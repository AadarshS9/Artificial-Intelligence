# Aim
Write a program to implement Hangman Game.

# Theoretical Background
The hangman game is a multiplayer game. It is about guessing letters from A to Z to form the words. If the player guesses the right letter that is within the word, the letter appears at its correct position. The user has to guess the correct word until a man is hung, then the game is over. The one
who is playing is having a certain number of guesses to guess the characters in the word. If the players are able to guess the characters in the entire word within certain attempts, they win otherwise they’ll lose.

# Algorithm
- Step 1: Start.
- Step 2: Read the name of the user using the input() method.
- Step 3: Select a random word from a list of words and start guessing the characters in the word.
- Step 4: Define the maximum number of attempts the user can take.
- Step 5: Use a while loop to repeatedly ask the user to guess the character until the attempts are exhausted.
- Step 6: Inside the while loop, if the user guesses the correct character, then include it in the response. Otherwise notify them that they made a mistake.
- Step 7: If the user is able to guess all the characters of the word within the maximum number of attempts, then they’ll win.
- Step 8: If the user exhausts all their attempts before guessing the entire word then they’ll lose.
- Step 9: Stop.

# Solution
- hangman.py
- hangman.png
