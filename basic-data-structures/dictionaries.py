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
