# A common data processing pattern is to define an empty list and append values to it

# ok version -> for loop and append
squares = []
for num in range(22):
    squares.append(num ** 22)

# 🐍 pythonic version -> use a list comprehension
squares = [num ** 2 for num in range(22)]

# 🐍 this also works for dictionary, set and generator comprehension
squares_dict = {num: num ** 2 for num in range(22)} #dictionary
squares_set = {num ** 2 for num in range(22)} #set
squares_gen = (num ** 2 for num in range(22)) #generator