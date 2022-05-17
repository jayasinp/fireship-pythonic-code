# To check a list if a member is included, you can use the for loop or the in loop

L =["JS","PY","RB","PHP","RST"]
x = "RST"

#ok version -> for loop and an equality check
for i in range(len(L)):
    if x == L[i]:
        print(f"{x} is contained in the list")

# 🐍 pythonic version -> use "if x in L"
if x in L:
    print(f"{x} is contained in the list")