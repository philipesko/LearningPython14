from Lesson1.sale import *
import random

for phone in stock:
    phone['price_final'] = discounted(phone["price"], phone["discount"], name='phone')

print(stock)

# Home mission:

# Создать список из десяти целых чисел.
# Вывести на экран каждое число, увеличенное на 1.

dict = []
for value in range(0, 50, 5):
    dict.append(value)

# Show list
print(dict)

dictResult = []
for sum in dict:
    dictResult.append(int(sum) + 1)

print(dictResult)  # show eresult dict + summ

# -------------------------------------------
# Цикл
# Ввести с клавиатуры строку.
# Вывести эту же строку вертикально: по одному символу на строку консоли.

inString = list(input("please input string: "))
for show in inString:
    print(show)

# Оценки
# Создать список из словарей с оценками учеников разных классов школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
# Посчитать и вывести средний балл по всей школе.
# Посчитать и вывести средний балл по каждому классу.


# school_classes = list()# create list for school_classes
# for classes in range(1, 12):
#     school_classes.append(str(classes) + 'a')
#     school_classes.append(str(classes) + 'b')
#     school_classes.append(str(classes) + 'c')
#
# child_list = list()
# scores_list = list()
# for clsses_count in range(len(school_classes)):
#
#     for child_count in random(3, 7):
#         child_list.append(child_count)
#             for scores in random (2, 6):
#                 scores_list.append(scores)
#
#
# print(child_list)
# print(scores_list)






# scores = list()
# for classCount in range(len(school_class)):
#     for scoresFormClasses in range(random.randint(10, 25)):
#         scores.append(random.randint(1, 6))
#     school['scores'] = scores


print(school)
