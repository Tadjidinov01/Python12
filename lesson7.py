# # # # #Dictionary-словари
# # # # # Типы данных: list, tuple, int, str, float,bool, set, frozenset, dict
# # # # student = {"name":"Nurbolot", "age":19}
# # # # print(student)
# # # # print(student["name"])
# # # # print(student["age"])
# # # # student.setdefault("language", "Python")#метод для добавление в список
# # # # print(student)
# # # # student.pop("age")#метод удаления из списка по ключу
# # # # print(student)
# # # # student["language"]="java"#синтаксис для обновление значения по ключу
# # # # print(student)
# # # # print(student.keys()) #метод для получения для ключей из словаря
# # # # print(student.values())#метод для получения значений из словаря
# # # # print(student.items())#метод для получения ключча и значения за раз

# # # geeks ={"name":"geeks", "count_students": 340, "address":"Amatova 18"}
# # # print(geeks)
# # # for key,value in geeks.items():
# # #     print(key,value)
    
# # # dct = {}
# # # print(type(dct))

# # # contact = {"MCHS":112}
# # # while True:
# # #     command = input("1 - посмотреть, 2 - добавить, 3-Удалить, 4-обновить :")
# # #     if command == "1":
# # #         print(contact)
# # #     elif command =="2":
# # #         add_name = input("Имя: ")
# # #         add_number = input("Номер: ")
# # #         contact.setdefault(add_name, add_number)
# # #         print("Контакт", add_name, "Успешно добавлен")
# # #     elif command == "3":
# # #         remove_name = input("Кого удалить?")
# # #         contact.pop(remove_name)
# # #         print("Контакт", remove_name, "успешно удален")
# # #     elif command == "4":
# # #         update_name = input("кого обновить?")
# # #         update_number = input("Новый номер: ")
# # #         contact[update_name] = update_number
# # #         print("Номер контакта", update_name, "успешно обновлен на ",update_number)
# # #     else:
# # #         print("Такой комманды нету")
 
 
# # #Functions-Функции
# # # def hello():
# # #     print("Hello World")
# # # hello()
# # # hello()

# # def welcome():
# #     name = input("Имя: ")
# #     print("Привет", name)
# # # welcome()

# # def add():
# #     num1 = int(input("Первое число: "))
# #     num2 = int(input("Второе число: "))
# #     print(num1+num2)
# # add()

# def mult(num1,num2): #num1 и num2 являются параметрами функции MULT
#     print(num1 + num2)
# mult(5,3) #числа 5 и 3 являются аргуменатми функции
# mult(10, 100)
 
def div(num1, num2):
    try: 
        print(num1 / num2)
    except ZeroDivisionError:
        print("На ноль делить нельзя")
div(10, 5)
div(10, 0)