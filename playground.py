#concat strings 
name = 'gilbert'
print(f'el nombre es {name}') 

#casting
num = '5'
int(num)

#user input
input_user = input()

#round number 
round(3.1416, 1) 

#logical sentences
if name == True:
    print(name)
elif name == 'gilbert':
    print(name)
else:
    print(name)

#loops 

#for value in iterable:
    #do code

for item in range(1,5):
    print('range number ' + str(item))


contWhile = 1
while contWhile < 2:
    print(f'cont while {contWhile} times')
    contWhile += 1


#list
my_list = [0,1,2]

#lenght of list
print(str(len(my_list)))

#get list item
my_list[0] #prints 0
my_list[-1] #prints 2

#check item in list 
1 in my_list

#add item to list. Ej: arr, number,etc..
my_list.append(4) # my_list value is [0,1,2,4]
my_list.append([1,2]) # my_list value is [0,1,2,[1,2]]

# add items of iterable object to list 
my_list.extend(range(1,3)) # my_list value is [0,1,2,1,2]

#insert item to list in a specefic position 

