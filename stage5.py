import random

word_list = ['python', 'java', 'kotlin', 'javascript']
random_word = random.choice(word_list)
print("H A N G M A N")

dashdash = ['-' for i in range(len(random_word))]

def word_revealer(user_input=None):
    global dashdash
    indices = []
    if user_input:
        # for determining all the position of the user_input in random_word
        for position, value in enumerate(random_word):
            if random_word[position] == user_input:
                indices.append(position)

        # inserting the user_input on dashdash in the positions where it
        #  is found in the random_word

        for index, value in enumerate(indices):
            # print(indices[index])
            dashdash[indices[index]] = user_input

    return ''.join(dashdash)


count = 1
while True:
    print()
    print(word_revealer())
    user_input = input("Input a letter: ")
    

    if user_input in random_word:
        revealed_word = word_revealer(user_input)
        print(revealed_word)
    elif user_input not in random_word:
        print("No such letter in the word")

    if count == 8:
        print()
        print("Thanks for playing!")
        print("We'll see how well you did in the next stage")

    count = count + 1
