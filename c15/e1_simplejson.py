__author__ = 'Enrique Coslado'

import simplejson as json

JSON_STRING = '{"key1": "value", "key2": ["value2", "value3", "value4"], "key3": "value4"}'

def main():
    json_dict = json.loads(JSON_STRING)
    print "Loads returns %s. This variable is %s" % (json_dict, type(json_dict))

    json_dict["key3"] = {
        "foo": {
            "stuff": 5
        },
        "bar": {
            "stuff": 3
        }
    }

    print "After inserting some information in dictionary: %s" % json_dict

    json_string = json.dumps(json_dict)
    print "Dumps returns %s. This variable is %s" % (json_string, type(json_string))

if __name__ == "__main__":
    main()


