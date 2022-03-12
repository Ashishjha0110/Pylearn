#List methods
New_list = [1,2,3,4,5]

#1. Adding a new object to the exciting list
# Append Method: this method changes the list in place 
# i.e. it means it does not give out a new list, it just adds the value to the existing list. 
#Example1
New_list.append (6)
new= New_list
print (New_list)
print (new)

#INSERT Method: It is used to insert the object at a particular index/location in the existing list. 
#Example 2
#Syntax: .insert(index,value)
New_list.insert(3,7)
I_new=New_list
print (I_new)

#EXTEND Menthod: This method is use to extend the existing list and it does not create a new copy with modified value. 
#Note: this method takes "Iterable" instead of normal object
New_list.extend([8])
Ex_new=New_list
print (Ex_new)