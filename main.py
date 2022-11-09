with open('recipes.txt', 'rt') as file:
    cook_book = []
    for line in file:
        a = line.strip()
        b = int(file.readline())
        ingridients = []
        for _ in range(b):
            c = file.readline().split(' | ')
            ingredient_name, quantity, measure = c
            ingridients.append({'ingredient_name': ingredient_name,
                                'quantity': quantity,
                                'measure': measure
                                })
            file.readline()
            cb = {'name': a,
             'ingr_count': b,
             'ingridients': ingridients}

            cook_book.append(cb)
    # a = file.readline()
    # b = int(file.readline())
    # c = file.readline().split(' | ')
print(cook_book)
# with open('recipes.txt', 'rt') as file:
#     content = file.read()
#     print(content)