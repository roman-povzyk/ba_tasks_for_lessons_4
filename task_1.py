import random

while True:

    user_number = input("Введіть число від 1 до 10\n")
    comp_number = random.randint(1, 10)

    if user_number.isdecimal():
        if int(user_number) < 1 or int(user_number) > 10:
            print("Ваше число не відповідає правилам!\n")
        elif int(user_number) == comp_number:
            print("Вітаємо, ви вгадали!\n")
        else:
            print(f"На жаль, ви не вгадали! Це число {comp_number}\n")
    else:
        print("Ви ввели не число, тому не зіграєте\n")


