names = ['Азамат']
numbers = [123,234]
uslugi = ['Удалить', 'Cтоп']
delete = ()

funkciya = input('Выбереите нужную функцию: Имя/ Номер/ Услуга ')
while True:
        if funkciya == 'Имя':
            add=input('Введите Имя! ')
            names.append(add)
            print('Имя успешно добавлено! ')
            print(names)
            aza=input('Желаете продолжить? ')
            if aza=='Нет':
                break
        elif funkciya == 'Номер':
            add=input('Введите Номер! ')
            numbers.append(add)
            print('Номер успешно добавлен! ')
            print(numbers)
        elif funkciya == 'Услуга':
            print(uslugi)
            delete=input('Выберите Услугу ')
            if delete=='Удалить':
                print(numbers)
                input('Какой номер следует удалить? ')
                if delete in numbers:
                    remove.numbers(delete)
                    print(numbers)
            elif delete=='Стоп':
                break

