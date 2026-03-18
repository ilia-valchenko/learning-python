from collections import defaultdict

animalsDictionary = {
    'a': 'aardvark',
    'b': 'bear',
    'c': 'cat', # Trailing comma - good practice
}

bear = animalsDictionary['b']

# Add a new item to the dictionary
animalsDictionary['d'] = 'dog'

# Change the value
animalsDictionary['a'] = 'antelope'

# Get keys & values
# If we want to change them we need to modify underlying dictionary
keys = animalsDictionary.keys() # NOTE: It's an immutable dict_keys object not a list. We can iterate over dict_keys, but can't change it.
values = animalsDictionary.values() # NOTE: It's an immutable dict_values object not a list. We can iterate over dict_values, but can't change it.

# But we can do the following
simpleList = list(animalsDictionary.keys())

# Get value from the dictionary by using fake key
# item = animalsDictionary['fakeKey'] # KeyError: 'fakeKey'

# We have an alternative function for retrieving values from a dictionary
# Note: The second argument is a default value
item2 = animalsDictionary.get('fakeKey') # None
item3 = animalsDictionary.get('fakeKey', 'defaultAnimal') # defaultAnimal

# Length of a dictionary
numberOfItems = len(animalsDictionary)

# Dictionary of lists
complexDictionaryOfAnimals = {
    'a': ['aardvark', 'antelope'],
    'b': ['bear']
}

complexDictionaryOfAnimals['b'].append('bison')
complexDictionaryOfAnimals['c'] = ['cat'] # The item with 'c' key doesn't exist. That's why we need to set a list.

# Check a key for an existence
if 'c' not in complexDictionaryOfAnimals:
    complexDictionaryOfAnimals['c'] = []

complexDictionaryOfAnimals['c'].append('cat')

# Start using defaultdict from collections
animals = defaultdict(list)
