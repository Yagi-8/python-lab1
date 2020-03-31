"""
Напишите скрипт, который позволяет ввести с клавиатуры номер
дебетовой карты (16 цифр) и выводит номер в скрытом виде: первые и
последние 4 цифры отображены нормально, а между ними – символы
«*» (например, 5123 **** **** 1212)
"""

#s = input('введите число:')
#a=s.split(' ')
a = [int(s) for s in input().split()]
print(a)
i=0
#for item in enumerate(a):
#    print(item,end='')

#for item in a:
while i<len(a):
    if a[i] < a[4]:
        print(a[i])
    if a[i]>a[3] and a[i]<a[12]:
        print('*')
    if a[i]>a[11] and a[i]<a[15]:
        print(a[i])
    i+=1
