new_task = int(input())
bandits = 5
print("Пойти одному или вызвать супергероя?")
if bandits < 5:
    print("Я смогу сам!")
elif bandits > 5:
    print("Помоги мне Бэтмен!")
else:
    print("Удачи тебе!")