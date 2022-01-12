from model.contact_model import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", middlename="", lastname="", nickname="", company="", address="", homephone="",
                    mobilephone="", workphone="", secondaryphone="", email="", email2="", email3="")]+[
           Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10),
                   lastname=random_string("lastname", 10), nickname=random_string("nickname", 10),
                   company=random_string("company", 10), address=random_string("address", 10),
                   homephone="+380935121990", mobilephone="+380935121991", workphone="+380935121992",
                   secondaryphone="+380935121993",
                   email="adileshemshedinovaa@gmail.com", email2="test@gmail.com", email3="test1@gmail.com")
           for i in range(n)
    ]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
