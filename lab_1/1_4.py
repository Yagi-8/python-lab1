"""

Напишите скрипт, который разделяет введенный с клавиатуры текст на
слова и выводит сначала те слова, длина которых превосходит 7
символов, затем слова размером от 4 до 7 символов, затем – все
остальные.
"""


string=input('введите текст ')
print('вся строка: ',string)
str7=string[0:7]
print('str7: ',str7)
str4=string[7:12]
print('str4: ',str4)
str5=string[12:17]
print('str5: ',str5)
str6=string[17:23]
print('str6: ',str6)
str77=string[23:31]
print('str77: ',str77)
str_all=string[31:len(string)]
print('остаток: ',str_all)
print(str7,'+',str4,'+',str5,'+',str6,'+',str77,'+',str_all)
import random

print('ИЛИ ')
str7=string[0:7]
print('str7: ',str7)
n=random.randint(4,7)
b=int(n)
strr=string[7:7+b]
print('число: ',b,'слово: ',strr)
str_all=string[7+b:len(string)]
print('остаток: ',str_all)
print(str7,'+',strr,'+',str_all)