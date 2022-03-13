#Dictionary
#Dictoionary keys has to be immutsble that is why we cannot use list as the keys for a dictionary.
dictionary= {
'a': [1,2,3],
'b': 'hello',
'c': 4  
}

print (dictionary['a'][1])

#Dictionary Methods
#1. get method
#Syntax: .get

user={
'weapons':[1,2,3,4],
'greet' : 'hi',
'age' : 23  
  
}
print(user.get('age',26))# this line simply mean that if the age key does not have a value assigned to it then assign a the default value 26 to it but if it has then print the value which is there in the dictionary.

#dict method is use to create a dictionary
user2 = dict(name='Ashish')
print(user2)