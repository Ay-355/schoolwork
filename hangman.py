import random
import sys

choice = input("Would you like to get a [R]andom word, or [I]nput your own: ").lower()
if choice == "r":
    with open("words.txt") as f:
        word = random.choice(f.read().splitlines())
elif choice == "i":
    word = input("What word would you like to guess: ").lower()
else:
    print("Could not recognize input, closing.")
    sys.exit(1)

wrong = 0
guessed = []
current = list(len(word) * "_")
won = False

hc = ['''
    +---+
    |   |
        |
        |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
        |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
   /|   |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
   /|\  |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
    =========''', '''
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
    =========''']

while not won:
    print(f"-------------------\nCurrent progress: {''.join(current)}\n")
    inp = input("Your guess: ").lower()
    length = len(inp)
    if inp in guessed:
        print("Already guessed letter/word\n")
        continue
    if length == 1:
        guessed.append(inp)
        if inp in word:
            print(f"You got the letter `{inp}`\n")
            for i, letter in enumerate(word):
                if letter == inp:
                    current[i] = inp
            final = "".join(current)
            if final == word:
                won = True
        else:
            print("Incorrect. Hangman:")
            print(hc[wrong])
            if wrong < 6:
                wrong += 1
    elif length == len(current):
        if inp == word:
            won = True
        else:
            guessed.append(inp)
            print("Not the correct word. Hangman: ")
            print(hc[wrong])
            if wrong < 6:
                wrong += 1
    else:
        print("Has to be one character or the word\n")

print(f"You win! The word was {word}")
print(f"Took you {len(guessed)} tries")
