from model.contact_model import Contact


def test_modify_contact_name(app, prepare_contact):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="New contact name")
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
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
