import os




### Current directory
a = os.getcwd()
print(a)


### Get the path for parent directory
# step 1: use "os.pardir" to return .. command
print(os.pardir)  #  ..

# step 2: use join to form path command
path_command = os.path.join(os.getcwd(), os.pardir)
print(path_command)  # /home/synferlo/my_disk/git/trypython/Python_Basic/..

# step 3: use os.path.abspath() generating final path for parent dir
par_path = os.path.abspath(path_command)
print(par_path)  #  /home/synferlo/my_disk/git/trypython

