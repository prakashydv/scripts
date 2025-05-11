import os
f = file('list.txt','w')

for subdir, dirs, files in os.walk(os.getcwd()):
    for file in files:
        filepath = os.path.join(subdir, file)
        f.write(filepath)
        print filepath

f.close()