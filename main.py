#List methods Part 1.2
New_list = [1,2,3,4,5]

# removing the value from a list
#POP method is used to remove the object from the end or from the given index of the list. By default, it has the index of the last object. pop()/pop(index)
# if we use the pop and use it to assign or create the new list then it will only pop that index value and paste it to new list.
New_list.pop()
new=New_list.pop(2)
print(New_list)
print(new)

#REMOVE method is used to remove a given value. remove(value)

# New_list.remove(4)
# print(New_list)

#CLEAR method simply clears the entire list 
New_list.clear()
print(New_list)