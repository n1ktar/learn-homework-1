"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""
phone_sold =  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]

def main(sold_number):
   
    sold_sum = 0
    for sold in sold_number:
      sold_sum += sold
    return sold_sum
    
all_sold_sum = 0

   
if __name__ == "__main__":
    for one_item in phone_sold:
     sold_sum = main(one_item['items_sold'])
     sold_avg =round(sold_sum / len(one_item['items_sold']))
     all_sold_sum += sold_sum 
     print(f'Суммарное колличество продаж {one_item["product"]}: {sold_sum}')
     print(f'Среднее колличество продаж {one_item["product"]}: {sold_avg}')

all_sold_avg = round(sold_sum / len(phone_sold))  
print(f'Cуммарное количество продаж всех товаров: {all_sold_sum}')
print(f'Среднее количество продаж всех товаров: {all_sold_avg}')