friends = ['joseph', 'glenn', 'sally']
# print(friends[1])   # prints out glenn

# lists are mutable (change be edited)
friends[0] = 'Henry'
# print(friends)   # it prints ['Henry', 'glenn', 'sally']

# Using range function
# print(range(4))   # prints 0, 1, 2, 3

# counted loop
for i in range(len(friends)):
    friend = friends[i]
    # print(i, friend)

# Concatenting lists
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
# print(c)

# print(dir(a))  # this is to find the functions to use on lists

# Building lists from scratch
stuff = list()   # OR stuff = []
stuff.append('book')
stuff.append(99)
print(stuff)  # prints ['book', 99]

# in operator
some = [1, 9, 35, 23]
print(9 in some)  # prints TRUE

# You can use list.sort() to arrange items in a list alphabetically

# Split
abc = 'With three words'
stuff = abc.split()   # converts abc into stuff list
# print(stuff)

# split just separates words from delimiter (whitespace or any delimiter)
# you can specify the particular delimiter you want

# Double Split Pattern
line = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
words = line.split()
email = words[1]
pieces = email.split('@')
# print(email)  # prints out stephen.marquard@uct.ac.za
# print(pieces)  # prints out ['stephen.marquard', 'uct.ac.za']
