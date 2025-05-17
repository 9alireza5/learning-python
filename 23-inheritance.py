print("explaining inheritance in oop")
print('\n')
class Computer:
    #count=0 # this is a clas variable and al objects can see this
    def __init__(self,ram,hard,cpu,gpu):
        self.ram=ram
        self.hard=hard
        self.cpu=cpu
        self.gpu=gpu
    def value(self):
        return self.ram+self.hard+self.cpu+self.gpu
class Laptop(Computer):  #with laptop(computer) laptop class inherit from computer class
    def value(self):
        return self.ram+self.hard+self.cpu+self.gpu+self.size
pc1=Computer(32,4,11700,3060)
pc2=Computer(16,1,10900,2070)

Laptop1=Laptop(32,1,7945,4060)
Laptop1.size=14

print('pc1 value is:',pc1.value(),'and pc2 value is: ',pc2.value())
print('laptop value is:',Laptop1.value())
print('\n')

class mobile:
    def __init__(self, name, brand):
        self.name = name
        self.brand = brand

    def get_name(self):
        return self.name


class cpu(mobile):
    def get_name(self):
        print("This mobile has HighTech %s CPU " % self.name)


brand = cpu("Intel", "Sony")
print(brand.get_name())