import csv
import random

# from .models import *

with open('data.csv', 'r', encoding="utf-8") as file:
    reader = csv.reader(file)
    i = 1
    for row in reader:
        print(random.random())
        # Employees.objects.create(subdivision=i, role=1, full_name=row[0], salary=row[1])
        print(row)


a = {}
a["1"] = 2
print(a)
