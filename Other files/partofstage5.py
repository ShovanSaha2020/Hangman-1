random_word = 'kotlin'
dashdash = ['-' for i in range(len(random_word))]

user_input =  'k'
indices = []

#for determining all the position of the user_input in random_word
for position, value in enumerate(random_word):
    if random_word[position] == user_input:
        indices.append(position)


#inserting the user_input on dashdash in the positions where it
#  is found in the random_word
if user_input in random_word:
    for index, value in enumerate(indices):
        # print(indices[index])
        dashdash[indices[index]] = user_input
    print(''.join(dashdash))
    