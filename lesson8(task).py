from fileinput import close

clients = {}
opened_room = [i for i in range(1,41)]
closed_rooms = []
def dobavit():
    name = input('Введите ваше имя')
    room = int(input('Введите номер комнаты: '))
    if room in closed_rooms:
        print('Номер занят')
    elif room not in opened_room:
        print('Номер успешно забронирован!')
        closed_rooms.append([name][room])
        return(name,room)
def udalit():
    name= input('Введите ваше имя: ')
    if name in closed_rooms:
        closed_rooms.pop(name)
        print('Готово')
while True:
    usluga=input('Выберите услугу: Добавить/Удалить/Увидеть занятые номера ')
    if usluga== 'Добавить':
            dobavit()




