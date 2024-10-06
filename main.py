import random
import os
from hangman_art import stages,logo
from hangman_words import word_list

print (f"{logo}\n\n")
chosen_word = random.choice(word_list)
display = []
for letter in chosen_word:
    display.append("_")
lives = 6 #Number of chances available for the user.
guessed_letters = []
while "_" in display and lives !=0:
    print(f"{' '.join(display)}\n")
    print(stages[lives])
    guess = input("Guess a letter: ").lower()
    position = 0
    os.system('cls' if os.name == 'nt' else 'clear')
    if guess not in guessed_letters:
        if guess in chosen_word:
            for letter in chosen_word:
                if letter == guess:
                    display[position] = letter
                position += 1 
        else:
            lives -= 1 
            print(f"Your guess {guess} is not in the word. You lose a life.")
    else:
        print(f"You already have guessed the letter {guess}. Pick another letter.")
    guessed_letters.append(guess)
if lives == 0:
    print ("Game over. You lose.")
else:
    print ("Congratulations. You won!")
