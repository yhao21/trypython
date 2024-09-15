from pathlib import Path



'''
You can check existence and create a dir using
    Path(<your path>).mkdir(parent = , exist_ok = )
Example:
    Path(<your path>).mkdir(parent = True, exist_ok = True)

If parent = True, any missing parents of this path are created as needed
If exist_ok = True, FileExistsError will not be raised unless the given path already exists in the file system and is not a directory
If exist_ok is false (the default), FileExistsError is raised if the target directory already exists.
    
'''
