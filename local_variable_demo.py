g_var = 3

def mysum():
    l_var = 3
    global inside_global
    inside_global = 4
    print(l_var)
    print(g_var)


mysum()
print(g_var)
# print(l_var) error
# print(inside_global) error