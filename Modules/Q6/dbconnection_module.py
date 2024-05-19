import psycopg2
class DataBaseConnection:
    def __init__(self, config:dict) -> None:
        self.config=config
        self.connection=None
        self.cursor=None

    def connect(self) -> None:
        self.connection=psycopg2.connect(**self.config)
    
    def create_cursor(self) -> None:
        self.cursor=self.connection.cursor()
    
    def close_cursor(self) -> None:
        self.cursor.close()

    def rollback(self) -> None:
        self.connection.rollback()

    def commit(self) -> None:        
        self.connection.commit()

    def close_connection(self) -> None:
        self.connection.close()

    def close(self) -> None:
        self.cursor.close()
        self.connection.close()