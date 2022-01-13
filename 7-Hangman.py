from dis import dis
import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_as_list = list(chosen_word)
#Testing code
print(f'Pssst, the solution is {chosen_word}.')

display = []

for i in chosen_word:
    display.append("_")

print(display)
#print(len(chosen_word))



while display != word_as_list:
    guess = input("Guess a letter: ").lower()

    for dis_num in range(len(chosen_word)): #loops the number of times as there are letters in the chosen word from the list
        letter = chosen_word[dis_num] #starting at the first letter of the chosen word, will check the index (chosen_word[the current letter of that word])
        if letter == guess: # if the letter and guess match
            display[dis_num] = guess #then the display[] index will change to match the letter at that position

    print(display)

print("Game Over")