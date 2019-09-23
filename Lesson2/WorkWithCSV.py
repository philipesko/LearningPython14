import csv


# Задание
# Создайте список словарей:
#         [
#         {'name': 'Маша', 'age': 25, 'job': 'Scientist'},
#         {'name': 'Вася', 'age': 8, 'job': 'Programmer'},
#         {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
#     ]
# Запишите содержимое списка словарей в файл в формате csv

listdictionary =  [
        {'name': 'Маша', 'age': 25, 'job': 'Scientist'},
        {'name': 'Вася', 'age': 8, 'job': 'Programmer'},
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
    ]

with open('export.csv', 'w', encoding='utf8', newline='') as f:
    fields = ['name', 'age', 'job']
    writer = csv.DictWriter(f, fields)
    writer.writeheader()
    for data in listdictionary:
        writer.writerow(data)

# for dictionary in listdictionary:
#     #val_from_di = dictionary.key()
#     list_for_writing = []
#     list_for_writing.append(dictionary['name'])
#     list_for_writing.append(dictionary['age'])
#     list_for_writing.append(dictionary['job'])
#     print(list_for_writing)
#     for row in list_for_writing:
#         writer.writerow(row)


f.close()








