# a=lambda x:x**2
# print(a(10))
#


# b=lambda y,u: y+u
# print(b(2,3))


# x=lambda e:e
# print(x(9))

# a= lambda e: e*4
# print(a(int(input('Введите сторону квадрата: '))))
#
# a=lambda e: e*4
# side= int(input('Введите сторону кв:'))
# print(a(side))

# def alo(a,b=4):
#     print(a+b)
#
# alo(2)

# def spam(*args):
#     return args
# print(spam(1,2,3,4,5,6,7,8,9,10))

# def spam(*args):
# #     for a in args:
# #         print(a)
# #
# # spam(1,2,3,4,5,6,7,8,9,10)

# def spam(**kwargs):
#     for a,b in kwargs.items():
#         print(a,b)
# print(spam(name='Abubi',age='24'))

def chislo():
    a=(int(input('Введите число: ')))
    if a%2 == 0:
        print('True')
    elif a%2!=0:
        print('False')
        return a

print(chislo)