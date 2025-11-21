fid = open("myfile.txt",'w')
students = ["Sam\n", "John\n", "Sara\n", "Tom\n"]
fid.writelines(students)
fid.close()