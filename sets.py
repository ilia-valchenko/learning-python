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
