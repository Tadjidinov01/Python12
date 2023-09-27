#Модули - это python файл
#В python модули можно имортировать 3 способами
# import lesson8 #без окончания .py
# print(lesson8.hello())#Вызвываем функции их модули lesson8
# print(lesson8.three_add(10,10,10))

#2 - импортировать отдельные определения из модуля 
# from lesson8 import hello
# from lesson8 import three_add
# print(hello()) #вызываем функцию из другого модуля Python
# print(three_add(10, 10 ,10))
 
#3 - импортировать все содержимое модуля сразу
from lesson8 import * #оператор (*)означает все (весь)
print(hello())
print(three_add(5,5,5))
