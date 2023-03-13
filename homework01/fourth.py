print('Ломаем шоколадку')
n = int(input('Размер шоколадки n: '))
m = int(input('Размер шоколадки m: '))
k = int(input('Количество долек k: '))
if k < n * m and ((k % n == 0) or (k % m == 0)):
    print('Можно')
else:
    print('Нельзя')
