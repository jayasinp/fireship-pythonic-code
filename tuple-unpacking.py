# You can unpack values directly from a tuple. 
# One way is to access each element using indices.
# The efficient way is to unpack the elements directly.

# Tuple unpacking
some_tuple = (1,2,3)

# ok version -> unpack elements by index
x = some_tuple[0]
y = some_tuple[1]
z = some_tuple[2]

# 🐍 pythonic version -> unpack elements directly
x, y, z = some_tuple