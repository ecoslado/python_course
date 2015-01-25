__author__ = 'Enrique Coslado'

from datetime import date, time, datetime, timedelta

def main():
    print "time.now(hour=2): %s" % time(hour=2)
    print "date.today(): %s" % date.today()
    print "datetime.now(): %s" % datetime.now()
    print "datetime(year=2014, month=12, day=22, hour=10, minute=0): %s" % datetime(year=2014, month=12, day=22, hour=10, minute=0)
    print "datetime.now() - timedelta(days=2): %s" % (datetime.now() - timedelta(days=2))

if __name__ == "__main__":
    main()