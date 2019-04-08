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


#logical operators
a = 1
b = 1 

a > b # returns True
a <  b # returns True
a >= b # returns False
a <= b # returns False

not True # returns False since not negates condition


if a and b : #if a and b are true do condition 
    #execute your code 
    a = True
elif a or b :  #if a or  b are true do condition 
     #execute your code 
     a =  False


a is b # returns True since they share same space in memory
a == b # returns True since they share the same value

a = [1,2]
b = [1,2]

a is b # returns False since they not share same space in memory
a == b # returns True since they share the same value


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
my_list.insert(0,'hola')  # my_list value is ['hola',0,1,2,1,2]

#clear all elements from list

my_list.clear()  # my_list value is []

#delete element from list (optional: use that value later in a variable)

popped_element = my_list.pop() #by default delete last element from list and its now in variable
                               #pop can delete by index with pop(index)

# remove item from list if match its found in list,only removes the first incidence found

my_list = [1,2,2,2]

my_list.remove(2)  # my_list value is [1,2,2,2] ,   

# get index of item if a match its found in list,only gets the index of  the first incidence found

my_list.index(1) # returns index 0 

# count number of incidences in list 

my_list.count()

# reverse content of a list 

my_list = [1,2,2,2]
my_list.reverse()  # set the list value to [2, 2, 2, 1]

#sort simple (we can sort by the criteria that we want later)

my_list = [1,3,2]

my_list.sort() #returns [1,2,3] 

#join values of list of strings 

my_list = ['hello ', 'word']

', '.join(my_list) # returns 'hello , word' (join can only be used with a list of str)

#slicing list (copy of list to another variable ) slicing can be used in any iterable objects 

#my_list[start: end: step] 

#start = index of start for the array.
#end =  index of end for the array,exclusive range so it doesnt count the end range
#step = intervals that we want the copy to make (if wanted with intervals ) .

my_list = [1,2,3,4,5,6] 

my_list[0:] #copy of all elements of the list
my_list[:] #copy of all elements of the list
 
my_list[1:]  #copy elements of the list starting from the index 1 of the list

my_list[-1:]  #returns copy array  [6]
my_list[-2:]  #returns copy array  [5,6]

my_list[1:3] #returns copy array  [2,3] , exclusive range in the end 

my_list[:-1] #returns copy array   [1,2,3,4,5] ,we copy backwards and dont take in account the end limit

my_list[::2] #returns copy array  [1,3,5] since we take a step of 2 values

my_list[::-1] #returns copy array [ 6,5,4,3,2,1],reverse the array

my_list[1:3]  =[ 'a', 'b','c' ]  # returns copy array [1, 'a', 'b','c' ,2,3,4,5,6] so we copy the array and insert new values in the range 

my_list = [ 'hola', 'adios']

my_list[0][::-1] #retorna 'aloh', reversing the string

#swaping elements of a list 

my_list = [ 'hola', 'adios']

my_list[0] , my_list[1] = my_list[1] , my_list[0] # returns ['adios', 'hola']   

# Lists Comprehensions(kinda like for each in other lenguages ,map in javascript )

my_list = [1,2,3]

#[var_name for varName in list] structure of list Comprehensions

my_list2 = [nm * 2 for nm in my_list] #returns a new list with  [2, 4, 6] since we are multiplying times 2 each value of the list

#with conditionals we have

[nm * 2 for nm in my_list if nm%2 == 0] #only if we have a logical operator

[nm * 2  if nm%2 == 0  else nm *3 for nm in my_list ] #multiple logical operators go like this 

# using nested operations in list Comprehensions

[['x' for x in range(1,4)] for value in range(1,4)] #returns  [['x', 'x', 'x'], ['x', 'x', 'x'], ['x', 'x', 'x']] ,nested operation 

#dictionaries (objects in other lenguages)

person = {'name': 'Gilbert' , 27: 'my age'} #value of key in list  permitted its string or number

#using the dict() function for creating a dictionary

person = dict(name = 'Pedro', age = 44)  #creates dictionary {'name': 'Pedro', 'age': 44}

person['name'] # returns value pedro

#add key/value pair to dictionary 

person['country'] = 'Venezuela'  # adds the key/value pair having now {name = 'Pedro', age = 44, country='Venezuela'}


#format string with dictionary values 

artist = {
    "first": "Neil",
    "last": "Young",
}

full_name = "{} {}".format(artist["first"],artist["last"])  #returns  Neil Young 

# dictionarys are not iterable objects!!!!!!, if we want to iterate a dictionary 
# we need to use the methods keys() ,values() or items() more of this in the next code blocks

#search value in dictionary

'Pedro' in person # by default the in will search in the dictionary by key so doesnt returns anything 

'Pedro' in person.values() # here it will search the value in the values of the dictionary

#delete data from the dictionary

person.clear()

#copy dictionary (make copy to another space in memory)
copyPerson = person.copy()

#init dictionary

   #dict.fromKeys can be used to
{}.fromkeys( ['name', 'address'], None ) # returns {'name': None, 'address': None} 

#get value of dictionary by key 

person.get('name') # returns Pedro if the dictionary have a property name ,if not returns None

#remove value from dictionary 

artist = {
    "first": "Neil",
    "last": "Young",
}

artist.pop('first') # delete  the key/value pair first/Neil and returns the str Neil
artist.pop('e') # returns error KeyError since the key e doesnt exist in the dictionary 

#remove random value from dictinary 

artist.popitem() # removes a random value and returns the key/value pair 
artist.popitem('a') # returns error since pop item dosnt take a argument

#update value of one dictionary to another dictionary 

artist = {
    "first": "Neil",
    "last": "Young",
}

performer = {}

performer.update(artist)
performer # performer now have the key/values {"first": "Neil","last": "Young"} since we updated the performer dictionary with the info of the artist dictionary 

artist['first'] = 'Neily'

performer.update(artist) # performer now have the key/values {"first": "Neily","last": "Young"} ,so the update() method
                         # adds the key/values if they dont exist and if they exist they will update the values based in his keys 

# Dictionary  Comprehensions (kinda like for each in other lenguages ,map in javascript )

#manipulate existing dictionary 
numbers = dict(first = 1, second = 2 ,third = 3)

squared_numbers = {key: value**2 for key,value  in numbers.items()} # this will create the dictionary {'first': 1, 'second': 4, 'third': 9} 

#create dictionary 

{num: num ** 2 for num in range(1,6)} # creates the dictionary {1: 1, 2: 4, 3: 9, 4: 16, 5: 25} with the key value pairs 


# create dictionary with 2 strings 
str1 = 'ABC'
str2 = '123'

combo = { str1[i]: str2[i] for i in range(0, len(str1)) } # creates de dictionary {'A': '1', 'B': '2', 'C': '3'} here
                                                          # we use the index in the dictionary Comprehensions and we
                                                          # condition the for with the lenght of the string 

#manipulate existing dictionary to create other dictionary

instructor = dict(name = 'Gilbert' , age = '27' )

upper_instructor = {name.upper(): age.upper() for name,age in instructor.items()} # returns {'NAME': 'GILBERT', 'AGE': '27'} so we changed the keys and values to uppercase 

#conditional operations in dictionary Comprehensions

num_list = range(1,5)

{num: ('even' if num % 2 == 0 else 'odd') for num in num_list}










