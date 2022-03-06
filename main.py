##List Slicing
#1. List are mutable
amazon_cart =['notebook','candies','jwellery','googles']
amazon_cart[0]='laptop' #changing the value at index 0
# if we want to copy the list then it should be done in this way
new_cart= amazon_cart[:]
print(amazon_cart)
#print(amazon_cart[1:3])
#print(amazon_cart[0::])

##At this point as we have not assigned any slicing
## so the changes at index 0 happens in the amazon cart stored in the memory location.
new_cart=amazon_cart
new_cart[0]='gum'
print(new_cart)
print(amazon_cart)



