import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
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
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

lives = 6

display = []

word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"

# print(display)

end_of_game = False

while not end_of_game:

    guess = input("Choose a letter: ").lower()

    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1        
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(f"{''.join(display)}")
    print(stages[lives])

    if "_" not in display:
        end_of_game = True
        print("You win.")

