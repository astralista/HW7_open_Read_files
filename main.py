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

inputs = []
lenth1 = sum(1 for line in open('sorted/1.txt', 'r'))
print(lenth1)

for file in os.listdir('sorted'):
    if file.endswith('.txt'):
        inputs.append(os.path.join('sorted', file))

print(inputs)
with open('merged_file.txt', 'w') as outfile:
    for fname in inputs:
        with open(fname, encoding="utf-8", errors='ignore') as infile:

            outfile.writelines(f'\n{fname}\n')
            outfile.writelines(f'{lenth1}\n')
            outfile.write(infile.read())