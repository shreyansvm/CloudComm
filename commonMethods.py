import datetime
from datetime import date
import calendar

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

def msgBodyString(twoHosts, type):
    # TODO : if twoHosts is empty then raise an exception.

    msgBody = ""
    turn = ", it's your turn to get snacks. "
    replyFormat = "Reply:\n" \
                  "NO - If you are NOT available.  \n" \
                  "OK - If one of you is available and the other can just contribute\n"

    host_1 = twoHosts[0].split(' ')
    host_2 = twoHosts[1].split(' ')
    bothHosts = "Hello "+str(host_1[0])+" and "+str(host_2[0])+":\n"

    my_date = date.today()
    snacksDay = ''  ;# Today or Tomorrow
    if calendar.day_name[my_date.weekday()] == 'Monday' or calendar.day_name[my_date.weekday()] == 'Wednesday':
        snacksDay = 'Tomorrow'
    elif calendar.day_name[my_date.weekday()] == 'Tuesday' or calendar.day_name[my_date.weekday()] == 'Thursday':
        snacksDay = 'REMINDER : Today'

    if type == 'start':
        msgBody = msgBody + bothHosts + snacksDay + turn + replyFormat


    return msgBody

#print greetingString('end')
#print msgBodyString(['Manish Jain Manish.Jain@alcatel-lucent.com 0\n', 'Karunendra Karumanchi Karunendra.Karumanchi@alcatel-lucent.com 0\n'], 'start')