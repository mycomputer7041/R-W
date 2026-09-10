
            
#---------------


import os
from datetime import datetime

class gunral_managae:
    """
    Main class for managing personal journal entries.
    Handles saving, reading, searching, and deleting entries in a text file.
    """

    def __init__(self):
        """
        Sets the default filename when class is initialized
        arguments: none
        returns: nothing
        """
        self.filename = "journal.txt"

    def add_j(self):
        """
        Adds a new journal entry with current date and time
        arguments: none
        returns: nothing
        """
        print("Welcome to Personal jounal manager")
        a = input("enter youe journal entry")

        # Gets current date and time format
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Appends new entry to the file
        with open(self.filename, "a") as file:
            file.write(f"[{timestamp}]\n{a}")
        print("add sucessfuly")

    def read_j(self):
        """
        Reads and prints all entries from the journal file
        arguments: none
        returns: nothing
        """
        try:
            with open(self.filename, "r") as file:
                print(file.read())
        except FileNotFoundError:
            # Displays error if file does not exist
            print("error: the file are a not exit")

    def search_j(self):
        """
        Searches entries by keyword or date string
        arguments: none
        returns: nothing
        """
        keyword = input("\nEnter a keyword or date to search: ").strip()
        try:
            with open(self.filename, "r") as file:
                # Splits content into separate entries
                entries = file.read().split("\n\n")
                
                # Filters entries containing matching keyword
                matched = [e for e in entries if keyword.lower() in e.lower() and e.strip()]
                
                if matched:
                    print("\nMatching Entries:")
                    print("-" * 35)
                    for entry in matched:
                        print(entry)
                    print("-" * 35 + "\n")
                else:
                    print(f"\nNo entries were found for the keyword: {keyword}\n")
        except FileNotFoundError:
            print("\nError: The journal file does not exist. Please add a new entry first.\n")

    def delete_j(self):
        """
        Deletes the entire journal file after user confirmation
        arguments: none
        returns: nothing
        """
        # Checks if journal file exists
        if not os.path.exists(self.filename):
            print("\nNo journal entries to delete.\n")
            return

        confirm = input("\nAre you sure you want to delete all entries? (yes/no): ").strip().lower()
        if confirm == 'yes':
            # Removes file from disk
            os.remove(self.filename)
            print("All journal entries have been deleted.\n")
        else:
            print("Deletion cancelled.\n")



# Creates class instance
journal = gunral_managae()

# Continuous menu loop
while True:
    """
    Displays menu options and calls functions based on user choice
    """
    print("Welcome to Personal Journal Manager!")
    print("Please select an option:")
    print("1. Add a New Entry")
    print("2. View All Entries")
    print("3. Search for an Entry")
    print("4. Delete All Entries")
    print("5. Exit")

    choice = input("User Input: ").strip()

    if choice == '1':
        journal.add_j()      # Calls add entry method
    elif choice == '2':
        journal.read_j()     # Calls view all entries method
    elif choice == '3':
        journal.search_j()   # Calls search method
    elif choice == '4':
        journal.delete_j()   # Calls delete method
    elif choice == '5':
        print("\nThank you for using Personal Journal Manager. Goodbye!")
        break                # Exits the application loop
    else:
        print("\nInvalid option. Please select a valid option from the menu.\n")

        

