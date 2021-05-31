import matplotlib.pyplot as plt
from last_seven_days import *

def diagram(data_in, country_in):
    '''
    opens a window showing a chart with the information of the last 7 days

    :param data_in: list of lists
    :param country_in: string with the current country
    '''

    data = data_in
    country = country_in

    death = []
    recovered = []
    active = []
    date = []

    for data_day in data:
        date.append(data_day[0][0:10])
        death.append(data_day[2])
        recovered.append(data_day[3])
        active.append(data_day[4])

    # openig a new window with the chart
    plt.figure(figsize=(8, 6)).canvas.set_window_title('Corona 7 days development')
    plt.title("Corona 7 days development\n" + str(country).title())
    plt.bar(date, death, color="red", label="Death")
    plt.bar(date, active, color="yellow", bottom=death, label="Activ")
    plt.bar(date, recovered, color="green", bottom=[sum(data) for data in zip(active, death)], label="Recovered")
    plt.ylabel("Number of citizens (Mio)")
    plt.xlabel("Date")

    plt.legend(loc="lower left", bbox_to_anchor=(0.8, 1.0))
    plt.show()
