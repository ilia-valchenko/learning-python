bool(1) # True
bool(0) # False
bool(0.0) # False
bool(-1) # True
bool(1j) # True
bool(0j) # False
bool('True') # True
bool('False') # NOTE: True
bool('') # False
bool(' ') # True
bool([]) # False
bool({}) # False
bool([1, 2]) # True
bool(None) # False

weatherIsNice = False
haveUmbrella = True

if not haveUmbrella or weatherIsNice:
    print('Stay inside')
else:
    print('Go for a walk')
