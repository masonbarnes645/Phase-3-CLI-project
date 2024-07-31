# lib/cli.py

from helpers import (
    exit_program,
    list_customers,
    find_customer,
    new_customer,
    meetings_by_date,
    num_meetings_by_service,
    meetings_by_type,
    list_services,
    delete_customer,
    meetings_of_customers,
    learn_service,
    new_service,
    delete_service,
    delete_meeting,
    add_meeting,
    list_meeting
    
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            customer_menu()
        elif choice == "2":
            service_menu()
        elif choice == "3":
            meeting_menu()
        else:
            print("Invalid choice")

def customer_menu():
    while True:    
        print("Customer Menu:")
        print("0. Back to Main Menu")
        print("1. List of Customers")
        print("2. Search For Customer")
        print("3. Add New Customer to Database")
        print("4. Remove Customer from Database")
        print("5. Exit Program")
        choice = input("> ")
        if choice == "0":
            break
        elif choice == "1":
            list_customers()
        elif choice == "2":
            find_customer()
        elif choice == "3":
            new_customer()
        elif choice == "4":
            delete_customer()
        elif choice == "5":
            exit_program()
            
def service_menu():
    while True:    
        print("Service Menu:")
        print("0. Back to Main Menu")
        print("1. List of Services")
        print("2. Learn More about a Service")
        print("3. Add new service")
        print("4. Delete Service")
        print("5. Exit Program")
        choice = input("> ")
        if choice == "0":
            break
        elif choice == "1":
            list_services()
        elif choice == "2":
            learn_service()
        elif choice == "3":
            new_service()
        elif choice == "4":
            delete_service()
        elif choice == "5":
            exit_program()

def meeting_menu():
    while True:    
        print("Meeting Menu:")
        print("0. Back to Main Menu")
        print("1. List of Meetings")
        print("2. List of Meetings by Type")
        print("3. List of Meetings by Date")
        print("4. List of Meetings for Service")
        print("5. List of Meetings for Customer")
        print("6. Add New Meeting")
        print("7. Remove Meeting")
        print("8. Exit Program")
        choice = input("> ")
        if choice == "0":
            break
        elif choice == "1":
            list_meeting()
        elif choice == "2":
            meetings_by_type()
        elif choice == "3":
            meetings_by_date()
        elif choice == "4":
            num_meetings_by_service()
        elif choice == "5":
            meetings_of_customers()
        elif choice == "6":
            add_meeting()
        elif choice == "7":
            delete_meeting()
        elif choice == "8":
            exit_program()
            
        
def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Customer Menu")
    print("2. Services Menu")
    print("3. Meetings Menu")
   


if __name__ == "__main__":
    main()
