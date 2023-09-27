# #Задача 1
# dictionary_1 = {'a': 300, 'b': 400}
# dictionary_2 = {'c': 500, 'd': 600}
# dictionary_1.update(dictionary_2)
# print(dictionary_1)
#Задача 2
# numbers = {"num_1" : 1, "num_2" : 2, "num_3" :3, "num_100" : 100}
# for key in numbers:
#     numbers[key] *=5
# print(numbers)
#Задача 3
# student = {"name" : "Askhat", "age" : 17}
# student["age"]*=2
# print(student)
#Задача 4
# student = {"name" : "Askhat", "age" : 17, "color": "white"}
# student["age"]=16
# print(student)
#Задача 5
# student = {"name" : "Askhat", "age" : 17}
# student.pop("age")
# print(student)
#Задача 6
# student = {"name" : "Askhat"}
# student.setdefault("address", "Западный анар")
# print(student)
#Задача 7
# def aziz():
#     user = input("Введите фразу: ")
#     ali = user.split()
#     ali1=[]
#     for word in ali:
#         ali1.append(word[0].upper())
#     ali2="".join(ali1)
#     print(ali2)
# aziz()
#Задача 8
# def user():
#     a="Money, money, money, it's always sunny, in the richmen's world".lower()
#     print("money: ", a.count("money"))
#     print("it's: ", a.count("it's"))
#     print("always: ", a.count("always"))
#     print("sunny: ", a.count("sunny"))
#     print("in: ", a.count("in"))
#     print("the: ", a.count("the"))
#     print("richmen's: ", a.count("richmen's"))
#     print("world: ", a.count("world"))
# user()
#Задача 9
# def user(word):
#     unique_letters=set()
#     for letter in word:
#         if letter in unique_letters:
#             return False
#         unique_letters.add(letter)
#     return True
# word1 = "apple"
# word2 = "danil"
# word3 = "ali"
# print(user(word1))
# print(user(word2))
# print(user(word3))


#Задача 10
# def b(a):
#     a_b =int(str(a)[::-1])
#     print (a_b)
# b(27)
 
 
#Дополнительное задание
# def user(): 
#     while True:
#         user = input("Можете задать вопрос : ")
#         if user.find("?")>=0:
#             print("Конечно!")
#         elif user.find("!")>=0:
#             print("Успокойся")
#         elif user == "":
#             print("Как классно, Когда ты молчишь. Продолжай в том же духе!")
#         else:
#             print("Ну и что")
# user()
