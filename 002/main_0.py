# v. 1.0
# 10.01.2018
# Sergii Mamedov

first = 1
second = 2
summa = 2
while second < 4000000:
    next = first + second
    first = second
    second = next
    if second % 2 == 0:
        summa += next

print(summa)
