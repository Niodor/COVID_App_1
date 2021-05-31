import requests
import datetime


def last_seven_days(country):
    '''
    Function for the output of the last seven days of a country, with the values: confirmed cases,
    active cases, recovered cases, deceased cases.

    Use datetime to get the data from the last 7 days
    the function gets the data starting from the current date -1
    :param country: string with the current country
    :return: days - list of lists
    '''

    yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
    seven_days = yesterday.now() - datetime.timedelta(days=8)
    date_yesterday = str(yesterday.strftime("%Y")) + "-" + str(yesterday.strftime("%m")) \
                  + "-" + str(yesterday.strftime("%d")) + "T00:00:00Z"
    date_before_seven_days = str(seven_days.strftime("%Y")) + "-" + str(seven_days.strftime("%m")) \
                             + "-" + str(seven_days.strftime("%d")) + "T00:00:00Z"

    # building Web-Request and getting data
    #https://api.covid19api.com/country/germany?from=2020-03-01T00:00:00Z&to=2020-04-01T00:00:00Z
    url = "https://api.covid19api.com/country/" + country + "?from=" + date_before_seven_days \
          + "&to=" + date_yesterday


    days = []

    # check if the url exists, if not closes app
    try:
        data = requests.get(url)
        data.raise_for_status()
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)


    # create list of lists with all data
    for value in data.json():
        day = [value["Date"],
                value["Confirmed"],
                value["Deaths"],
                value["Recovered"],
                value["Active"]
                ]
        days.append(day)

    return days


# -----------------------------------------
# #Testausgabe mit germany
# days = last_seven_days("germany")
# for day in days:
#     print(day)
