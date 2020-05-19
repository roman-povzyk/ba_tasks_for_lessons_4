main_line = input("Введіть свій рядок: \n")
delete_word = input("Введіть слово, яке треба видалити: \n")

new_main_line = main_line.replace(delete_word, "*")
print(new_main_line)

