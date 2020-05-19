import random

main_word = input("Введіть ваше слово: \n")

for i in range(len(main_word)):
    new_word = ''.join(random.sample(main_word, len(main_word)))
    print(new_word)