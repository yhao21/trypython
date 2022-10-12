
import os, sys


def main():
    a = [1,2,3,4,5]
    
    
    for i in range(10):
        print(a[i])

if __name__ == '__main__':
    try:
        main()
    except:
        os.execv(sys.executable, ['python3.8'] + sys.argv)
