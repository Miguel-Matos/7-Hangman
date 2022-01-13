from dis import dis
import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_as_list = list(chosen_word)
#Testing code
#print(f'Pssst, the solution is {chosen_word}.')


lives = 6
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

display = []

for i in chosen_word:
    display.append("_")

print(display)
#print(len(chosen_word))

end_game = False

while not end_game:
    print(f"Lives: {lives}")
    print(stages[lives])
    print(display)
    
    guess = input("Guess a letter: ").lower()

    for dis_num in range(len(chosen_word)): #loops the number of times as there are letters in the chosen word from the list
        letter = chosen_word[dis_num] #starting at the first letter of the chosen word, will check the index (chosen_word[the current letter of that word])
        if letter == guess: # if the letter and guess match
            display[dis_num] = guess #then the display[] index will change to match the letter at that position
    
    if guess not in display:
        lives -= 1
    
    

    if display == word_as_list:
        end_game = True
        print("You win!")
    elif lives == 0:
        end_game = True
        print("You lose!")
    
