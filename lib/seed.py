import ipdb
from classes.customer import Customer
from classes.service import Service
from classes.meeting import Meeting
from random import sample
from faker import Faker
fake = Faker()



def drop_tables():
    Customer.drop_table()
    # Meeting.drop_table()
    # Service.drop_table()

def create_tables():
    Customer.create_table()
    # Meeting.create_table()
    # Service.create_table()

def seed_tables():
    pass
    
if __name__ == '__main__':
    drop_tables()
    create_tables()
    # ipdb.set_trace()

