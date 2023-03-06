import random

word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

display = []

word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"

# print(display)

guess = input("Choose a letter: ").lower()

for position in range(word_length):
    letter = chosen_word[position]
    # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
    if letter == guess:
        display[position] = letter

print(display)