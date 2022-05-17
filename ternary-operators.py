# Python uses if/elif/else blocks for control flow

# assign a value based on a condition
a = 42

# ok version -> if/else blocks
if a > 0:
    sign = "positive"
else:
    sign = "negative"

# 🐍 pythonic version -> use a ternary operator
sign = "positive" if a > 0 else "negative"