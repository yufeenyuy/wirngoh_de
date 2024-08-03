import sys
import chardet as cd


# Using python as a calcuator. It is important to consider the precedence of operators when doing calculations

print(3*2-5/6+(-9)**2)

a = 5
b = 3

# addition
c = a + b
print("The value of c in addition is", + c)

# subtraction
c = b - a
print("The value of c in subtraction is", + c)

# division
c = a / b
print("The value of c in division is", + c)

c = a // b #floor level result (abrunden)
print("The value of c in floor level division is", + c)

# modulo
c = a % b
print("The value of c in rest of division is",  c, c + 1)

# String: Immutable objects in python meaning that the value at a position cannot be changed

yuf = "yufenyuy"  # remember that indexing in python begin at 0 (zero)
print("the first letter in yuf is",yuf[0], yuf.count("y"))

print("All the letters in yuf are:",yuf[:])

print("let's slice the string yuf\nthe first 3 eleemtns are:", yuf[:3],
      "\nNotice how those 3 letters are indices 0,1 and 2")

print("the last letter in the string can be retrieved by", yuf[-1])

print(r"r stands for raw and prints the content of a string as passed.")

for lett in yuf:
    print(lett)

for i in range(len(yuf)): #If not specified the range function has a start index is 0 and increment by 1
    print("The letter at index", i, "is", yuf[i])
print("The length of yuf is",len(yuf))

#List: this is a mutable data type in python and can hold a series of elements of different data types.

lis = [3, 4.7,{"name": "Yufenyuy", "age":30}, -1, ["High","Medium","Low"],-1,"fruits", (17,-6), "product"]


## list operations
lis.append("fruits") #appends a whole element at the end of a list. e.g "fruits" is appended to the list as an entire element.

lis.extend("fruits") # the extend function appends the elements in an iterable object(e.g string, list, tuple) at the end of the list.

print(lis.pop(lis.index("fruits")), lis,"length of lis is", len(lis)) #pop removes the index so here fruits is completely removed from the list. lifo

print(f'the new list:{lis}')

print(lis.remove(-1), lis,"length of lis is", len(lis)) #revove spans list from left to right an eliminates,by name, the first occurance. fifo

print(lis.count(-1)) #count the number of occurances of an element in the iterable

lis.insert(2,"mango") #insert takes an index and an element to be inserted at that index. Existing element at the index is moved to right
print(lis)

lis.reverse() #reverse changes the order of the element in the list. first becomes last and vise vesa
print(lis)

#lis.sort() #sort reorders the list in ascending order but elements should be of same data type otherwise error.
print(lis,"\n")

#lis.clear: empty the list

## Slicing lists is similar to slicing strings.

#List in python can be used as stacks (last-in-first-out). LIFO is achieved with list.append and list.pop
lifolis = [] # initial an empty list
lifolis.append(1)
lifolis.append(2)
lifolis.append(3)
lifolis.append(4)
print("A list as stack after adding elements to the list:",lifolis,"\n")

lifolis.pop()
lifolis.pop()
print("A list as stack after poping elements from the list:",lifolis,"\n")

#python list can also be used as queues but require a package to achieve this since lis.append and lis.pop in python as queues is costly.
from collections import deque
queue = deque(lifolis) # first of all the list has to be converted to queue
queue.append(5) # enqueue
queue.append(6) # enqueue
queue.append(7) # enqueue

print("A list as queue after enqueue:",queue,"\n")

queue.popleft() # dequeue
queue.popleft() # dequeue

print("A list as queue after dequeue operations:",queue,"\n")

print(list(queue),"\n") # convert the queue back to the normal python list

#List comprehensions: A way of creating a list based on some criteria to fit a use case.E.g Create a list of odd numbers
oddnums = []
def oddnum(ran):
    for num in range(ran):
        if num % 2 != 0:
            oddnums.append(num)
    return oddnums

print("list of odd numbers:",oddnum(20),"\n")

# Best way to create a list of odd numbers is with a list comprehension since odd numbers follow a particular partern
limit = 20
oddnumbers = [num for num in range(limit) if num % 2 != 0]
print("Odd numbers with list comprehension:",oddnumbers,"\n")

# del statement: unlike the pop which returns the element to be removed via index, del completely romeves the element from a list by index

del oddnumbers[2] # delete the 3 element or value at index 2. Delete can also be used to delete all element or the entire list.

print(oddnumbers,"\n")

# working with sets: an unordered collection with no duplicate elements.

myset = set() # only way to create an empty set.
myset.add("mango") # add element to a set

basket = {"apple","orange","apple","pear","orange","banana", "avocado"} #duplicates are automatically removed

print("The basket:",basket,"has a length of:",len(basket),"\n")

print("mango" not in basket,"\n")

mybasket = {"apple","pineapple","apple","mango","orange","banana", "avocado"}

# Finding difference between sets
print("Elements in basket that are not in mybasket are:", basket-mybasket,"\n")

# OR operation in sets
print("Elements that are in basket or mybasket are:", basket | mybasket,"\n")

# AND operation in sets
print("Elements that are both in basket and mybasket are:", basket & mybasket, "\n")

# Exclusive OR
print("Elements that are either in basket or mybasket are:", basket ^ mybasket, "\n")

#list comprehension in sets

