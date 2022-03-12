#List methods Part 1.2
New_list = ['a','b','c','d','e','f','b','b']

# INDEX method: This method is used to get the index of a particular object.
#Syntax: .index(value,start,stop)
print(New_list.index('d',0,4))

#in keyword
print('d' in New_list)

#COUNT method: This method is used to count the number of times an object occurs in a given list.

print (New_list.count('b'))