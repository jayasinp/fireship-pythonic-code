# Python supports default values for function parameters. 
# if a value for a parameter isnt passed during a function call
# the specified default value is used. If the default value is 
# of a mutable type, this is dangerous. If the list is modified, 
# the default value is also modified.

#to avoid this set the default value to None.

#mutable default arguments -> wrong way
def append_element(elem, L=[]):
    L.append(elem)
    return L

L1 = append_element(21) #[21]
L2 = append_element(42) #[21, 42] this is wrong

# 🐍 pythonic version -> use None
def better_append(elem, L=None):
    if L is None:
        L = []
    L.append(elem)
    return L

L1 = better_append(21) #[21]
L2 = better_append(42) #[42]