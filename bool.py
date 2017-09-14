# Script to demonstrate Python comparison and boolean operators.

# Don't forget the very useful in operator.  This works on most (all?) of the
# built-in data structures, including strings.
some = [2,4,7]
for a in range(1,5):
    if a in some:
        print(a, 'is'),
    else:
        print(a, 'is not'),
    print('in', some)