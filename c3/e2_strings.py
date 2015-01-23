__author__ = 'kike'

def words(text):
    return text.split(' ')

def changed_second_by_third(three_strings):
    return "{0}{2}{1}".format(*three_strings)

def titled_title(any_title, artist):
    return " %s by %s " % (any_title, artist)

def main():
    print words("Joseph of Arimathea. He who is valiant and pure of spirit may find the Holy Grail in the Castle of aaarrrrggh ...")
    print changed_second_by_third("Helloworld")
    print titled_title("The life of Brian", "Monty Python")

if __name__ == "__main__":
    main()