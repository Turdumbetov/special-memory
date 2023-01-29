summa = 0
for number in range(0, 1000):
    if number % 2 == 0 or number % 3 == 0 and number % 4 != 0:
            print(number)
            summa += number
