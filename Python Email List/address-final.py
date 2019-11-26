phonebook = {}
with open('phonebook.txt', 'r') as phone_book:
    while True:
        name = phone_book.readline().strip('\n')
        email = phone_book.readline().strip('\n')
        if name == "" :
            break
        else:
            phonebook[name] = email
print (phonebook)
            
