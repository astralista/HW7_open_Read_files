import os

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
                dishes_list.update({name: {'measure': int(measure) * count,
                                           'quantity': quantity}})

    return dishes_list
# print(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2))

list_of_files = filter(lambda x: os.path.isfile(os.path.join('sorted', x)), os.listdir('sorted'))
list_of_files = sorted(list_of_files, key=lambda x: os.stat(os.path.join('sorted', x)).st_size)

inp = []
for i in list_of_files:
    inp.append(os.path.join('sorted', i))

with open('merged_file.txt', 'w') as outfile:
    for fname in inp:
        with open(fname, encoding="utf-8", errors='ignore') as infile:
            count = int()
            for line in infile:
                count += 1
            infile.seek(0)
            text = infile.read()
            outfile.writelines(f'{fname}\n{count}\n{text}\n')