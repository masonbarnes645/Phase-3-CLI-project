from classes.__init__ import CURSOR, CONN
import re
from .customer import Customer
from .service import Service


class Meeting:
    all = {}
    def __init__(self, date, time, type, customer_id, service_id, id = None):
        self.date = date
        self.time = time
        self.type = type
        self.customer_id = customer_id
        self.service_id = service_id
        self.id = id
    
    @property
    def date(self):
        return self._date
    

    @date.setter
    def date(self,date):
        datepattern = r"^(?:(?:[0-9]{4})-(?:(?:0[1-9]|1[0-2])-(?:0[1-9]|1[0-9]|2[0-9]|3[01])))$"
        if not re.search(datepattern,date):
            raise ValueError("Dates must be entered YYYY-MM-DD")
        else:
            self._date = date
        
    @property
    def time(self):
        return self._time
    
    @time.setter
    def time(self,time):
        timepattern = r"^(?:[01]\d|2[0-3]):[0-5]\d$"
        if not re.search(timepattern, time):
            raise ValueError("Time must be in 24 hour format and structured as follows: HH:MM")
        else:
            self._time = time

    @property
    def type(self):
        return self._type
    
    @type.setter
    def type(self,type):
        valid_type = ["Conference Call", "Phone Call", "In person meeting"]
        if type not in valid_type:
            raise ValueError("Please enter a valid meeting type")
        else:
            self._type = type

    @property
    def customer_id(self):
        return self._customer_id
    
    @customer_id.setter
    def customer_id(self, customer_id):
        ids = Customer.get_all()
        
        if Customer.customer_id_exists(customer_id):
            self._customer_id = customer_id
            
        else:
            raise ValueError("Please enter valid customer id")
        
    @property
    def service_id(self):
        return self._service_id
    
    @service_id.setter
    def service_id(self, service_id):

        
        if Service.service_id_exists(service_id):
            self._service_id = service_id
            
        else:
            raise ValueError("Please enter valid service id")






    @classmethod
    def create(cls, date, time, type, customer_id, service_id):
        newDBM = cls(date, time, type, customer_id, service_id)
        newDBM.save()
        return newDBM     
    
    
    @classmethod
    def create_table(cls):
        try:
            CURSOR.execute(
                """
                CREATE TABLE IF NOT EXISTS meetings (
                    id INTEGER PRIMARY KEY,
                    date TEXT,
                    time TEXT,
                    type TEXT,
                    customer_id INTEGER,
                    service_id INTEGER
                    
                );
                """
            )
            CONN.commit()
        except Exception as e:
            CONN.rollback()
            print(f"Unexpected Error: {e}")
    @classmethod
    def drop_table(cls):
        try:
            CURSOR.execute(
                """
                DROP TABLE IF EXISTS meetings
                """
            )
            CONN.commit()
        except Exception as e:
            CONN.rollback()
            print(f"Unexpected Error: {e}")
    
    @classmethod
    def create(cls, date, time, type, customer_id, service_id):
        newMeet = cls( date, time, type, customer_id, service_id)
        newMeet.save()
        return newMeet

    def save(self):
        try:
            CURSOR.execute(
                """
                INSERT INTO meetings (date, time, type, customer_id, service_id)
                VALUES (?, ?, ?, ?, ?)
                """,
                (self.date, self.time, self.type, self.customer_id, self.service_id),
            )
            CONN.commit()
            self.id = CURSOR.lastrowid
            type(self).all[self.id] = self
            return self
        except Exception as e:
            CONN.rollback()
            print(f"Unexpected Error: {e}")
    
    @classmethod
    def return_type_meetings(cls, type):
        CURSOR.execute(
        """
        SELECT *
        FROM meetings 
        WHERE type == ?
        """,(type,))
        rows = CURSOR.fetchall()
        results = [cls(row[1], row[2], row[3], row[4], row[5], row[0]) for row in rows]
        return [(f'{type}: {result.date}: {result.time}') for result in results]
    
    @classmethod
    def sort_by_date(cls):
        CURSOR.execute(
            """
            SELECT *
            FROM meetings
            ORDER BY date ASC
"""
        )
        rows = CURSOR.fetchall()
        results = [cls(row[1], row[2], row[3], row[4], row[5], row[0]) for row in rows]
        return [(f'{result.date}: {result.time}') for result in results]
    
    @classmethod
    def customer_meeting_join(cls, name):
        try:
            CURSOR.execute(
            """
            SELECT date, type FROM meetings 
            INNER JOIN customers ON meetings.customer_id = customers.id
            WHERE customers.name == ?
            """,(name,))
            meetings = CURSOR.fetchall()
            return meetings
        except Exception as e:
            return e
    
    @classmethod
    def service_meeting_join(cls,name):
        try:
            CURSOR.execute(
            """
            SELECT date, type FROM meetings 
            INNER JOIN services ON meetings.service_id = services.id
            WHERE services.name == ?
            """,(name,))
            meetings = CURSOR.fetchall()
            return meetings
        except Exception as e:
            return e
    @classmethod
    def remove_by_exact_match(cls, id):
        try:
            CURSOR.execute(
                """
            DELETE FROM meetings
            WHERE id == ? 
                """, (id,)
            )
            CONN.commit()
        except Exception as e:
            CONN.rollback()
            print(f"Unexpected Error: {e}")

    def count_rows():
        CURSOR.execute(
        """
        SELECT COUNT(*)
        FROM meetings
        """)
        count = CURSOR.fetchone()[0]
        return count
    

    @classmethod
    def get_all(cls):
        CURSOR.execute(
            """
            SELECT * FROM meetings; 
        """
        )
        rows = CURSOR.fetchall()
        return [cls(row[1], row[2], row[3], row[4], row[5], row[0]) for row in rows]

        



