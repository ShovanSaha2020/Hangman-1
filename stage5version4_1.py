# Updated version 4_1 on 24th June, 2020

import random

word_list = ["python", "java", "kotlin", "javascript"]
random_word = random.choice(word_list)
dashdash = ["-" for i in range(len(random_word))]


def word_revealer(user_input1=None):
    global dashdash
    indices = []
    if user_input1:
        # for determining all the position of the user_input in random_word
        for position, value in enumerate(random_word):
            if value == user_input1:
                indices.append(position)

        # inserting the user_input on dashdash in the positions where it
        #  is found in the random_word

        for value in indices:
            dashdash[value] = user_input1


def status_printer():
    print("".join(dashdash))


print("H A N G M A N")
count = 1
while count < 9:
    print()
    status_printer()
    user_input = input("Input a letter: ")

    if user_input in random_word:
        word_revealer(user_input)

    elif user_input not in random_word:
        print("No such letter in the word")
    count = count + 1


print()
print(
    """Thanks for playing!
We'll see how well you did in the next stage"""
)

