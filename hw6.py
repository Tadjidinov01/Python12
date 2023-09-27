#Задание 1


#Задание 2
try:
    user_input = input("Введите строку, представляющую число: ")
    number = float(user_input)   
    print("Вы ввели число:", number)
except ValueError:
    print("Ошибка: Введенная строка не является числом.")
#Задание 3
text = input("Введите текстовую строку: ")
words = set(text.split())
unique_words = len(words)
print("Количество уникальных слов:", unique_words)
#Задание 4
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

set1 = set(list1)
set2 = set(list2)

common_elements = set1.intersection(set2)

print("Общие элементы, используя set:", common_elements)

frozen_set1 = frozenset(list1)
frozen_set2 = frozenset(list2)

frozen_common_elements = frozen_set1.intersection(frozen_set2)

print("Общие элементы, используя frozenset:", frozen_common_elements)