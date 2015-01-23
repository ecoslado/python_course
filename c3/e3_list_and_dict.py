__author__ = 'kike'

from c3.e4_mutable_immutable import variable_info

def from_second(any_list):
    return any_list[1:]

def till_penultimate(any_list):
    return any_list[:-1]

def string_keys(any_dict):
    out = list()
    for key in any_dict:
        if type(key) == str:
            out.append(key)
    return out

def value_with_string_keys(any_dict):
    out = list()
    for key, value in any_dict.items():
        if type(key) == str:
            out.append(value)
    return out

## alternate string_key
def alter_string_keys(any_dict):
    return [key for key in any_dict if type(key) == str]


def main():
    fruits = ["orange", "pear", "apple"]
    mixed_dict = {"fruits": fruits, 2: "stuff", "foo": "bar"}

    print "Fruits: %s" % fruits
    print "Mixed dict: %s" % mixed_dict
    print "Access to a list element: %s" % fruits[0]
    print "Access to a dict element: %s" % mixed_dict["fruits"]
    print "Two level access in mixed dict: %s" % mixed_dict["fruits"][0]
    print "Fruits from second element: %s" % from_second(fruits)
    print "Fruits till penultimate element: %s" % till_penultimate(fruits)
    print "String keys in mixed dict: %s" % string_keys(mixed_dict)
    print "String keys in mixed dict with alternate method: %s" % alter_string_keys(mixed_dict)
    print "Values with string keys in mixed dict: %s" % value_with_string_keys(mixed_dict)

    print "By the way variable info for fruits: %s" % variable_info(fruits)
    print "While variable info for mixed_dict['fruits']: %s" % variable_info(mixed_dict["fruits"])

if __name__ == "__main__":
    main()