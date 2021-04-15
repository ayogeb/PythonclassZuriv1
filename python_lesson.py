#Variable. A Python variable is a reserved memory location to store values. In other words, a variable in a python program gives data to the computer for processing. This memory location can handle only one item (for e.g., a single number or word- a single data type) OR multiple items at the same time (as in lists, array, etc- multiple data types).
cup = "Water";
print(cup)
cup = "Sand" #Here, we are re-declaring the variable "Cup"- from sand water to sand.
print(cup)

crate = ['Sand',"Water",7,5.9,True]
print(crate)
print(crate[1])
crate.append('Mike') #appends 'Mike' to the end of the list 'crate' --> Mike is placed at index position5 (starting from 0)
print(crate[5])


print('new file')
firstValue = 50
secondValue = 200

result = firstValue + secondValue #nomenclature format used here is called camel casing: starts with lowercase (first) and subsequent words start with uppercase (Value).
print(result)

#Data Type, String --> uses single quote '' or double quote "". Examples include the following:
string1 = "Mike"
string2 = "4.5"
string3 = '0'
string4 = 'true'
string5 = "6"
print(string1)
print(string1 + string4) #Notice no space between 'Mike' and 'true' in output
print(string1 + ' ' + string4) #Now has space between 'Mike' and 'true' in output due to (' '). This is concatenation.

#Data Type, numbers. Numbers do not have any quote signs around them
number1 = 4.5
number2 = 0
number3 = 5
number4 = -4
number5 = 13890003920

print(number1 + number3) #Take note, concatenation with numbers is actually addition.
#print(string1 + number1) #Note 2 different data types cannot be added/ concatenated.Error message given off: can only concatenate str (not "float") to str

#Data Type, Boolean. Can only be 1 OR 0, True (== yes) OR False (==no)
isStudentAcction = True #yes
print(isStudentAcction)
isGraduate = False #no
print(isGraduate)

age = 50
if(age > 45):
    print('yes')

#Sttring Formating
name = "Mike"
age = 55

print("His name is " + name) #another way we can write this command is the following:

print("His name is %s" %name) #%s is saying add a string which is defined by %name. %s is used because the variable input we're interested in (name = Mike) is a string. When it is a number, we use %d

print("His name is %s and he is %d years old" %(name, age))
#We can apply this principle to a list:
sampleList = ['mike', 'dove', 'love']
print("some text %s" %sampleList)

#String Methods: Determiniing the length of a string
string = "I am a string"
print(len(string)) #Prints the length of a string, index count starts from 0.
print(string.index('g')) #Prints the index of letter 'g'
print(string.count('a')) #Prints the quantity of 'a' in the string
print(string.count('am')) #Prints the quantity of 'am' in the string
print(string.count(' ')) #Prints the quantity of 'space' in the string
print(string.count('')) #Returns 14, not sure what this count refers to

print(string[2:9]) #Prints from index 2 to 8 (note: not 9)
print(string.upper())#Print the string in uppercase
print(string.lower()) #Print the string in lowercase

print(string[::-1]) #Inveres the string, i.e. "I am a string" becomes "gnirts a ma I"
print(string.startswith("I")) #checks if the string starts with I, returns True or False
print(string.startswith("P")) #checks if the string starts with P, returns True or False

print(string.endswith("ssskhjd")) #checks if the string ends with 'ssskhjd', returns True or False


#Operators- -perform actions on one or more entities.
# +, - *, /
firstValue = 4
secondValue = 7

#addition
print('addition--->')
print(firstValue + secondValue)
#+ used for concatenation of strings

#subtraction
print('subtraction--->')
print(firstValue - secondValue)

#multiplication
print('multiplication--->')
print(firstValue * secondValue)

#division
print('division--->')
print(firstValue / secondValue)

#assignment operator =
variable = 5

#comparison

#isEqual
print(firstValue == secondValue) #This checks if firstValue is equal to secondValue. Should return False in this case, since they are not equal.Compares equality.

#isGreater
print(firstValue > secondValue)
#isLess
print(firstValue < secondValue)
#isGreaterorEqual
print(firstValue >= secondValue)
#isLessorEqual
print(firstValue <= secondValue)
#remainder (modulus)
print(firstValue % secondValue)

voice = 'Shout '
print(voice *5)
aList = [1,2,3,4,5]
print(aList *3)

A = [1,2,3,4]
B = [5,6,7,8]
print(A + B)

age = 35
age = age + 1
print(age)
#Another way of writing age = age + 1 would be:
age +=1 #age +=1 is equivalent to age = age + 1
print(age)
#It can also be used with other mathematical operators like -, *, /
age /=2 #Or age *=2; age -=2, etc
print(age)

#Conditionals
#operations carried out if conditions are satisfied.
age = 18.5
movie = "scary terry"
height = 5

if(age >=18):
    print("Customer can purchase ticket for " + movie)

if(age < 18):
    print("Customer is not allowed to watch this " + movie)

#Conditionals- and/ or
#and- both conditions must be true for the test to pass.
# oronly one condition must be tru tor the test to pass.

if (age >= 18 and height >=5):
    print('Person can get on this ride')
  
elif(age <18 or height < 5):
    print('Person cannot get on this ride')
else:
    print('Error, something went worng with your input')


    
aList = ['Mike','Live','Long']
name = 'Live'
if(name in aList):
    print('Name Found')
else:
    print('Name not Found!')

#Loops- ForLoops
alist = [1,2,3,4,5,6]
for item in alist:
    print(item)

for x in range(5):
    print(x) #This prints all the numbers in range(5), ie.e, 0,1,2,3,4

for x in range(5):
    if(not(x == 0)):#This prints numbers in range(5) apart from 0, i.e., 1,2,3,4
        print(x)

for x in range(6):
    if(x == 0):
        continue
    print(x) #Prints all numbers in range(6) apart from 0.

#Loops- WhileLoops
count = 5
while count > 0:
    print(count)
    count -=1

#Functions- Functions allow us to group a block of code and use them over and over again.
 #To define a function, we start with the word 'def', then the name of the function, followed by parenthesis(). Afterwards, indicate the action required in the function (In this case below, it is to print 'This is a function).

def nameOfFunction():
    print('This is a function')
#Running the code at this point won't do anything, since we've only defined the function and not called it--> it shouldn't return anything.

nameOfFunction() #Here we call up the function, so it returns 'This is a function' as in the function definition. We can call it up as many times as we want.

#We can pass parameters into a function.
def nameOfFunction(count):
    print('This is a function %d' %count)

#We can pass even more parameters into the function.
def nameOfFunction(name, count):
    print('%s called the function %d' %(name,count))
nameOfFunction("Ayoge",4)
nameOfFunction("UGB",5)
nameOfFunction("Mike",2)

def nameOfFunction(name, count):
    print(name*count)
nameOfFunction("Ayoge ",4) #Prints the name Ayoge 4x, as per function command.
nameOfFunction("UGB ",5) #Prints the name UGB 10x, as per function command.
nameOfFunction("Mike ",2) #Prints the name Mike 2x, as per function command.
