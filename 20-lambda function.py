print("what's lambda function and how it works & map and filter")
my_func=lambda x:x*2
my_value=my_func(4)
print(my_value)
second_try=lambda x,y:(2*x)+(3*y)
print(second_try(3,4))
my_list = [(2,8), (3,7), (1,9), (4,6)]
print("my list is: {}".format(my_list))
#print("my list is: %s" % my_list) #or I can use this format
#print("my list is:",my_list) #or I can use this format
my_list.sort()
print("sorted list is:",my_list)
my_list.sort(key=lambda x:x[1])
print("sorted list, based on second digit inside '()':",my_list)
print("map and filter")
mylist=[1,2,3,4,5,6,7,0.5,0.75]
print("my original list is:",mylist)
print("my mapped list is:",list(map(lambda x:x*2,mylist)))
print(list(map(lambda x:'even'if x%2==0 else 'odd'if x%2==1 else 'even',mylist))) #new way for if and else
print("this worked on original list because lambda is anonymous!!")
my_new_list=[1,2,3,4,5,6,7,11,13,14]
print('my new list is:',my_new_list)
print("filter numbers of my new list which are even:")
print(list(filter(lambda x:x%2==0, my_new_list)))