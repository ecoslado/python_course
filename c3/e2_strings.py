__author__ = 'Enrique Coslado'

def words(text):
    for char in ",.;:":
        text = text.replace(char, '')

    first_split = text.split(' ')
    out = list()
    for elem in first_split:
        if elem != '':
            out.append(elem)

    return out

def changed_second_by_third(three_strings):
    return "{0}{2}{1}".format(*three_strings)

def formatted_title(any_title, artist):
    return " %s by %s " % (any_title, artist)

def main():
    monty_python_text = "Joseph of Arimathea. He who is valiant and pure of spirit may find the Holy Grail in the Castle of aaarrrrggh ..."
    print monty_python_text
    print words(monty_python_text)
    print changed_second_by_third("Helloworld")
    print formatted_title("The life of Brian", "Monty Python")

if __name__ == "__main__":
    main()