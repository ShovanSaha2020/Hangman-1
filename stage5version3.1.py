import random

word_list = ['python', 'java', 'kotlin', 'javascript']
random_word = random.choice(word_list)
dashdash = ['-' for i in range(len(random_word))]


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

        for index, value in enumerate(indices):
            dashdash[value] = user_input1

    return ''.join(dashdash)


print("H A N G M A N")

count = 0
while True:
    count = count + 1

    print()
    revealed_word = word_revealer()
    print(revealed_word)
    # print(count)
    user_input = input("Input a letter: ")
    revealed_word = word_revealer(user_input)

    if user_input in random_word and count < 8:
        continue

    if user_input not in random_word:
        print("No such letter in the word")

    if count == 8:
        print()
        print("Thanks for playing!")
        print("We'll see how well you did in the next stage")
        break
