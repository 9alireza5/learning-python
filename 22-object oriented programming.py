print("object oriented programming")
class Person:
    count=0
    def __init__(self,name,age): #init is start method #we always have this (self)
        self.name=name
        self.age=age #these twi lines mean that every person must have a name and age\
        Person.count+=1 # this cause that every person that add, it goes up by one
    def get_name(self):
        print('name is: %s'%self.name)
    def get_age(self):
        print('age is: %s'%self.age)
    def full_info(self):
        print('name is %s and age is %s'%(self.name,self.age))
    def birthdayngettingold(self):
        self.age+=1
        print('happy birthday %s, now you are %s years old'%(self.name,self.age))
    def return_count(self):
        return Person.count
alireza=Person('alireza',29) # this is a person
alireza.get_name() #this function prints person's name
alireza.get_age() #this function prints person's age
alireza.full_info() #this function prints person's name and age
alireza.birthdayngettingold() #this function send a happy birthday message and add 1 to person's age
print('\n')
#now we add a new object to our class:
mammad=Person('mammad',28)
mammad.full_info()

print('at this moment we have %i person' % Person.count)