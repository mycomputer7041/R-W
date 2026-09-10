import os
from datetime import datetime


class gunral_managae:
    def __init__(self):
        self.filename = "journal.txt"

    def add_j(self):
        print("Welcome to Personal jounal manager")
        a=input("enter youe journal entry")

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(self.filename, "a") as file:
            file.write(f"[{timestamp}]\n{a}")
        print("add sucessfuly")
    def read_j(self):
        try:
            with open(self.filename, "r") as file:
                print(file.read())
        except FileNotFoundError:
            print("error: the file are a not exit")
    def search_j(self):
        keyword = input("\nEnter a keyword or date to search: ").strip()
        try:
            with open(self.filename, "r") as file:
                entries = file.read().split("\n\n")
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
        
        if not os.path.exists(self.filename):
            print("\nNo journal entries to delete.\n")
            return

        confirm = input("\nAre you sure you want to delete all entries? (yes/no): ").strip().lower()
        if confirm == 'yes':
            os.remove(self.filename)
            print("All journal entries have been deleted.\n")
        else:
            print("Deletion cancelled.\n")
journal = gunral_managae()

while True:
    print("Welcome to Personal Journal Manager!")
    print("Please select an option:")
    print("1. Add a New Entry")
    print("2. View All Entries")
    print("3. Search for an Entry")
    print("4. Delete All Entries")
    print("5. Exit")

    choice = input("User Input: ").strip()

    if choice == '1':
        journal.add_j()
    elif choice == '2':
        journal.read_j()
    elif choice == '3':
        journal.search_j()
    elif choice == '4':
        journal.delete_j()
    elif choice == '5':
        print("\nThank you for using Personal Journal Manager. Goodbye!")
        break
    else:
        print("\nInvalid option. Please select a valid option from the menu.\n")
            


        

