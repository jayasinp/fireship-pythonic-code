# Python provides built in functions that can check conditions that apply to at least one element, or all elements in an iterable.

#check for negative values in a list
nums = [1,2,3,4,5,-42,6,7,8]

# inefficient way to use a for loop and a flag
contains_neg = False #flag
for num in nums:
    if num < 0:
        contains_neg = True

# 🐍 pythonic way -> use the built-in any function
contains_neg = any(num < 0 for num in nums)

# 🐍 bonus -> use the built in all function
contains_neg = not all(num >= 0 for num in nums)

#any returns True if a condition applies to any element of the iterable. If the iterable is empty, returns False
#all returns True if a condition applies to all elements of the iterable, or if the iterable is empty