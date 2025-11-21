import os

print("currenct working dir", os.getcwd())
cwd = os.getcwd()

file = os.path.join(cwd, "demo.txt")
exist = os.path.exists(file)
print(exist)