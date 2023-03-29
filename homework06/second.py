import random

numbers = [random.randint(-100, 100) for _ in range(20)]

print("Сгенерированный список:", numbers)

min_num = int(input("Введите минимальное число: "))
max_num = int(input("Введите максимальное число: "))

print("Числа в диапазоне от", min_num, "до", max_num, ":")
for num in numbers:
    if min_num <= num <= max_num:
        print(num)
