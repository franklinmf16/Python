import sys


for arg in sys.argv[1:]:
    front = arg.split(':')
    print(int(front[1])*100)
