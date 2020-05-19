answer = input("20 + 40 = ")

if answer.isdecimal():
    if int(answer) == 60:
        print("Ви відповіли вірно!")
    else:
        print("На жаль, вам потрібно ще вчити математику!")
else:
    print("Ви взагалі ввели не число. У вас кіт на руках чи що?")
