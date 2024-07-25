from classes.__init__ import CURSOR, CONN 

class Customer:
    def __init__(self, name, company, email, id = None):
        self.name = name
        self.company = company
        self.email = email

    @property
    def name(self):
        return  self._name
    @name.setter
    def name(self, name):
        firstlast = name.split()
        if not isinstance(name, str):
                raise TypeError("Customer Name must be string")
        elif not len(firstlast) > 1:
                raise ValueError("Please include customer's first and last name")
        else:
            self._name = name

    @classmethod
    def create_table(cls):
        try:
            CURSOR.execute(
                """
                CREATE TABLE IF NOT EXISTS customer (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    company TEXT,
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
            DROP TABLE IF EXISTS customer
            """
        )
        CONN.commit()
    
    
    
    
    
