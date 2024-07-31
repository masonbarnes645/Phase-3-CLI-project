from classes.customer import Customer
from classes.service import Service
from classes.meeting import Meeting


def welcome():
    print("Welcome to Meeting Manager")

def exit_program():
    print("Goodbye!")
    exit()





def list_customers():
    customers = Customer.get_all()
    if customers:
        for customer in customers:
            print(customer.name)
    else:
        print("We have no customers in the system at this moment.")

def find_customer():
    name = input("Enter Customer Name:")
    if isinstance(name,str):
        customer = Customer.find_by_name(name)
        print(customer) if customer else print("We could not find a customer with that name.")

def new_customer():
    name = input("Enter Customer Name:")
    company = input("Enter Employer:")
    email = input("Enter Email:")

    try:
        customer = Customer.create(name, company, email)
        print(f"{customer.name} has been added to database")
    except Exception as e:
        print('Unexpected Error', e)
def delete_customer():
    name = input("Which customer would you like to remove? (Must be Exact Match):").strip()
    count1 = Customer.count_rows()
    try:
        Customer.remove_by_exact_match(name)
        count2 = Customer.count_rows()
    except Exception as e:
        print('Unexpected Error', e)
    if (count1 == count2):
        print("A customer with that name does not exist")
    else:
        print(f"{name.title()} has been removed from database")











def new_service():
    name = input("Enter Company Name:")
    description = input("Enter Service description:")


    try:
        service = Service.create(name, description)
        print(f"{service.name} has been added to database")
    except Exception as e:
        print('Unexpected Error', e)

def delete_service():
    name = input("Which company would you like to remove? (Must be Exact Match):").strip()
    count1 = Service.count_rows()
    try:
        Service.remove_by_exact_match(name)
        count2 = Service.count_rows()
    except Exception as e:
        print('Unexpected Error', e)
    if (count1 == count2):
        print("A company with that name does not exist")
    else:
        print(f"{name.title()} has been removed from database")

def list_services():
    services = Service.get_all()
    if services:
        for service in services:
            print(f"{service.name}")
    else:
        print("We do not offer any services currently.")

def learn_service():
    name = input("Which service would you like to learn more about?")
    print(Service.find_by_name(name))











def add_meeting():
    date = input("Please enter date of meeting (YYYY-MM-DD):")
    time = input("Please enter time of meeting (HH:MM):")
    type = input("Please enter the type of meeting (Conference Call, Phone Call, or In person meeting):")
    customer_id = input("Please enter Id of customer:")
    service_id = input("Please enter Id of service:")

    try:
        meeting = Meeting.create(date, time, type, customer_id, service_id)
        print(f"{meeting.date} has been added to database")
    except Exception as e:
            print('Unexpected Error', e)

def list_meeting():
    meetings = Meeting.get_all()
    if meetings:
        for meeting in meetings:
            print(f"{meeting.date}")
    else:
        print("We do not offer any services currently.")

def meetings_by_type():
    type = input("What type of meeting would you like to see?")
    meetings = Meeting.return_type_meetings(type)
    print(meetings)

def meetings_of_customers():
    name =  input("Enter Customer Name: ")
    print(Meeting.customer_meeting_join(name))

def meetings_by_date(): 
    MBD = Meeting.sort_by_date()
    print(MBD)

def num_meetings_by_service():
    service = input("What type of meeting would you like to see?")
    MBS = Meeting.service_meeting_join(service)
    print(MBS)

def delete_meeting():
    id = input("Please enter the id of the meeting you would like to remove:").strip()
    count1 = Meeting.count_rows()
    try:
        Meeting.remove_by_exact_match(id)
        count2 = Meeting.count_rows()
    except Exception as e:
        print('Unexpected Error', e)
    if (count1 == count2):
        print("A meeting with that id does not exist")
    else:
        print(f"Meeting number {id} has been removed from database")
    




