def convertFromSeconds( s ):
    """
        output: takes s and converts it to days, hours, minutes
                and seconds
        input s: any positive int
    """
    days = s / (24*60*60)  # # of days
    s = s % (24*60*60)     # the leftover
    hours = s / (60*60)
    s = s % (60*60)
    minutes = s / 60
    s = s % 60
    seconds = s
    return [days, hours, minutes, seconds]
    
def convertDays(days, currentMonth, currentDay, currentYear):
    """days, currentMonth, currentDay, and currentYear are integers."""
    #Yes, this is unsightly code, but this was a result of my thought 
    #process while attempting this problem. All I can say is that due 
    #to my previous function, I know for sure that the correct time stamp 
    #is 2923 days, 10 hours, 9 minutes, and 21 seconds ahead!"""
    end = 0
    weirdMonths = [4, 6, 9, 11]
    feb = 2
    while (end != days):
        if (currentDay == 31 and currentMonth not in weirdMonths):
            currentDay = 0
            ++currentMonth
            ++end
        elif (currentDay == 30 and currentMonth in weirdMonths ):
            currentDay = 0
            ++currentMonth
            ++end
        elif (currentDay == 28 and currentMonth == feb and currentYear % 4 != 0):
            currentDay = 0
            ++currentMonth
            ++end
        elif (currentDay == 29 and currentMonth == feb and currentYear % 4 == 0):
            currentDay = 0
            ++currentMonth
            ++end
        elif (currentMonth == 12 and currentDay == 31):
            currentDay = 0
            currentMonth = 0
            ++currentYear
            ++end
        else:
            ++currentDay
            ++end
    return [currentMonth, currentDay, currentYear]
