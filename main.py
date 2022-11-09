# with open('recipes.txt', 'rt') as file:
#     cook_book = []
#     for line in file:
#         a = line.strip()
#         b = int(file.readline())
#         ingridients = []
#         for _ in range(b):
#             c = file.readline().strip().split(' | ')
#             ingredient_name, quantity, measure = c
#             ingridients.append({'ingredient_name': ingredient_name,
#                                 'quantity': quantity,
#                                 'measure': measure})
#             file.readline()
#             cb = {'name': a,
#              'ingr_count': b,
#              'ingridients': ingridients}
#
#             cook_book.append(cb)
# print(cook_book)


with open('recipes.txt', 'rt') as file:
    departments = []
    for line in file:
        department_name = line.strip()
        employees_count = int(file.readline())
        employees = []
        for _ in range(employees_count):
            emp = file.readline().strip().split(' | ')
            name, last_name, birth_date = emp
            employees.append({'name': name,
                              'last_name': last_name,
                              'birth_date': birth_date})
        file.readline()
        dep = {'name': department_name,
               'employees_count': employees_count,
               'employees': employees}
        departments.append(dep)

print(departments)

print('hello')