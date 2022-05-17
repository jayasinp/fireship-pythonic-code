#When iterating over values in a list, a common pattern is to use a for loop and an index
#A neater way is to use a for loop and iterate directly over the list elements.

#iterating over a single list
L = ["a","b","c","d"]

# ok version -> index in range
for i in range(len(L)):
    val = L[i]
    print(i, val)

# 🐍 pythonic version -> access elements directly
for el in L:
    print(el)

# 🐍 pythonic version -> use enumerate if you need the index, value pair
for i, val in enumerate(L):
    print(i, val)

# these also apply when iterating over multiple lists. We can iterate directly over values in two collections using zip. 
# if an index is required, we can use a combination of enumerate and zip.

A = ["a", "b", "c", "d"]
B = ["e", "f", "g", "h"]

# ok version -> index in range
for i in range(len(A)):
    va, vb = A[i], B[i]
    print(i, va, vb)

# 🐍 pythonic version -> use zip to get values 
for va, vb in zip(A,B):
    print(va,vb)

# 🐍 pythonic version -> use zip and enumerate to get an index value too
for i, (va, vb) in enumerate(zip(A,B)):
    print(i, va, vb)