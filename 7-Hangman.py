import random

word_list = ["aardvark", "baboon", "camel"]


chosen_word = random.choice(word_list)

word = ""

print(chosen_word)

guess = input("Choose a letter: ").lower()

num = 0

for letter in chosen_word:
    if letter == guess:
        print("yes")
    else:
        print("no")
    num += 1