import sqlite3


class CoronaDatabase():
    '''
    database to save the actual corona cases
    '''

    def __init__(self):
        '''
        Establishes a connection to the database,
        creates a database file if it does not exist
        '''
        self.Connection = sqlite3.connect("database_corona.sqlite3")
        try:
            self.createTable()
        except sqlite3.OperationalError:
            pass

    def createTable(self):
        '''
        Creates a table for providing corona data in the corona database.
        '''
        cursor = self.Connection.cursor()
        query = f'''
                    CREATE TABLE corona (
                        id INTEGER PRIMARY KEY,
                        country VARCHAR(200),
                        date VARCHAR(200),
                        confirmed VARCHAR(200),
                        death VARCHAR(200),
                        recovered VARCHAR(200),
                        active VARCHAR(200)
                    );
                    '''
        cursor.execute(query)
        self.Connection.commit()

    def getData(self):
        '''
        Retrieves all data from corona table
        '''
        cursor = self.Connection.cursor()
        select_query = '''
            SELECT * FROM corona
        '''
        cursor.execute(select_query)
        data = cursor.fetchall()

        return data

    def insertManyData(self, country, date, confirmed, death, recovered, active):
        '''
        Saves data into corona table for not existing data
        '''
        cursor = self.Connection.cursor()

        # checks if a date already exits
        select_query = f'''
                    SELECT id FROM corona
                    WHERE country = "{country}" AND date = "{date}"
                '''
        cursor.execute(select_query)
        result = cursor.fetchall()

        # if nothing found, insert data:
        if not result:
            insert_query = f'''
                        INSERT INTO corona (id, country, date, confirmed, death, recovered, active)
                        VALUES (NULL, "{country}", "{date}", "{confirmed}", "{death}", "{recovered}", "{active}");
                        '''
            cursor.execute(insert_query)
            self.Connection.commit()


    def deleteRowsFromTable(self, ID):
        '''
        Deletes data from the corona table giving an id
        '''
        cursor = self.Connection.cursor()
        delete_query = f'''
            DELETE FROM corona
            WHERE ID = "{ID}"
        '''
        cursor.execute(delete_query)
        self.Connection.commit()

    def deleteAllFromTable(self):
        '''
        Delete all data from the corona table
        '''
        cursor = self.Connection.cursor()
        delete_query = f'''
            DELETE FROM corona
        '''
        cursor.execute(delete_query)
        self.Connection.commit()

#--------------------------------------------------------------------------------
## For testing:
# my_test = CoronaDatabase()
#print(my_test.getData())
#my_test.deleteAllFromTable()

#data = last_seven_days('germany')
#my_test.insertManyData(data)
#print(my_test.getData())