a = int(input())
b = int(input()) 
summa = 0 
co_3 = 0 
for i in range (a, b+1):
    if i%3 == 0:
        summa = summa + i
        co_3 += 1  
print (summa/co_3)