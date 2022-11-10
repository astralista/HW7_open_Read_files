with open('recipes.txt', 'r') as file:
    cook_book = {}
    for line in file:
        recipe_name = line.strip()
        ingr_count = int(file.readline())
        ingridients = []
        for _ in range(ingr_count):
            ingr = file.readline().strip().split(' | ')
            product, amount, unit = ingr
            ingridients.append({'ingredient_name': product,
                                'quantity': amount,
                                'measure': unit})
        file.readline()
        rcps = {recipe_name: ingridients}
        cook_book.update(rcps)

# print(cook_book)
#
#
#
def get_shop_list_by_dishes(dishes):
    dishes_ingr = {}
    for key in cook_book:
        if dishes == key:
            for i in cook_book[key]:
                for k in i[key]:
                    print(k)
    # return dishes_ingr

print(get_shop_list_by_dishes('Омлет'))

# print(cook_book['Омлет'][0])

