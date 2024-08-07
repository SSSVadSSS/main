grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
# Сначала создадим новый список, который будет состоять
# из средних оценок вычисляемых по исходному списку элементов
a = len(grades) # Длина исходного списка
median_grades = [] # Вычислим cписок для средних значений оценок учеников
for i in grades:
    a = grades.index(i)
    median_grades.append(float(sum(grades[a])/len(grades[a])))
    # Получаем список средних оценок - median_grades
    # Каждый элемент нового списка образуется путем сложения чисел в исходных элементах и
    # делением результата на количество оценок в текущем элементе перебора по списку grades
#print(median_grades)
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
# Преобразуем множество элементов с именами учеников в список:
students = list(students)
# Сортируем элементы списка по алфавиту
students = sorted(students)
#print(students)
# Создаем словарь, объединяя два списка, где ключи будут
# имена из списка students, а значения из списка median_grades
successfully = dict(zip(students, median_grades)) #Итоговый словарь, полученный объединением.
print(successfully)
