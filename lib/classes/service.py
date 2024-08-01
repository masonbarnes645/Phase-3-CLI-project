import ipdb
import re
from classes.__init__ import CURSOR, CONN 
class Service:
    all={}
    
    def __init__(self, name, description, id = None):
        self.name = name
        self.description = description
        self.id = id
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if len(name) > 40:
            raise ValueError("Company name is too long")
        else:
            self._name = name

    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self,description):
        if len(description) < 5:
            raise ValueError("Please enter a longer description")
        else:
            self._description = description
    
    
    
    @classmethod
    def create(cls, name, description):
        newDBS = cls(name, description)
        newDBS.save()
        return newDBS     


    @classmethod
    def get_all(cls):
        CURSOR.execute(
            """
            SELECT * FROM services; 
        """
        )
        rows = CURSOR.fetchall()
        return [cls(row[1], row[2], row[0]) for row in rows]

    @classmethod
    def service_id_exists(cls, id):
        CURSOR.execute("SELECT 1 FROM services WHERE id = ?;", (id,))
        result = CURSOR.fetchone()
        return result is not None

    
    @classmethod
    def create_table(cls):
        try:
            CURSOR.execute(
                """
                CREATE TABLE IF NOT EXISTS services (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    description TEXT UNIQUE
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
                DROP TABLE IF EXISTS services
                """
            )
            CONN.commit()
        except Exception as e:
            CONN.rollback()
            print(f"Unexpected Error: {e}")

    @classmethod
    def create(cls, name, description):
        newService = cls(name, description)
        newService.save()
        return newService

    def save(self):
        try:
            CURSOR.execute(
                """
                INSERT or REPLACE INTO services (name, description)
                VALUES (?, ?)
                """,
                (self.name, self.description),
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
          SELECT * FROM services
          WHERE name LIKE '%' || ? || '%' --case-insensitive
            """, (name,)
        )
        
        rows = CURSOR.fetchall()
        results = [cls(row[1], row[2]) for row in rows] if rows else []
        return [(f'{result.name}: {result.description}') for result in results]
    
    @classmethod
    def remove_by_exact_match(cls, name):
        try:
            CURSOR.execute(
                """
            DELETE FROM services
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
        FROM services
        """)
        count = CURSOR.fetchone()[0]
        return count


    