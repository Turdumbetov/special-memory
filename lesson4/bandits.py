count_bandits = int(input("Введите количество преступников: "))
if count_bandits <= 5:
    print("Я смогу сам!")
elif count_bandits >= 5 and count_bandits <= 10:
    print("Помоги мне Бэтмен")
else:
    print("Удачи тебе!")    