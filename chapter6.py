
'''
#Question 1
class Thing():
    pass

print(Thing)

example = Thing()

print(example)

#Question 2
class Thing2():
    letters = 'abc'

print(Thing2.letters)

#Question 3
class Thing3():
    def __init__(self):
        self.letters = 'xyz'

something = Thing3()
print(something.letters)

#Question 4
class Element:
    def __init__(self,name,symbol,number):
        self.name = name
        self.symbol = symbol
        self.number = number

#obj = Element('Hydrogen','H','1')

#Question 5
dict = {'name':'Hydrogen','symbol':'H','number':'1'}

#hydrogen = Element(dict['name'],dict['symbol'],dict['number'])
hydrogen = Element(**dict)
print(hydrogen.name)

#Question 6
class Element:
    def __init__(self,name,symbol,number):
        self.name = name
        self.symbol = symbol
        self.number = number
    def dump(self):
        print('name=%s,symbol=%s,number=%s' %
              (self.name,self.symbol,self.number))


dict = {'name':'Hydrogen','symbol':'H','number':'1'}
hydrogen = Element(**dict)
hydrogen.dump()

#Question 7
class Element:
    def __init__(self,name,symbol,number):
        self.name = name
        self.symbol = symbol
        self.number = number
    def __str__(self):
        return ('name=%s,symbol=%s,number=%s' %
              (self.name,self.symbol,self.number))

dict = {'name':'Hydrogen','symbol':'H','number':'1'}
hydrogen = Element(**dict)
print(hydrogen)

#Question 8
class Element:
    def __init__(self,name,symbol,number):
        self.__name = name
        self.__symbol = symbol
        self.__number = number
    @property
    def name(self):
        return self.__name
    @property
    def symbol(self):
        return self.__symbol
    @property
    def number(self):
        return self.__number

hydrogen = Element('Hydrogen','H','1')
print(hydrogen.name)

#Question 9
class Bear:
    def eats(self):
        return 'berries'

class Rabbit:
    def eats(self):
        return 'clover'

class Octothorpe:
    def eats(self):
        return 'campers'

b = Bear()
r = Rabbit()
o = Octothorpe()

print(b.eats())
print(r.eats())
print(o.eats())
'''

#Question 10
class Laser:
    def does(self):
        return 'disintegrate'

class Claw:
    def does(self):
        return 'crush'

class Smartphone:
    def does(self):
        return 'ring'

class Robot:
    def __init__(self):
        self.laser = Laser()
        self.claw = Claw()
        self.smartphone = Smartphone()
    def does(self):
        return '''I have many attachments:
My laser, to %s.
My claw, to %s.
My smartphone, to %s.''' % (
            self.laser.does(),
            self.claw.does(),
            self.smartphone.does() )

robbie = Robot()
print(robbie.does() )





