print("Введите размер шоколадки: N x M")
n = int(input("N >> "))
m = int(input("M >> "))
k = int(input("А теперь сколько долек вы хотите отломить за 1 раз >> ")) 
min = 0
max = n*m
if n<m:
    min = n
elif n>m:
    min = m
else:
    min = n

if min<=k<=max:
    if min%k==0 or max%k==0:
        print(f"{n} {m} {k} -> yes")
    else:
        print(f"{n} {m} {k} -> no")
else:
    print(f"{n} {m} {k} -> no")