#List methods Part 1.2
New_list = ['a','b','c','d','e','f','b','b']
New = ['a','b','c','d','e','f','b','b','a','c']

# SORT method: This method does not give any output. it is simply use to sort the value of the list. 
# There is function named "SORTED(iterable,key,reverse)" but that function returns the value.
New_list.sort()
print(sorted(New))
print(New_list)

# "reverse" method is use to reverse the list without sorting it.

New_list.reverse()
print (New_list)