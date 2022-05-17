# null is denoted with the keyword none but you can use if to do a simplified null check

# null check: ok version -> explicit if x is not none
n = 42
if n is not None:
    print(f"n exists and is equal to {n}")

# 🐍 pythonic version using simplified if

x = 20
if x:
    print(f"x exists and is equal to {x}")