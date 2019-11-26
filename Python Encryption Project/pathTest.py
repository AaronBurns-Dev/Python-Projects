import os
import os.path

PATH = './deleteCookie.txt'

if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
    print ("My roflcopter goes soi soi soi soi")
else:
    print ("Sadface :( ")
