# Add all common methods

import datetime

'''
Returns Greetings string to start or end with.
'''
def greetingString(type):
    greetings = ""
    isNight = 0

    # Returns in 24 hour clock format
    currentTime = datetime.datetime.now()


    if currentTime.hour < 12:
        greetings = "Good Morning"
    elif 12 <= currentTime.hour < 18:
        greetings = "Good Afternoon"
    elif 18 <= currentTime.hour < 20:
        greetings = "Good Evening"
    else:
        isNight = 1
        greetings = "Good Night"

    if type == 'start':
        if isNight:
            greetings = "Hi there! "
        else:
            greetings = "Hi there, " + greetings + ". "
    elif type == 'end':
        greetings = "Thank you, " + greetings + ". "

    return greetings
