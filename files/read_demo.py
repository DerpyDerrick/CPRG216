fid = open("myfile",'r')
lines = fid.readlines()
for line in lines:
    print(line.rstrip())
print(line)
fid.close