# author: blv
# Description: OOP address book

# welcome screen
print("-------------Welcome to the CELLS Contact Book-------------")
print("Enter your contact's information")
#
# # Vars for person/info objects
# first_name = input("First name = ")
# last_name = input("Last name = ")
# age = input("Age = ")
# phone_number = input("Phone number = ")
# twitter = input("Twitter = ")
# instagram = input("Instagram = ")
#
# # input confirmation
# print("Thank you for your input! We've received your contacts information.")


# Class def


class Person:
    def __init__(self, first, last, contact_age, contact_phone_number,
                 contact_twitter, contact_instagram):
        self.first = first
        self.last = last
        self.age = contact_age
        self.phone_number = contact_phone_number
        self.twitter = twitter
        self.instagram = instagram

    # full name

    def full_name(self):
        return f'{self.first} {self.last}'  # clean full name print

    # converting ppl objects into printable strings

    def __str__(self):
        return f"{self.first} {self.last}{','} {self.age}{','} {self.phone_number}{','} " \
               f"{self.twitter}{','} {self.instagram}"


contacts = list()

user_input = ""

while user_input != "q":
    print("Available actions")
    print("1 - Enter a contact")  # should be Roman numerals?
    print("2 - Display contacts")
    print("3 - Find Contact")
    print("q - Quit program")
    user_input = input("Select an action: ")

    if user_input == "1":
        print("Enter your contact's information")
        first_name = input("First name = ")
        last_name = input("Last name = ")
        age = input("Age = ")
        phone_number = input("Phone number = ")
        twitter = input("Twitter = ")
        instagram = input("Instagram = ")

        our_contact = Person(first_name, last_name, age, phone_number, twitter, instagram)
        contacts.append(our_contact)  # storing contacts into memory
        print("Thank you for your input! We've received your contacts information.")
    elif user_input == "2":
        for cont in contacts:
            print(cont)
        input("Contacts displayed! Hit 'ENTER' to continue...")
    elif user_input == "3":
        search_cont = input("Enter contact's name to search\n")
        for cont in contacts:
            if search_cont.lower() in cont.full_name():
                print(cont)
    elif user_input.lower() == "q":
        break

print("Thank you for using the CELL Address Book.")


our_contact = Person(first_name, last_name, age, phone_number, contact_twitter=twitter, contact_instagram=instagram)
# print(our_contact)
