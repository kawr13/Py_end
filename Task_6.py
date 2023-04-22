# Задача 6: Вы пользуетесь общественным транспортом?
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.

# 1. Решение без цыкла

ticket = input("Введите номер билета: ")

if len(ticket) != 6: # Проверка номера на колличество символов
    print("Не корректный номер")
else:
    digit_sum_left = int(ticket[0]) + int(ticket[1]) + int(ticket[2])
    digit_sum_right = int(ticket[3]) + int(ticket[4]) + int(ticket[5])

    if digit_sum_left == digit_sum_right:
        print("Счастливый билет")
    else:
        print("Не счастливый билет")

# 2. Решение через цыкл for

# ticket = input("Введите номер билета: ")

# x = ticket[0:3]
# y = ticket[3:6]

# digit_sum_left  = 0
# digit_sum_right = 0

# for digit in x:
#     digit_sum_left += int(digit)
# for digit in y:
#     digit_sum_right += int(digit)
# if digit_sum_left == digit_sum_right:
#     print("Счастливый билет")
# else:
#     print("Не счастливый билет")





