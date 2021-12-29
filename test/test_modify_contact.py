from model.contact_model import Contact
from random import randrange


def test_modify_some_contact_name(app, prepare_contact):
    app.open_home_page()
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="Modified name")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    app.open_home_page()
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


# def test_modify_contact_lastname(app, prepare_contact)
#     old_contacts = app.contact.get_contact_list()
#     app.contact.modify_first_contact(Contact(lastname="New contact lastname"))
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) == len(new_contacts)
#
#
# def test_modify_contact_middlename(app, prepare_contact):
#     old_contacts = app.contact.get_contact_list()
#     app.contact.modify_first_contact(Contact(middlename="New contact middlename"))
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) == len(new_contacts)
