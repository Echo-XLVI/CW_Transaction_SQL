from dbconnection_module import DataBaseConnection

class ContextManager:
    def __init__(self, config:dict) -> None:
        self.config=config
        self.connection_obj=None

    def __enter__(self) -> object:
        self.connection_obj = DataBaseConnection(self.config)
        self.connection_obj.connect()
        self.connection_obj.create_cursor()
        return self.connection_obj

    def __exit__(self, exc_type, exc_value, exc_traceback) -> None:
        if  exc_type or exc_value or exc_traceback:
            print(exc_value)
            self.connection_obj.rollback()
        else:
            self.connection_obj.commit()
        self.connection_obj.close_cursor()    