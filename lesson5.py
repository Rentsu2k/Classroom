username = []
while True:
    abc= input('Введите юзернейм ')
    if abc not in username:
        print('Юзернейм создан')
        username.append(abc)
    elif abc in username:
        print('Юзернейм занят, попробуйте снова ')