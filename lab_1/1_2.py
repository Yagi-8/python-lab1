"""

Написать скрипт, который выводит на экран «True», если элементы
программно задаваемого списка представляют собой возрастающую
последовательность, иначе – «False».
"""

#num[]=input('Введите последовательность')
num=[1,2,3,4,5]
a=0
for item in num:
    if item<item+1:
        print('True')
    else:
        print('False')
        print(item)
        #print('test: ',a)
    