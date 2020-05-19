import random

computer_number = random.randint(1, 10)
user_number = input("Введіть число від 1 до 10\n")

if user_number.isdecimal():
    if int(user_number) < 1 or int(user_number) > 10:
        print("Ваше число не відповідає правилам!")
    elif int(user_number) == int(computer_number):
        print("Вітаємо, ви вгадали!")
    else:
        print(f"На жаль, ви не вгадали! Це число {computer_number}")
else:
    print("Ви ввели не число, тому не зіграєте")


