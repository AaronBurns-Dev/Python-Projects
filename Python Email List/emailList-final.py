phonebook = {}
file = input("Enter the name of your dictionary: ")
with open(file, 'r') as phone_book:
    while True:
        name = phone_book.readline().strip('\n')
        email = phone_book.readline().strip('\n')
        if name == "" :
            break
        else:
            phonebook[name] = email

def addressBook():
    menu = {}
    menu['1'] = "Lookup Email"
    menu['2'] = "Add Name/Email"
    menu['3'] = "Change Email"
    menu['4'] = "Delete Name/Email"
    menu['5'] = "Save and Exit"
    while True:
        options = menu.keys()
        for entry in options:
            print (entry, menu[entry])

        selection = input("Please Select a Option: ")
        if selection == '1':
            emailLookup = input("Please enter the name of the contact: ")
            if emailLookup in phonebook:
                print(phonebook[emailLookup])
            else:
                print ("Sorry. no contact exists under this name.")
        elif selection == '2':
            addContact = input("Please add a new name: ")
            if addContact in phonebook:
                print("Contact name already exists, please try again.")
            else:
                phonebook[addContact] = input("Enter a email address: ")
        elif selection == '3':
            changeEmail = input("Please enter the contact's name: ")
            if changeEmail in phonebook:
                phonebook[changeEmail] = input("Enter a new email address: ")
            else:
                print("Sorry, no contact exists under this name.")
                
        elif selection == '4':
            contactDelete = input("Please enter the name you wish to remove: ")
            if contactDelete in phonebook:
                del phonebook[contactDelete]
            else:
                print("Sorry, no contact exists under this name.")
            
        elif selection == '5':
            saveFile = str(input('Update dictionary? (Yes/No)'))
            if saveFile == 'Yes':
                file = input('Enter name of save file: ')
                with open(file, 'w') as saveData:
                    saveData.write(str(phonebook))
                print("Data saved. Have a nice day.")
                break
            else:
                print("Thank you and have a nice day")
                break
        else:
            print ("Please enter a valid menu option.")
addressBook()
