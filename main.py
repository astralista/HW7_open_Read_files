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

def get_shop_list_by_dishes(dishes, count):
    dishes_list = {}
    for dish in dishes:
        if dish in cook_book:
            ingrs = cook_book.get(dish)
            for x in ingrs:
                ingrs = list(x.values())
                name, measure, quantity = ingrs
                dishes_list.update({name: {'measure': int(measure)*count,
                                           'quantity': quantity}})

    return dishes_list

print(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2))