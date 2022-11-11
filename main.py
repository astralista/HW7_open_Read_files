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
print(cook_book)

# def get_shop_list_by_dishes(dishes, count):
#     dishes_ingr = []
#
#     for dish in dishes:
#         for i in cook_book[dish]:
#             dishes_ingr.append(i)
#
#     for i in dishes_ingr:
#         i['quantity'] = int(i['quantity']) * count
#         up = {**i[0], **i[1]}
#     return up

def get_shop_list_by_dishes(dishes, count):
    dishes_ingr = {}
    for dish in dishes:
        if dish in cook_book:
            

print(get_shop_list_by_dishes(['Омлет', 'Запеченный картофель'], 1))