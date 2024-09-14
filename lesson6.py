all_products={'Весь склад':{'Продукты': 'Молоко'}}
admin= input('Что вы хотите сделать? ')
if admin == 'Добавить':
    product_name = input('Введите название продукта: ')
    product_count = input('Введите количество: ')
    all_products['Весь склад'][product_name] = product_count
    print(all_products['Весь склад'])
elif admin == 'Продукты':
    print(all_products['Весь склад']['Продукты'])