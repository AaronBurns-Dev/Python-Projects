def spellChecker():
    dictInput = input("Enter the name of dictionary: ")
    dictFile = open('words.txt', 'r')
    dictionary = dictFile.read()
    textInput = input("Enter the name of text file: ")
    textFile = open('moreWords.txt', 'r')
    while dictionary != '':
        # Check word entered against dictionary
        word = dictionary
        text = textFile.readline()
        if word in dictionary:
            print("No spelling errors found.")
            break
        else:
            print("Unknown word " + word + " found in line " + text)
            break
spellChecker()
