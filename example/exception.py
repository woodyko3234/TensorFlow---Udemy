import sys 
try:
    #f = open('myle.txt')
    f = open('mysql.py')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err)) 
except ValueError:
    print("Could not convert data to an integer.") 
except:
    print("Unexpected error:", sys.exc_info()[0])
