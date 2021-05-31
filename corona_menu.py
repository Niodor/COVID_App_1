# User Interface
#####################################
#                   #               #
# 7 days incidence  #   Recovered   #
#                   #               #
#####################################
#                                   #
#               Update              #
#                                   #
#####################################

from tkinter import *
from Infected import *
from Update import *
from Recovered import *
from last_seven_days import *


def change_country(event):
    '''
    function to change the global variable "country"
    depending on the OptionMenu (dropdown)
    and get the dta from the last 7 days
    '''
    country_id = clicked.get()
    country_dict = {"DE": "germany", "IT": "italy", "AT": "austria", "ES": "spain"}
    global country
    global data
    country = country_dict[country_id]
    data = last_seven_days(country)


# create Main Window
window = Tk()
window.geometry("700x360")
window.title("Corona Virus Resource Center")
window.iconbitmap("v1.ico")

frame = Frame(window, relief="flat", borderwidth=5)
frame.pack(fill="both", expand=1)


# adding menu-bar and Exit-button
menu = Menu(window)
window.config(menu=menu)

filemenu = Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Exit", command=window.destroy)


# including image to background
C = Canvas(frame, bg="blue", height=250, width=300)
filename = PhotoImage(file="coronavirus-origine.gif")
background_label = Label(frame, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
C.place()


# adding upper-label to window
label = Label(frame, text="Corona Virus Resource Center")
label.config(font=("Arial", 18, "bold"), bg='LightBlue')
label.place(x=180, y=10)


# adding Option-Menu for the different countries
country = "germany"
options = ('DE', 'IT', 'AT', 'ES')
clicked = StringVar()
clicked.set('DE')

drop_menu = OptionMenu(window, clicked, *options, command=change_country)
drop_menu.place(x=20, y=20)


# calling data for the default country (Germany)
data = last_seven_days(country)


# adding button infected
button_infected = Infected(frame, text="7 days incidence", width=20, height=5)
button_infected.config(font=("Arial", 14, "bold"))
button_infected['command'] = lambda: button_infected.show_data(data, country)
button_infected.place(x=85, y=50)

# adding button recovered
button_recovered = Recovered(frame, text="Recovered", width=20, height=5)
button_recovered.config(font=("Arial", 14, "bold"))
button_recovered['command'] = lambda: button_recovered.show_recover(data, country)
button_recovered.place(x=380, y=50)

# adding button update
button_update = Update(frame, text="Update database", width=20, height=5)
button_update.config(font=("Arial", 14, "bold"))
button_update['command'] = lambda: button_update.update(data, country)
button_update.place(x=240, y=200)

window.mainloop()
