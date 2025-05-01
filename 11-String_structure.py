my_string=(str(input()))
#print(dir(my_string))
#print(help(str.__add__))
my_string=my_string.lower()
for char in my_string:
    for letters in 'aeiouAEIOU':
        my_string=my_string.replace(letters,'')
#print(my_string)
for i in my_string:
    #print(i)
    i='.'+i
    print(i,end="")