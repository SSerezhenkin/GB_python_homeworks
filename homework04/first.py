n = int(input("Введите количество элементов первого множества: "))
m = int(input("Введите количество элементов второго множества: "))

set1 = set(int(input("Первое множество: ")) for i in range(n))
set2 = set(int(input("Второе множество: ")) for i in range(m))

common_elements = sorted(set1.intersection(set2))

print("Общие элементы в порядке возрастания: ", common_elements)