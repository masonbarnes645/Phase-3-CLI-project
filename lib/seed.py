import ipdb
from classes.customer import Customer
from classes.service import Service
from classes.meeting import Meeting
from random import sample
from faker import Faker
fake = Faker()
from datetime import datetime, timedelta
import requests

start_date = datetime.today()
end_date = start_date + timedelta(days = 200)

companies =[
    'TechWave Solutions',
    'GreenLeaf Innovations',
    'BlueSky Enterprises',
    'Fusion Dynamics',
    'QuantumEdge Technologies',
    'EcoZen Industries',
    'SilverLine Ventures',
    'UrbanVista Designs',
    'AeroPulse Engineering',
    'NexaCore Systems'
]

descriptions = [
    'Offering advanced frameworks for optimizing business dynamics.',
    'Providing cutting-edge methodologies to streamline enterprise processes.',
    'Delivering transformative approaches to improve organizational effectiveness.',
    'Enabling multifaceted development opportunities through bespoke solutions.',
    'Utilizing progressive techniques to elevate operational metrics.',
    'Crafting tailored interventions to drive overarching success.',
    'Merging forward-thinking practices with existing frameworks for superior outcomes.',
    'Facilitating novel mechanisms to bolster corporate functionality.',
    'Implementing sophisticated strategies to enhance managerial performance.',
    'Offering broad-spectrum solutions to elevate business capabilities.',



]

typeMeet = [
    'Conference Call',
    'Phone Call',
    'In person meeting'
]


def drop_tables():
    Customer.drop_table()
    Meeting.drop_table()
    Service.drop_table()

def create_tables():
    Customer.create_table()
    Meeting.create_table()
    Service.create_table()

def seed_tables():
    for _ in range(25):
        try:
            Customer.create(fake.name(), sample(companies, 1)[0], fake.email())
        except Exception as e:
            print('Failed to create tables due to error', e)
    for _ in range(5):
        try:
            Service.create(fake.company(), sample(descriptions, 1)[0])
        except Exception as e:
            print('Failed to create tables due to error', e)
    for _ in range(40):

        try:
            customers = Customer.get_all()
            services = Service.get_all()
            Meeting.create(
                fake.date_between(start_date=start_date, end_date=end_date).strftime('%Y-%m-%d'),
                fake.time()[:5],
                sample(typeMeet,1)[0],
                sample(customers, 1)[0].id,
                sample(services, 1)[0].id,
                )
        except Exception as e:
            print('Failed to create tables due to error', e)


            
    
    
if __name__ == '__main__':
    drop_tables()
    create_tables()
    seed_tables()
    

