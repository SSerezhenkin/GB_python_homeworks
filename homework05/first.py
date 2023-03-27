a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

def power(a, b):
    if b == 0:
        return 1
    else:
        return a * power(a, b-1)

result = power(a, b)
print(f"{a} в степени {b} равно {result}")