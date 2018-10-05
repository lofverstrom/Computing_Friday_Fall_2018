#!/usr/bin/env python

######### List sorting ##########

print('\n--- EXAMPLE: lists indexing and sorting ---\n')


fruits = ['banana', 'apple', 'pear', 'kiwi', 'orange']

print('Original list:')
print(fruits)


#print('First element in list: %s'%fruits[0])
#print('First two elements in list: %s'%fruits[0:2])


## Negative indexing is OK too
#print('Last items in list: %s'%fruits[-1])
#print('Every other element in list: %s'%fruits[::2])


## Slicing
#print('First three character of first element in list: %s'%fruits[0][0:3])


## Loop over items in list
#for fruit in fruits:
#    print(fruit)


## Sort list (defaults to sort alphabetically)
#fruits_sorted = sorted(fruits)
#print(fruits_sorted)


fruits_sorted_reverse = sorted(fruits, reverse=True)
#print(fruits_sorted_reverse)



## Uncomment to see more things you can do with 
## build in function sorted()

## Method 1: print "doc string"
#print(sorted.__doc__)

## Method 2: print help text
#print(help(sorted))



print('\n--- END OF EXAMPLE ---\n')
