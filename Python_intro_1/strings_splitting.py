#!/usr/bin/env python

######### String splitting ##########


fullname = 'Jane Doe'

print('Full name is: '+fullname)

firstname, lastname = fullname.split(' ')

## OBS, "fullname.split()" also works in this case

print('First name is: '+firstname)
print('Last name is: '+lastname)


## Function "split()" creates a comma separated
## list where each element is observing "split criteria". 
## Uncomment the following lines for example

#print(fullname.split())
#print(fullname.split('a'))





"""
==================== Lists ========================

['Linus', 'Torvalds'] is what's called a list. You can have any number
of items in a list, and you can reference them by number using square
brackets, with 0 denoting the first item:

>>> fullname = "Linus Torvalds"
>>> names = fullname.split()
>>> print "Hello,", names[0]
Hello, Linus

Lists can contain any type, and the items don't all have to be the
same type. A list like this:

mylist = [1, "eeny meeny miny moe", 3.14159]

is perfectly valid. Lists can even contain other lists, but let's not
worry about that just now.

You can loop over the items in a list:

for n in names :
    print n

================ Slices =====================

Okay, firstname and lastname are easy if there are only two names.
What about people with multi-part names?

>>> fullname = "Guido van Rossum"
>>> names = fullname.split()
>>> names
['Guido', 'van', 'Rossum']

You can still use names[0] to get the first name. But the last name is
no longer names[1] -- that would be "van". Python gives you a neat way
of referring to several list items at once, called slices, where you
can specify a start and end position with a colon in between. So if
you knew Guido had a 2-part last name, you could say

>>> names[1:3]
['van', 'Rossum']

Or you might want to say "Give me everything except the first name".
How would you do that? You can get the number of items in the list
with len, the same way you get the length of a string. Then use it
to take a slice (I'll space things out to make it more readable):

>>> names[ 1 : len(names) ]
['van', 'Rossum']

Getting everything to the end of the list, though, is such a common case
that if you include a colon with nothing after it, Python assumes you
want everything to the end of the list:

>>> names[1:]
['van', 'Rossum']

============ Similaries between lists and strings ===========

Many of the things you can do with lists, you can do with strings,
and vice versa. You can take slices of a string:

>>> fullname[0:5]
'Guido'
>>> fullname[6:]
'van Rossum'

and you can loop over a string's individual characters:
for c in fullname :
    if c == " " :
        print "It's a space!"

You can add to the end of a list; but instead of using += like you
would for strings, use append: names.append("Jr.")

"""
