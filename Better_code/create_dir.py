import os
from pathlib import Path




###------Method 1------###
'''
if not os.path.exists('my_data'):
    os.mkdir('my_data')
'''

###------Method 2------###
#   This would be much easier

# create my_data then create hello dir if they are not existed

'''
my_path = './my_data/hello'
Path(my_path).mkdir(exist_ok = True)
'''

