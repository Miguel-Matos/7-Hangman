from dis import dis
import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

display = []

for i in chosen_word:
    display.append("_")

print(display)
#print(len(chosen_word))

guess = input("Guess a letter: ").lower()

for dis_num in range(len(chosen_word)): #loops the number of times as there are letters in the chosen word from the list
    letter = chosen_word[dis_num] #starting at the first letter of the chosen word, will check the index
    if letter == guess: # if the letter and guess match
        print("Right")
        display[dis_num] = guess #then the display[] index will change to match the letter at that position
    else:
        print("Wrong")

print(display)