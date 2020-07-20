import random

word_list = ['python', 'java', 'kotlin', 'javascript']
random_word = random.choice(word_list)
print("H A N G M A N")


def hide_letters(random_word_1):
    x = random_word_1[0:3]
    y = (len(random_word_1) - 3) * '-'
    return f"{x}{y}"


answer = input(f"Guess the word {hide_letters(random_word)} ")
# print(f"|{random_word}|")
# print(f"|{answer}|")

if answer.strip() == random_word:
    print("You survived!")

else:
    print("You are hanged!")
