n = int(input("Введите размер массива: "))
a = list()

for i in range(n):
    a.append(int(input(f'Введите {i + 1} элемент массива: ')))
print("Массив: ", a)

x = int(input("Введите искомое число: ")) 
count = 0

for i in a:
    if i == x:
        count += 1

print(f'Искомое число встречается в массиве {count} раз(а)')
