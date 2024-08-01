from classes.__init__ import CURSOR, CONN
import ipdb
import re

class Customer:
    
    all={}
    def __init__(self, name, company, email, id=None):
        self.name = name
        self.company = company
        self.email = email
        self.id = id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        firstlast = name.split()
        if not isinstance(name, str):
            raise TypeError("Customer name must be a string")
        elif not re.fullmatch(r'[a-zA-Z  -]+', name):
            raise TypeError("Invalid characters used in name")
        elif not len(firstlast) > 1:
            raise ValueError("Please include customer's first and last name")
        elif len(name) > 40:
            raise ValueError("Customer name is too long")
        else:
            self._name = name

    @property
    def company(self):
        return self._company
    
    @company.setter
    def company(self, company):
        if not isinstance(company, str):
            raise TypeError("Company name must be a string")
        if len(company) > 40:
            raise ValueError("Company name is too long")
        else:
            self._company = company

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        emailpattern = "[a-zA-Z0-9]+@[a-zA-Z]+\.(com|edu|net|org)"
        if not re.search(emailpattern, email):
            raise ValueError("Please enter valid email address")
        else:
            self._email= email
    
    @classmethod
    def create(cls, name, company, email):
        newDBC = cls(name, company, email)
        newDBC.save()
        return newDBC
    
    def delete(self):
        try:
            CURSOR.execute(
                    """
                DELETE FROM customer
                where id = ?
                        """,(self.id,))
            CONN.commit()
            del type(self).all[self.id]
            self.id = None
            return self
        except Exception as e:
            CONN.rollback()
            print("Unexpected Error")       

    
    @classmethod
    def get_all(cls):
        CURSOR.execute(
            """
            SELECT * FROM customers; 
        """
        )
        rows = CURSOR.fetchall()
        return [cls(row[1], row[2], row[3], row[0]) for row in rows]
    
    @classmethod
    def customer_id_exists(cls, id):
        CURSOR.execute("SELECT 1 FROM customers WHERE id = ?;", (id,))
        result = CURSOR.fetchone()
        return result is not None



    @classmethod
    def create_table(cls):
        try:
            CURSOR.execute(
                """
                CREATE TABLE IF NOT EXISTS customers (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    company TEXT,
                    email TEXT UNIQUE
                );
                """
            )
            CONN.commit()
        except Exception as e:
            CONN.rollback()
            print("Unexpected Error")   

    @classmethod
    def drop_table(cls):
        try:
            CURSOR.execute(
                """
                DROP TABLE IF EXISTS customers;
                """
            )
            CONN.commit()
        except Exception as e:
            CONN.rollback()
            print(f"Unexpected Error: {e}")

    @classmethod
    def create(cls, name, company, email):
        newCust = cls(name, company, email)
        newCust.save()
        return newCust

    def save(self):
        try:
            CURSOR.execute(
                """
                INSERT INTO customers (name, company, email)
                VALUES (?, ?, ?)
                """,
                (self.name, self.company, self.email),
            )
            CONN.commit()
            self.id = CURSOR.lastrowid
            type(self).all[self.id] = self
            return self
        except Exception as e:
            CONN.rollback()
            print(f"Unexpected Error: {e}")
    @classmethod
    def find_by_name(cls, name):
        CURSOR.execute(
            """
          SELECT * FROM customers
          WHERE name LIKE '%' || ? || '%' --case-insensitive
            """, (name,)
        )
        
        rows = CURSOR.fetchall()
        results = [cls(row[1], row[2], row[3]) for row in rows] if rows else []
        return [(f'{result.name}: {result.email}') for result in results]
    
    @classmethod
    def find_by_id(cls, id):
        CURSOR.execute(
            """
          SELECT * FROM customers
          WHERE id == ?
            """, (id,)
        )
        rows = CURSOR.fetchall()
        results = [cls(row[1], row[2], row[3]) for row in rows] if rows else []
        return [(f'{result.name}: {result.email}') for result in results]
    
    @classmethod
    def remove_by_exact_match(cls, name):
        try:
            CURSOR.execute(
                """
            DELETE FROM customers
            WHERE name == ? 
                """, (name,)
            )
            CONN.commit()
        except Exception as e:
            CONN.rollback()
            print(f"Unexpected Error: {e}")

        


    def count_rows():
        CURSOR.execute(
        """
        SELECT COUNT(*)
        FROM customers
        """)
        count = CURSOR.fetchone()[0]
        return count