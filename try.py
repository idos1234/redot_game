#This file need to be removed

file = open('employees.txt', "r")
content = file.readlines()

employees = []

def separator(list):
    for item in list:
        item += '\n'
        employees.append(item)

separator(content)

file2 = open('data-base.txt', "a")

file2.writelines(employees)

file.close()
file2.close()