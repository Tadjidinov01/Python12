# #Задание 1
# a = 10
# b = 20
# if a>b: 
#     print("число a больше")
# if a<b: 
#     print("число b больше")
# else:
#     print("Они равны")
    
# #Задание 1,2
# n = int(input("Введите число: "))
# if n>0:
#     print("Число положительное")
# if n<0:
#     print("Число отрицательное")
# else:
#     print("Число равно 0")


# Задание 1.5
# a = int(input("Введите чило: "))

# if a < 0:
#     a =-a
# print(a)
    

# Задание 2
# a = int(input("Введите число:"))
# b = int(input("Введите число:"))
# if(a==b):
#     print("Yes")
# else:
#     print("No")


# # Задание 3
# a=int(input("Введите число:"))
# if a>100 or a< -100:
#     print("-")
# else:
#     print("+")

# Задание 4
# month = int(input("Введите номер месяца: "))

# if month <= 0 or month > 12:
#     print("Некорректный номер месяца")
# elif month <= 2 or month == 12:
#     print("Зима")
# elif month <= 5:
#     print("Весна")
# elif month <= 8:
#     print("Лето")
# elif month <= 11:
#     print("Осень")

# #Задание 5
# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# d = int(input("Введите третье число: "))
# if (a+b+d)>=10:
#     print("yes")
# else:
#     print("no")

# #Задание 6
# num1 = 20
# num2 = 10
# num3 = 30

# a=0

# if num1 > 0:
#     a += 1

# if num2 > 0:
#     a += 1

# if num3 > 0:
#     a += 1
# print(a)

# #Задание 7
# years =int(input("Введите количество лет:" ))
# months =int(input("Введите количество месяцев: "))
# total = years * 12+months
# result = total*29
# print(result)

#Задание 8
age = int(input("Введите возраст в алмазах: "))

if age < 16:
    print("Еще рано")
elif age >= 18 and age < 40:
    print("Идем служить")
elif age >= 40:
    print("Уже не надо")
