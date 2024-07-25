from classes.__init__ import CURSOR, CONN 
class Service:
    def __init__(self, name, description, id = None):
        self.name = name
        self.description = description
        self.id = id
        
        
    @classmethod
    def create_table(cls):
        CURSOR.execute(
            """
            CREATE TABLE IF NOT EXISTS service (
                id INTEGER PRIMARY KEY,
                name TEXT
                description TEXT
            );
        """
        )
        CONN.commit()
    
    @classmethod
    def drop_table(cls):
        CURSOR.execute(
            """
            DROP TABLE IF EXISTS service
            """
        )
        CONN.commit()
    