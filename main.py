# Содержимое файла с рецептами
content = '''Омлет
3
Яйцо | 2 | шт
Молоко | 100 | мл
Помидор | 2 | шт

Утка по-пекински
4
Утка | 1 | шт
Вода | 2 | л
Мед | 3 | ст.л
Соевый соус | 60 | мл

Запеченный картофель
3
Картофель | 1 | кг
Чеснок | 3 | зубч
Сыр гауда | 100 | г

Фахитос
5
Говядина | 500 | г
Перец сладкий | 1 | шт
Лаваш | 2 | шт
Винный уксус | 1 | ст.л
Помидор | 2 | шт'''

from typing import Dict, List


def read_cookbook(filename='recipes.txt'):
    """
    Читает рецепты из файла и возвращает словарь cook_book

    :param filename: Имя файла с рецептами
    :return: Словарь с рецептурой блюд
    """
    with open(filename, encoding="utf8") as file:
        cook_book = {}

        while True:
            # читаем название блюда
            dish_name = file.readline().strip()

            if not dish_name:
                break

            # читаем количество ингредиентов
            num_ingredients = int(file.readline())

            ingredients = []

            for _ in range(num_ingredients):
                ingredient_line = file.readline().strip()
                name, quantity, measure = map(str.strip, ingredient_line.split('|'))
                ingredients.append({
                    'ingredient_name': name,
                    'quantity': int(quantity),
                    'measure': measure
                })

            # добавляем блюдо в cook_book
            cook_book[dish_name] = ingredients

            # пропускаем пустую строку между рецептами
            file.readline()  # пропускаем пустую строку перед следующим блюдом

    return cook_book


# Проверяем работу функции чтения рецепта
if __name__ == "__main__":
    cook_book = read_cookbook('recipes.txt')
    print(cook_book)


def get_shop_list_by_dishes(dishes, person_count=1):
    """
    Формирует список продуктов для выбранных блюд и указанного числа персон

    :param dishes: Список блюд
    :param person_count: Кол-во персон
    :return: Словарь необходимых продуктов
    """
    shop_list = {}

    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                ingredient_name = ingredient['ingredient_name']
                total_quantity = ingredient['quantity'] * person_count

                if ingredient_name in shop_list:
                    # Если продукт уже есть в списке, увеличиваем его количество
                    shop_list[ingredient_name]['quantity'] += total_quantity
                else:
                    # Иначе создаем новый элемент
                    shop_list[ingredient_name] = {
                        'measure': ingredient['measure'],
                        'quantity': total_quantity
                    }

    return shop_list


# Тестируем функцию формирования списка покупок

if __name__ == "__main__":
    result = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
    print(result)

    import os


    def merge_files_into_one(files, output_file='result.txt'):
        """
        Объединяет файлы в один согласно правилу сортировки по числу строк

        :param files: Список имен файлов
        :param output_file: Имя итогового файла
        """
        file_data = []

        for file in files:
            with open(file, encoding="utf8") as f:
                lines = f.readlines()
                line_count = len(lines)
                file_data.append((file, line_count, ''.join(lines)))

        # Сортируем файлы по количеству строк
        sorted_files = sorted(file_data, key=lambda x: x[1])

        with open(output_file, mode='w', encoding="utf8") as merged_file:
            for file_name, line_count, content in sorted_files:
                merged_file.write(f"{file_name}\\n")
                merged_file.write(f"{line_count}\\n")
                merged_file.write(content)
                merged_file.write("\\n")  # Добавляем пустую строку между файлами


    # Пример запуска объединения файлов
    if __name__ == "__main__":
        input_files = ['1.txt', '2.txt']
        merge_files_into_one(input_files)












