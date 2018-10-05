#!/usr/bin/env python

######### Strings and lists ##########

print('\nEXAMPLE: "strings and lists"\n')

fullname = 'Jane Doe'

## Print original string
print('Full name is: '+fullname)


## Create a list 
list_of_names = fullname.split(' ')


## Print list
print(list_of_names)



## Access elements in list by index
## OBS, Python uses zero based indexing

#firstname = list_of_names[0]
#lastname  = list_of_names[1]

#print('First name is: '+firstname)
#print('Last name is: '+lastname)



## What will happen if we use a negative index?
#print('Negative index [-1]: '+list_of_names[-1])
#print('Negative index [-2]: '+list_of_names[-2])



## Slice a string
#print('First two letters of firstname: '+firstname[0:2])
#print('Last two letters of fullname: '+fullname[-2:])
#print('3rd to 7th letters of fullname: '+fullname[2:7])
 


print('\n--- END OF EXAMPLE ---\n')
