import random

word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

guess = input("Choose a letter: ").lower()

for char in chosen_word:
    if char == guess:
        print("Right")
    else:
        print("Wrong")