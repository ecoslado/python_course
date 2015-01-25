__author__ = 'Enrique Coslado'

import time

def main():
    print "time.clock(): %s" % time.clock()
    print "time.ctime(): %s" % time.ctime()
    print "time.daylight: %s" % time.daylight
    print "time.sleep(1): %s" % time.sleep(2)
    print "time.localtime(): %s" % time.localtime()
    print "time.mktime(time.localtime()): %s" % time.mktime(time.localtime())
    print "time.strftime('%%Y-%%m-%%d -> %%H:%%m:%%s'): %s" % time.strftime("%Y-%m-%d -> %H:%m:%s")


if __name__ == "__main__":
    main()