checkset = {ele for ele in mybasket if ele not in basket}
checksetalt = mybasket - basket
checksetalt1 = mybasket.difference(basket)

print(checkset, "\n",checksetalt, "\n", checksetalt1, "\n")

# working with dictionaries: A set of key:Value pair data type. Keys must always be unique and immutable. A dictionary is init with {}
names = {1:"yufenyuy",2:"leinyuy",3:"dzelafen",4:"wirfon"}
names[5] = "echo"  #add element to a dictionary
names[6] = "wirngoh"

ages = {}  
ages["yufenyuy"] = 30
ages["lemnyuy"] = 21
ages["echo"] = 26
ages["leinyuy"] = 35
ages["dzelafen"] = 49
print(names,"\n", ages,"\n")

# Retrieve information from python dictionary in a robust way. If key don't exist code will not throw an error.
ages.get("echo")

# pass default return value if searched element is not in the dictionary
ages.get("dzemo","not available")

mydict = dict([["p1","Christoph"],["p3","Anna"]]) # Create a dictionary with keyword dict. List or tuples can be used.

print("my dictionary:{}".format(mydict))

#Small exercise: Find the ages of people and return it as a list of sets

namesages = [(val,va) for val in names.values() for ki,va in ages.items() if val == ki] #loop through items

print(f"Names found and ages are: {namesages} \n")

namelis = [name for name in ages.keys()] # loop through keys of a dictionary
print("The current names of people registered are:", namelis, "\n")

agelis = [age for age in ages.values()] #loop through values of a dictionary

print("The current ages of the people registered are:", agelis,"\n")


words = ["cat", "window", "defenestrate"]


#compound statements: 
''' They are composed of a controlling statement and a group of controlled statements. The controlling statement determines the execution of control statements.
The controlling statement have the form <reserved keyword> <check expression>:
The controlled statements are often grouped as a block with the same level of indentation.
Among others some keywords for compound statements are *if, while, for, def*.
'''

if "cat" in words:
    print("yes!")

searchword = "window"
match searchword:
    case "cat":
        print("search word is a cat. \n")
    case "window":
        print("search word is a window. \n")
    case "cat":
        print("search word is a defenestrate. \n")
    case _:
        print("search not successful!. \n")

def check(maxlimit, currentlimit):
    if currentlimit > maxlimit:
        currentlimit = currentlimit -1
        print(f'the current limit is at:{currentlimit}')
        return check(maxlimit, currentlimit)
    return f'The max limit recorded is: {maxlimit}'
print(check(10,21))  



# args must always come before kwags or keywords. This means arguments should not be passed after kwarg e.g test(gender = "F",*args) is lkhjnot allowed 
def test(animal,*arguments,gender = "female",**keywords):
    for k in keywords:
        print(animal,gender,"has the keyword:",k,"while the value stored in the keyword is:",keywords[k],"\n")
    for ele in arguments:
        print(ele)

test("This gender:","personal info",name="yufe",age = 25, height = 1.66)

# Handling Exceptions in Python. Exceptions are errors detected when executing a python code. They'll cause the program to stop.

while True:
    try:
        num = int(input('Enter an integer value: '))
        break
    except ValueError: #if error from try block is listed after the except keyword then the except block is executed followed by the try block.
        print("since it is a ValueError detected in the try block then try again!!")

# True and False values: If and while statements are based on controlling statements that evaluate in true or false. 
'''following are used for comparisons ==, !=, <,> <=, >=. Generally comparing objects of different types like int and str always evaluate to false i.e 1 == "1" is always false.
Comparing float and int will yield expected results. The keyword not is used to negate an expression or a result'''

# this function detects and raises ZeroDivisionError
def exceptionhandling(value, val=0 , **keywords):
    if value < 1:
        try:
            for keys in keywords:
                keywords[keys] = (value + 1) / value
                val = keywords[keys]
        except ZeroDivisionError:     #if it is a zero division error from the try block then raise it.
            raise ZeroDivisionError('It is not allowed to divide by zero!')   # raise statement is used to bring up the error.
        else:                         # else block is always executed if no errors are detected in the try block. Typically after the finally clause.
            return val
        finally:
            return "End of exception Handling!"  #Always executed at the end of the try block.
    return f'{value} too large'

# lambda and map function in python

## lambda expression: 
'''This is a way of writting compact expressions typically applied on every element of an iterable. An iterable here could be e.g
list, set or tuple. By default a generato object is returned. To display content of the list at once this object must be cast as a list only.
The lambda expresion is made up of four part
1. lambda keyword
2. element from the iterable
3. column:
4. the operation that should be applied to the element from the iterable.
Lambda expressions are generally used with other supporting functions like: map, filter etc.
'''

## map function:
'''This function can be used in several ways. When used with lambda, it applies the expression defined by lambda on every element of 
the given iterable.
'''

lis = [3,2,5,7,6,9,11,20,8]
lam_ex = lambda x: str(x)

"Create a genarator object"
appli = map(lam_ex,lis)
print(f'This is a generator object:{appli} created via the combination of map and lambda.\nThe first element in the generato is:{next(appli)}')

print("The next element in appli is:",next(appli))
print("The next element in appli is:",next(appli))

"cast generator object to a list"

tup = ("yufenyuy","tardzenyuy","rachel","simba")
labex = lambda n: n.capitalize() 
capi = list(map(labex,tup))
print(f'This is {capi}')


