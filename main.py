#Dictionary
#Dictoionary keys has to be immutsble that is why we cannot use list as the keys for a dictionary.
dictionary= {
'a': [1,2,3],
'b': 'hello',
'c': 4  
}

#print('a'in dictionary.keys())
#print('hello' in dictionary.values())
print (dictionary.items())
##In the similar manner there is copy that copies the dictionary. SYntax: dict2= dict1.copy() 
##There is a clear method to clear the dictionary. 
# Syntax: dict1.clear()
## Pop and popitem the intial one pops the specific key and value whereas the latter which earlier used to remove any value randomly was updated in the python 3.7 to pop the last added value to the dictionary.__doc__

#Update this method updated the value of existing key or if the key is not present then it updates the dictionary with the new key and value.__doc__

# Syntax: dictionary.update({'c':6})


