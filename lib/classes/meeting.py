from classes.__init__ import CURSOR, CONN 

class Meeting:
    def __init__(self, name, date, time, type, customer_id, service_id, id = None):
        self.name = name
        self.date = date
        self.time = time
        self.type = type
        self.customer_id = customer_id
        self.service_id = service_id
        self.id = id
    @classmethod
    def create_table(cls):
        try:
            CURSOR.execute(
                """
                CREATE TABLE IF NOT EXISTS meeting (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    date TEXT,
                    time TEXT
                    type TEXT
                    customer_id INTEGER
                    service_id INTEGER
                    
                    email TEXT
                );
                """
            )
            CONN.commit()
        except Exception as e:
            return e
        
    @classmethod
    def drop_table(cls):
        CURSOR.execute(
            """
            DROP TABLE IF EXISTS meeting
            """
        )
        CONN.commit()