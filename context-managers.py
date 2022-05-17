# Use a context manager to ensure that a resource is properly closed
# if you write to a text file and the logic is complicated
# if an exception is raised the file wont be closed
# a context manager will close the file regardless of an exception

#ok way -> managing files - using open and f.close()\
f = open("file.txt", "w")
f.write("Hi mom!")
f.close()

# 🐍 pythonic way -> use a context manager
with open("file.txt", "w") as f:
    f.write("hi mom!")