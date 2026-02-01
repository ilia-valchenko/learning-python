# It looks like we are casting integer 4 to bytes objects, but not so fast.
# Actually it creates an empty bytes object that's four bytes long.
b = bytes(4)

print(b) # b'\x00\x00\x00\x00'