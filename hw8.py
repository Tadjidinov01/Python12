# задание 1
from datetime import datetime

def get_time_difference():
    time_str1 = input("1-ввод (HH:MM:SS): ")
    time_str2 = input("2-ввод (HH:MM:SS): ")

    time_format = "%H:%M:%S"
    try:
        time1 = datetime.strptime(time_str1, time_format)
        time2 = datetime.strptime(time_str2, time_format)
    except ValueError:
        print("Ошибка: Неправильный формат времени. Используйте HH:MM:SS.")
        exit()
        

    if time1 > time2:
        print("Ошибка: Первая отметка времени должна быть раньше второй.")
    else:
        time_difference = time2 - time1
        seconds_difference = time_difference.total_seconds()
        print(f"Ответ: {int(seconds_difference)} секунд разницы.")
# get_time_difference()

# #задание 2
def average_grades(name, grades):
    average = sum(grades) / len(grades)
    
    print(f"Среднее арифметическое значение оценок для {name}: {average}")
# average_grades("Dior",[7,8,9,10,11,12])

