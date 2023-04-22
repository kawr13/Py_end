
# Задача 2: Найдите сумму цифр трехзначного числа с циклом.


# x = input("Введите трех значное число: ")
# x = str(x)
# if  len(x) != 3:
#     print("Числа не трехзначные")
# else:
#     result = int(x[0]) + int(x[1]) + int(x[2])   
#     print(result)


# Тренировался и сделал улучшенный вариант на проверку 3 х значного числа

while True:
    x = input("Введите трех значное число: ")
    if  len(x) != 3:
        print("Числа не трехзначные")
    else:
      x = str(x)
      result = int(x[0]) + int(x[1]) + int(x[2])
      break
print(result)





