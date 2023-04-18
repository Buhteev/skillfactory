total = 0
n = int(input('Введите количество билетов, которое хотите купить: '))
for i in range (n):
    print ('Введите возраст ', i+1, 'покупателя:', end = ' ')
    age = int(input())
    if age < 18:
        total += 0
    elif 18<= age <= 25:
        total +=990
    else:
        total +=1390
    print ('Общая стоимость билетов на текущий момент - ', total)

if n >= 3:
    print ('Стоимость билетов со скидкой составляет - ', total-total*0.1)
else:
    print ('Стоимость билетов составляет - ', total)

