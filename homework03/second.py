n = int(input("Введите размер массива: "))
a = list()

for i in range(n):
    a.append(int(input(f'Введите {i + 1} элемент массива: ')))
print("Массив: ", a)

x = int(input("Введите искомое число: "))

min_diff = float('inf')
closest = a[0]

for i in a:
    diff = abs(i - x)
    if diff < min_diff:
        min_diff = diff
        closest = i

print(f'Ближайшее к искомому числу стоит: {closest}')
