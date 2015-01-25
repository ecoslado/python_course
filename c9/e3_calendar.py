__author__ = 'Enrique Coslado'

import calendar

def main():
    my_calendar = calendar.Calendar()
    print "CALENDAR:"
    print "Printing days in the week."
    for day in my_calendar.iterweekdays():
        print day

    print "Printing days in the month."
    for day in my_calendar.itermonthdays2(2012, 3):
        print day

    my_text_calendar = calendar.TextCalendar()
    print "TEXT CALENDAR:"
    print "Printing 2008 calendar in three columns"
    print my_text_calendar.formatyear(2008, 3)

    print "Printing third month in 2012"
    print my_text_calendar.formatmonth(2012, 3)

    my_html_calendar = calendar.HTMLCalendar()
    print "HTML CALENDAR:"
    print "Printing third month in 2014"
    print my_html_calendar.formatmonth(2014, 3)

if __name__ == "__main__":
    main()
