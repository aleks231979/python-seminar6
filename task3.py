# Задача
# Измените код одной-двух решенных ранее задач (с прошлых семинаров или домашних работ),
# применив лямбды, filter, map, zip, enumerate, списочные выражения.

# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# [1, 2, 2, 3, 4]  -> [1, 3, 4]

user = [1, 2, 2, 3, 4]
res = list(filter(lambda x: user.count(x) == 1, user))
print(res)