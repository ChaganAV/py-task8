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

# В 8 задаче можно также проверить, что пользователь ввел число равное сразу размеру всей плитки - ломать не придется!

# while True:
#     try:
#         n = int(input("Введите длину шоколадки: "))
#         m = int(input("Введите ширину шоколадки: "))
#         k = int(input("Введите количество кусочков: "))
#         if k < m * n:
#             if (k % m == 0 or k % n == 0):
#                 print(f'Можно ломать!')
#                 break
#         elif k == m * n:
#             print('Ломать не нужно! Забирайте целиком!')
#             break
#         else:
#             print('Столько кусочков нет!')
#             break
#     except:
#         print('Некорректный ввод. Попробуйте еще раз!') 