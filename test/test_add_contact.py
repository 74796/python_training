# -*- coding: utf-8 -*-
from model.contact_model import Contact
import pytest
import random
import string


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
           for i in range(2)
    ]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x)for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.open_add_new_contact_page()
    app.contact.create_contact(contact)
    app.open_home_page()
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
