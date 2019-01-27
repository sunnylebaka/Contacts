import os
import json
class phBook:
    # Adds contacts to the file named contacts.txt
    def add_contacts(self):
        name = input('Name: ')
        number = input('Number: ')
        Email = input('Email: ')
        # appends number and Email to the specified name in dict format.
        contact[name]=[number, Email]
        # opens a file Phone_book.txt and appends the details given by the user.
        Phone_book = open('Phone_book.txt','a')
        Phone_book.write(str(contact)+'\n')
        Phone_book.close()

    # Shows all the contacts in the Phone_book.txt file.
    def View_contacts(self):
        # reads all the data in the Phone_book.txt file.
        Phone_book = open('Phone_book.txt','r')
        for lines in Phone_book:
            x = lines.split("'")
            name = x[1]
            Ph_number  = x[3]
            Email = x[5]
            print('Name: ', name)
            print('Phnumber: ', Ph_number)
            print('Email: ', Email+'\n')
        # Prints all the data in the contacts.txt file.
        Phone_book.close()
    # Searches for the contact in contacts.txt file that user wants.
    def search_contacts(self):
        name = input('Enter a name to search: ')
        Phone_book = open('Phone_book.txt','r')
        for line in Phone_book:
            if name in line:
                x = line.split("'")
                a = x[3]
                b = x[5]
                print('Name: ', name)
                print('Phnumber: ', a)
                print('Email: ', b)
            else:
                print('Contact found')
        Phone_book.close()

    def options(self):
        choice=int(input('Enter your choice: '))
        if (choice == 1):
            self.add_contacts()
        elif (choice == 2):
            self.View_contacts()
        elif (choice == 3):
            self.search_contacts()
contact = {}
print('''1 = add_contacts
2 = View_contacts
3 = search_contacts''')
l = phBook()
l.options()
