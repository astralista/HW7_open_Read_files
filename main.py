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

# есть проблемка:
# вот этот код может отсортировать файлы по размеру(что мне и нужно),
# но в список они сохраняются без указания папки

# list_of_files = filter(lambda x: os.path.isfile(os.path.join('sorted', x)), os.listdir('sorted'))
# list_of_files = sorted(list_of_files, key=lambda x: os.stat(os.path.join('sorted', x)).st_size)


# а вот этот код после того как добавить после join название папки
# пишет полный путь, но в таком варианте у меня не работает сортировка
# помогите разобраться что написать в import os чтобы код выше работал

inputs = []
for file in os.listdir('sorted'):
    if file.endswith('.txt'):
        inputs.append(os.path.join('sorted', file))

with open('merged_file.txt', 'w') as outfile:
    for fname in inputs:
        with open(fname, encoding="utf-8", errors='ignore') as infile:
            count = int()
            for line in infile:
                count += 1
            infile.seek(0)
            text = infile.read()
            outfile.writelines(f'{fname}\n{count}\n{text}\n')