groupmates = [
    {
        "name": u"Арина",
        "group": "2256",
        "age": 23,
        "marks": [4, 5, 4, 5, 4]
    },
    {
        "name": u"Иван",
        "group": "2256",
        "age": 24,
        "marks": [4, 3, 2, 3, 4]
    },
    {
        "name": u"Алексей",
        "group": "2255",
        "age": 25,
        "marks": [5, 5, 3, 5, 5]
    },
    {
        "name": u"Елизавета",
        "group": "2255",
        "age": 22,
        "marks": [4, 3, 5, 5, 5]
    },
    {
        "name": u"Кристина",
        "group": "2255",
        "age": 24,
        "marks": [2, 5, 4, 3, 5]
    }    
]

def print_students(students):
    print (u"Имя студента".ljust(15), \
          u"Группа".ljust(8), \
          u"Возраст".ljust(8), \
          u"Оценки".ljust(20))
    for student in students:
        print (\
              student["name"].ljust(15), \
              student["group"].ljust(8), \
              str(student["age"]).ljust(8), \
              str(student["marks"]).ljust(20))
        print ("\n")

def filter_students_by_average_mark(students, min_average):
    filtered_students = []  # пустой массив для отфильтрованных студентов
    for student in students:
        # Вычисляем среднюю оценку текущего студента
        marks = student["marks"]
        average_mark = sum(marks) / len(marks)
        # Сравниваем с заданным значением
        if average_mark > min_average:
            filtered_students.append(student)  # добавляем студента, если прошел фильтрацию
    return filtered_students


# Вывод в консоль:
print("Все студенты:")
print_students(groupmates)

print("\nСтуденты со средней оценкой выше 4.5:")
filtered = filter_students_by_average_mark(groupmates, 4.5)
print_students(filtered)

print("\nСтуденты со средней оценкой выше 4.0:")
filtered = filter_students_by_average_mark(groupmates, 4.0)
print_students(filtered)