from tkinter import *
from tkinter import ttk
from diagram import *

class Infected(Button):
    '''
    class to create a custom button to show the infected cases
    for the last 7 days

    inherit the class Button from tkinter
    '''

    def show_data(self, data_in, country_in):
        '''
        opening a new window with the data of the corona cases
        for the last 7 days in a list

        :param data_in: list of lists
        :param country_in: string with the current country

        '''

        def popup_window(percentage_infected):
            '''
            pop-up for the warning message
            when the percentage of infected in the country > 0.01 %
            '''
            window = Toplevel()
            window.attributes('-topmost', True)
            window.title("Warning - MessageBox")
            window.iconbitmap("v1.ico")

            label = Label(window, text=f"WARNING\nPercentage infected = {percentage_infected} % !!", fg="red")
            label.config(font=("Arial", 14, "bold"))
            label.pack(fill='x', padx=50, pady=5)

            button_close = Button(window, text="Close", command=window.destroy, font=10)
            button_close.pack(fill='x')


        data = data_in
        country = country_in

        # creating window for the corona cases
        window = Tk()
        window.geometry("1250x470")
        window.title("Infections development")
        window.iconbitmap("v1.ico")

        frame = Frame(window, relief="flat", borderwidth=5)
        frame.pack(fill="both", expand=1)

        title_label = "Infections development in the last 7 days \n" + country.title()
        label = Label(frame, text=title_label)
        label.config(font=("Arial", 14, "bold"))
        label.pack(pady=20)

        frame_data = Frame(frame, relief="flat", borderwidth=1)
        frame_data.pack(pady=20, padx=30)

        corona_infections_table = ttk.Treeview(frame, columns=(1, 2, 3, 4, 5, 6), show='headings', height=10)
        corona_infections_table.pack(padx=10, pady=10)

        corona_infections_table.heading(1, text='Date')
        corona_infections_table.heading(2, text='Confirmed')
        corona_infections_table.heading(3, text='Death')
        corona_infections_table.heading(4, text='Recovered')
        corona_infections_table.heading(5, text='Active')
        corona_infections_table.heading(6, text='Change Active in %')


        # calculation and display of the increase of the active cases in relation with the previous day
        for index in range(len(data)):
            if index == 0:
                # no data from the previous date
                data[index].append('not available')
            else:
                change_active = round(((data[index][4] / data[index - 1][4]) - 1) * 100, 2)
                data[index].append(change_active)

        for value in range(len(data)):
            formatted_list_elements = list(map(lambda item: str(item).center(60), data[value]))
            corona_infections_table.insert('', 'end', values=formatted_list_elements)


        # calculation of the percentage of infections in the current country
        dict_citizens = {"germany": 83149300, "spain": 46764489, "austria": 9033859, "italy": 60026546}
        total_citizens = dict_citizens[country]

        total_confirmed = data[len(data) - 1][1]
        percentage_infected = round(total_confirmed * 100 / total_citizens, 2)

        if percentage_infected > 0.01:
            popup_window(percentage_infected)


        # "Go to Chart" button to show a diagram with active/recovered/death cases
        button_chart = Button(frame, text="Go to chart", width=10, height=2, bg="LightBlue")
        button_chart["command"] = lambda: diagram(data, country)
        button_chart.pack()

        # warning for special cases
        if country == "spain":
            label = Label(window, text="WARNING: The values of active and recovered may not be representative!\n"
                                       "These values should be cosidered together.")
            label.config(font=("Arial", 10, "bold"), fg="red")
            label.pack()

        window.mainloop()
