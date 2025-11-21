with open('myfile') as fid:
    for line in fid:
        print(line, end='')

with open('myfile','w') as file:
    file.write("Hey there")