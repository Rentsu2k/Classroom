# class Animal:
# #     def make_sound(self,s):
# #         print(s)
# #
# # class Horse(Animal):
# #     def galop(self):
# #         print('Begit')
# # pony = Horse()
# # pony.make_sound('НЫА')
# # begit= Horse()
# # begit.galop()
    #
    # class Parents:
    #     def FamilyPart(self):
    #         print('s')
    #
    # class Children(Parents):
    #     def NewGeneration(self):
    #         print('b')
    #
    # older=Children()
    # older.NewGeneration()

# class Car:
#     def __init__(self,model,color,year):
#         self.model=model
#         self.color=color
#         self.year=year
#
# class SuperCar(Car):
#     def __init__(self,model,color,year,sponsor):
#         super().__init__(model,color,year)
#         self.sponsor=sponsor
#
# CLk=SuperCar('CLK GTR','Silver',1989,'Mers')
# print(vars(CLk))

# class MyClass:
#     def __init__(self,value):
#         self.value=value
#
#     @classmethod
#     def from_string(cls,integer):
#         return cls(integer)
#
# my_obj = MyClass.from_string('5')
# print(my_obj.value)

# class Rectangle:
#     def __init__(self,width,height):
#         self.width=width
#         self.height=height
#
#     @property
#     def area(self):
#         return self.width * self.height
#
# rectangle = Rectangle(4,5)
# print(rectangle.area)
#
# rectangle.width=52
# print(rectangle.area)
#
# rectangle.height=1
# print(rectangle.area)

# class Worker:
#     def __init__(self,name,doljnost):
#         self.name=name
#         self.doljnost=doljnost
#
# class MiniWorker(Worker):
#     def __init__(self,name,doljnost):
#         super().__init__(name,doljnost)
#
#
# Admin=MiniWorker('Azamat','QA engineer')
# print(vars(Admin))

class Player:
    def __init__(self,strengh,accuracy,speed,endurance):
        self.strengh=strengh
        self.accuracy=accuracy
        self.speed=speed
        self.endurance=endurance

class Attacker(Player):
    def __init__(self,strengh,accuracy,speed,endurance,skill):
        super().__init__(strengh,accuracy,speed,endurance)
        self.skill=skill
        skill=print('Атакует')

class Defender(Player):
    def __init__(self,strengh,accuracy,speed,endurance,skill):
        super().__init__(strengh,accuracy,speed,endurance)
        self.skill=skill
        skill=print('Защищает')

class Middlefield(Player):
    def __init__(self,strengh,accuracy,speed,endurance,skill):
        super().__init__(strengh,accuracy,speed,endurance)
        self.skill=skill
        skill=print('Асистирует')

class Goalkeeper(Player):
    def __init__(self,strengh,accuracy,speed,endurance):
        super().__init__(strengh,accuracy,speed,endurance)
        skill=print('Защищает ворота')

Vratar=Goalkeeper(50,35,30,60)
print(vars(Vratar))