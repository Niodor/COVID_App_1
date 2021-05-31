from tkinter import *
from Corona_database import *

class Update(Button):

    def update(self, data_in, country_in):
        '''
        updates the data in the sql-table with the actual data
        :param data_in: list of lists
        :param country_in: string with the current country

        '''

        data = data_in
        country = country_in

        # create instance of database and inserts data
        my_database = CoronaDatabase()

        for data_day in data:
            date = data_day[0]
            confirmed = data_day[1]
            death = data_day[2]
            recovered = data_day[3]
            active = data_day[4]

            my_database.insertManyData(country, date, confirmed, death, recovered, active)

        # my_database.deleteAllFromTable()
