#Generators save memory and improve performace. 
#summing the first 42000 natural numbers with sum takes 351064 bytes
#using a generator reduces the size to just 104 bytes.

from sys import getsizeof

# inefficient way: using a list
L = [n for n in range(42_000)]
sum(L) #881979000
getsizeof(L) #351064 bytes

# 🐍 pythonic way -> use a generator
G = (n for n in range(42_000))
sum(G) #881979000
getsizeof(G) #104 bytes