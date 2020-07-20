import random
import string

word_list = ["python", "java", "kotlin", "javascript"]
random_word = random.choice(word_list)
dashdash = ["-" for i in range(len(random_word))]
used_letter = []


def letter_revealer(user_input1=None):
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
    status = "".join(dashdash)
    return status


print("H A N G M A N")
mistake = 0
while True:
    print()
    print(status_printer())
    user_input = input("Input a letter: ")
    if len(user_input) != 1:
        print("You should input a single letter")

    elif user_input in used_letter:
        print("You already typed this letter")

    elif user_input not in string.ascii_lowercase:
        print("It is not an ASCII lowercase letter")

    elif user_input in random_word:
        # if user_input in used_letter:
        #     print("No improvements")
        #     mistake = mistake + 1
        # else:
        letter_revealer(user_input)
        # used_letter.append(user_input)

    elif user_input not in random_word:
        print("No such letter in the word")
        mistake = mistake + 1

    if status_printer() == random_word:
        print('You guessed the word!')
        print('You survived!')
        break

    if mistake == 8:
        print("You are hanged!")
        break

    used_letter.append(user_input)
