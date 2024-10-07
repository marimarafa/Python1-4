class DataBaseConnection:
    def __init__(self,db_name) -> None:
        self.db_name = db_name
        self.connection = None

    def connect(self):
        print(f"Connecting to database :{self.db_name}")
        self.connection = f'Connection to {self.db_name}'

    def disconnect(self):
        print(f"Disconnecting from database: {self.db_name}")
        self.connection = None
    
    def commit(self):
        print("Committing transaction")

    def rollback(self):
        print("Rolling back transaction")

    def axecute_query(self,query):
        print(f"Executing query: {query}")
        return f'Results of {query}'
    
class DataBaseContextManager:
    def __init__(self,db_name) -> None:
        self.db= DataBaseConnection(db_name)

    def __enter__(self):

        self.db.connect()
        return self.db
    def __exit__(self,exc_type,exc_value,traceback):
        if exc_type is not None:
            self.db.rollback()
            print(f"Exception type: {exc_type}")
            print(f"Exception value: {exc_value}")
            print(f"Traceback: {traceback}")
        else:
            self.db.commit()
        self.db.disconnect()
        return False

def main():
    db_name = "example.db"
    query = "SELECT * FROM users"

    try:
        with DataBaseContextManager(db_name) as db:
            results = db.execute_query(query)
            print(f'Query results : {results}')

    except Exception as e:
        print(f'Caught an exception: {e}')
    
main()