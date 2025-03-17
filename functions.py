print('for saying hello t 4 people we have three ways:')
print('----------')
print('first way is using print 4 times:')
print('hello a')
print('hello b')
print('hello c')
print('hello d')
print('----------')
print('or we can use a for loop:')
for name in ['a', 'b', 'c', 'd']:
    print('hello '+name)
print('----------')
print ('or we can use a function:')
def names(fun):
    print('hi '+fun)
for name2 in ['a', 'b', 'c', 'd']:
    names(name2)
for names3 in ['a2', 'b2', 'c2', 'd2']:
    names(names3)
print('another example for functions:')
def sum(a,b):
    return a+b
print(sum(1,2))
print(sum(5,7))
