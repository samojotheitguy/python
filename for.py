# Python program to demonstrate for loops.
#

# The for loop goes through a list, like foreach in
# some other languages.  A useful construct.
for x in ['Bill', 'Alice', 'Joe', 'Sue', 'Samuel', 'Justin']:
    print(x, 'likes jelly beans.')

print() #For Space before the next line
print() #For Space before the next line


# The range operator simply creates a list of numbers
# in the indicated range.  Note that the range ends
# before the second argument.

print(range(5, 10))

# Range works with for to create the traditional for loop.
for y in range(2, 10):
    print(y),
print

for y in range(2, 10, 2):
    print(y),
print

for y in range(20, 10, -1):
    print(y),
print

