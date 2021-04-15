#Register
#Login


#Dictionary- a data type. Like  list, but unlike a list, it is created using curly brackets{}, not square brackets. It uses key value pair.
aSampleList = [1,2,3,4,5]
dictionaryOne = {}
print(dictionaryOne)#This prints the contents of the dictionary, which at this time is just the curly brackets{}

#Let's populate the dictionary- Method 1
dictionaryOne = {
    'key1' : 'value1',
    'key2' : 'value2',
    'key3' : 'value3'}
print(dictionaryOne)

#Let's populate the dictionary- Method 2
dictionaryTwo = {}
dictionaryTwo['key4'] = 'value4'
dictionaryTwo['key5'] = 'value5'
dictionaryTwo['key6'] = 'value6'
print(dictionaryTwo)

#We can delete items from a dictionary
del dictionaryTwo['key4']
print(dictionaryTwo)
#Another way to delete contents is by using 'pop'
dictionaryOne.pop('key1')
print(dictionaryOne)

#Dictionary Loop
#To use the for loop, you'll need to specify the key and the value in dictionary name.
for key, value in dictionaryOne.items():
   print('I have ' + key + ' relating with ' + value)
#This means for each key-value pair in the dictionary items, perform the following action- print the statement.
