# class Mouse:
#     type = 'wireless'
#     name = 'G-pro-x'
#     color='pink'
#     max_dpi=10000
#
# print(Mouse.type)
#
# class Car:
#     def __init__ (self,model,colour,year):
#         self.model= model
#         self.colour=colour
#         self.year=year
#
# chevy=Car('Jentra','Black','2021')
# print(vars(chevy))

# class Comment:
#     def __init__(self,username,text,likes=0):
#         self.username=username
#         self.text=text
#         self.likes=likes
#
#     def post(self):
#         print('Комментарий опубликован!')
#
# social=Comment('MaoZe','DaJiaHao')
# social.post()

# class BankAccount:
#     def __init__(self,name, balance=0):
#         self.name=name
#         self.balance=balance
#
# def deposit(self,amount):
#     self.balance+=amount
#
# def cash(self,amount):
#     self.balance-=amount
#
# def check(self):
#     return self.balance
#
# sasha= BankAccount('Sanya')
# print(sasha.check())
# sasha.deposit(10)
# print(sasha.check())

class User:
    def __init__(self,name,mail,age,number):
        self.name=name
        self.mail=mail
        self.age=age
        self.number=number

    def change_name(self,new_name):
            self.name=new_name

    def changenumber(self,new_number):
            self.number=new_number

    def change_mail(self,new_mail):
            self.mail=new_mail

proverka=User('Aza','Sobaka@aza.ru','71','777777')
print(proverka.name)
proverka.change_name('Damir')
print(proverka.name)
proverka.changenumber('Azliddin@mail.ru')
print(vars(proverka))

