import os
import os.path
max_offset = 26
result = ""

def getString():
        print('Please enter the name of the source file. ')
        file = input()
        if os.path.isfile(file):
            textFile = open(file, 'r')
            string = textFile.read()
            return string
        else:
            print('File name incorrect.')
            exit(1)
def getOutputFile():
    print ('Please enter the name of the output file. ')
    file = input()
    try:
        outputFile = open(file, 'w')
        return outputFile
    except:
        print('Output file cannot be accessed.')
        exit(1)

def getOffset():
    offset = 0
    while True:
        print('Enter the offset (1-%s)' % (max_offset))
        offset = int(input())
        if (offset >= 1 and offset <= max_offset):
            return offset
        else:
            print('Incorrect offset entered.')
        

def caesar(string, offset):
    offset = -offset
    result = ""

    if symbol.isalpha():
            num = ord(symbol)
            num += offset

            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26
            result += chr(num)
    else:
        result += symbol
    return result

def writeOutput(outputFile, result):
    outputFile.write(result)
    outputFile.close()

    
string = getString()
outputFile = getOutputFile()
offset = getOffset()
for symbol in string:
    result += caesar(string, offset)
writeOutput(outputFile, result)

