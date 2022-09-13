# Задача 1. Сумма чисел

import os
count_sum = 0

user_file = open('numbers.txt', 'r')
for number in user_file:
    count_sum += int(number)
user_file.close()

new_file = open('answer.txt', 'w')
new_file.write(str(count_sum))
new_file.close()
