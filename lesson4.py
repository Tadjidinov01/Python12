# # # Типы данных (4)
# # # integer,  =float , bool, string
# # # list - списки
# # name1 ="Nurbolot"
# # name2 ="Syimik"
# # name3 = "Islam"
# # print(name1, name2, name3) 

# # names = ["Nurbolot","Syimik","Islam"]
# # print(names)

# # numbers = [10,20,30,40,50]
# # print(numbers)
# # #integer   string        float   bool 
# # lst = [10, "Hello World", 0.1, True]
# # print(lst)

it_company = ["Google", "Meta", "Amazon"]
print(it_company)
# it_company.append("Starlink")# Метод Добавелние в конец списка
# print(it_company)
it_company.remove ("Meta")# Метод удаление из списка по значению
# print(it_company)
# print(it_company[0])
# it_company[1]= "Geeks" # Таким образом можно обновить значение из списка
# print(it_company)
# it_company.insert(0, "Codex")#Добавляет значенин по индексуу
# print(it_company)
# it_company.pop(3)#метод удаляет значение по индексу

# cities =["Bishkek","Osh","Batken","Talas","Naryn"]
# print(cities[::-1])
# print(cities[1:4])# Срезы в списках list
# del cities[1,4] # Удалаяем значения по срезам с помощью операторов del
# print(cities)

# cars = ["Bmw", "Tesla","Zeekr", "Toyota"]
# print(cars)
# print(cars[1][2])
# numbers = [10,1,3,4,88,0.1,90]
# print(numbers)
# numbers.sort() # Отсортировать список
# numbers.sort(reverse=True)# Отсортировать в обратном порядке
# print(numbers)


# # Tuple - кортежи
# computers = ('Asus','Acer','Hp','Huawei')
# print(computers)
# print(computers.index('Hp'))
# print(computers.count('Acer'))
# print(computers[0])
# print(computers[1:2])

# tup =(20,1.01, "Geeks",True,(10,20,30),[10,20,30])
# # print(tup)

# contact =["112"]
# user_contact = input("Введите контакт:")
# if user_contact in contact:
#     print(user_contact, "есть в списке")
# else:
#     print(user_contact, "нету в списке")

# my_contact = ["MCHS"]
# while True:
#     command = input("1-посмотреть контакты, 2-добавить, 3-удалить: ")
#     if command =="1":
#         print(my_contact)
#     elif command =="2":
#         add_contact = input("Контакт: ")
#         my_contact.append(add_contact)
#         print(add_contact, "Успешно добавлен")
#     elif command =="3":
#         remove_contact = input("Контакт которого вы хотите удалить: ")
#         if remove_contact in my_contact:
#             my_contact.remove(remove_contact)
#             print(remove_contact, "успешно удален")
#         else:
#             print(remove_contact, "нету в списке контактов")
#     else:
#         print("Такой команды нету")