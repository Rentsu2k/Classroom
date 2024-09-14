# def create_list():
#     my_list=[]
#     return my_list
#
# a=create_list()
# a.append(5)
# print(a)

# def f(x):
#     return 2 * x + 3
#
# print(f(5))

#icanhazip.com

import requests
while True:
    url='https://httpbin.org/post'
    data={'custname': 'Damir','custtel': '7777777','custemail': 'aboba@mail.ru','size': 'small','topping': 'bacon', 'delivery': '12:00','comments': 'POBISTREE!!!'}
    response=requests.post(url,data=data)
    print(response)

