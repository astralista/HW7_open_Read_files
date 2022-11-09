with open('recipes.txt', 'rt') as file:
    cook_book = []
    for line in file:
        recipe_name = line.strip()
        ingr_count = int(file.readline())
        ingridients = []
    #     for _ in range(ingr_count):
    #         ingr = file.readline().split(' | ')
    #         ingredient_name, quantity, measure = ingr
    #         ingridients.append({'ingredient_name': ingredient_name,
    #                             'quantity': quantity,
    #                             'measure': measure
    #                             })
    #         file.readline()
    #         cb = {'name': recipe_name,
    #          'ingr_count': ingr_count,
    #          'ingridients': ingridients}
    #
    #         cook_book.append(cb)
        ing = file.readline().split(' | ')
        ingredient_name, quantity, measure = ing
    print(ing)

# with open('recipes.txt', 'rt') as file:
#     content = file.read()
#     print(content)