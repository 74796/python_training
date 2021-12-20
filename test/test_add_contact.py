# -*- coding: utf-8 -*-
from model.contact_model import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.open_add_new_contact_page()
    contact = Contact(firstname="Adile", middlename="Revanovna", lastname="Shemshedinova", nickname="Adile",
                      company="Django stars", address="Nauki 62A", mobile="+380935121990",
                      email="adileshemshedinovaa@gmail.com")
    app.contact.create_contact(contact)
    app.open_home_page()
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


# def test_add_empty_contact(app):
#     old_contacts = app.contact.get_contact_list()
#     app.contact.open_add_new_contact_page()
#     contact = Contact(firstname="", middlename="", lastname="", nickname="", company="", address="", mobile="",
#                       email="")
#     app.contact.create_contact(contact)
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) + 1 == len(new_contacts)
#     old_contacts.append(contact)
#     assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
