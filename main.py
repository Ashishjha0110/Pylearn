##Create a program to check the password 
username = input ('Enter the desired username:')
password = input ('Enter the password:')
paslen = '*' * len (password)

#print('Hi your username is:' +username + 'and your password is :' +password +'which is '+paslen +'long')
print(f'{username},your password,{paslen},is {len(password)}long')






