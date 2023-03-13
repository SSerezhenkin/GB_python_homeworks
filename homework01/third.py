print('Счастливый билет')
ticket = input('Введите номер билета: ').strip()

if len(ticket) >= 6:
    if sum(list(map(int, ticket[:3]))) == sum(list(map(int, ticket[3:]))):
        print('Билет счастливый')
    else:
        print('Билет несчастливый')
else:
    print('Это не билетный номер')
