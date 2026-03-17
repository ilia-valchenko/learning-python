# NOTE: Set can only contain unique values

simpleSet = { 'a', 'b', 'c' }

# Pass any iterable object to Set's constructor
simpleSet = set([1, 2, 3])

# We can even pass Tuple
simpleSet = set(('a', 1, 'c'))

# Convert a list into a set, and vice versa, to get unique values
listWithDuplicates = ['a', 'b', 'b', 'c', 'c', 1000]
listWithUniqueItems = list(set(listWithDuplicates)) # [1000, 'c', 'b', 'a']

# NOTE: We can't use slice syntax here. The code below will not work.
# TypeError: 'set' object is not subscriptable
# mySet[0]

# Add elements to a set
# It's not the 'append' function we have for lists. Append adds a new item in the end of the list.
# In our case we just tossing it on the pile.
mySet = set(listWithDuplicates)
mySet.add('Cake')

# Check whether an item in a set or not
doesSetContainSpecificItem = 'Cake' in mySet

# Get the length of a set
lengthOfMySet = len(mySet)

# Pop an element of a set
while len(mySet):
    print(mySet.pop())
    
# 'discard' function removes a specified element from a set if it is present
mySet = {'a', 'b', 'c'}
mySet.discard('a')
