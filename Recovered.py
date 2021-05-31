from tkinter import *

class Recovered(Button):

    def show_recover(self, data_in, country_in):
        '''
        opening a new window with the % of recovered cases

        :param data_in: list of lists
        :param country_in: string with the current country

        '''

        data = data_in
        country = country_in

        # creating window for the recovered cases
        window = Tk()
        window.geometry("500x300")
        window.title("Recovered citizens")
        window.iconbitmap("v1.ico")

        frame = Frame(window, relief="flat", borderwidth=5)
        frame.pack(fill="both", expand=1)


        # calculation of the percentage of recovered cases
        dict_citizens = {"germany": 83149300, "spain": 46764489, "austria": 9033859, "italy": 60026546}
        total_citizens = dict_citizens[country]

        recovered = data[len(data)-1][3]
        percentage_recovered = recovered * 100 / total_citizens


        title_label = "Total recovery in \n" + country.title()
        label = Label(frame, text=title_label)
        label.config(font=("Arial", 14, "bold"))
        label.pack(pady=20)

        text_label = "Total recovery in %: " + str(round(percentage_recovered,2)) + " %"
        label = Label(frame, text=text_label)
        label.config(font=("Arial", 12, "bold"))
        label.pack(pady=20)

        text_label = "Percentage calculated from total of " + str(total_citizens) + \
                     " citizens\n" + str( "and ") + str(recovered) + str(" recovered citizens.")

        label = Label(frame, text=text_label)
        label.config(font=("Arial", 10, "bold"))
        label.pack(pady=40)

        window.mainloop()
