from model.contact_model import Contact


def test_modify_contact_name(app):
    if app.contact.count() == 0:
        app.open_home_page()
        app.contact.open_add_new_contact_page()
        app.contact.create_contact(Contact(firstname="test"))
        app.contact.return_to_home_page()
    app.open_home_page()
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(firstname="New contact name"))
    app.contact.return_to_home_page()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_modify_contact_lastname(app):
    if app.contact.count() == 0:
        app.open_home_page()
        app.contact.open_add_new_contact_page()
        app.contact.create_contact(Contact(firstname="test"))
        app.contact.return_to_home_page()
    app.open_home_page()
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(lastname="New contact lastname"))
    app.contact.return_to_home_page()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_modify_contact_middlename(app):
    if app.contact.count() == 0:
        app.open_home_page()
        app.contact.open_add_new_contact_page()
        app.contact.create_contact(Contact(firstname="test"))
        app.contact.return_to_home_page()
    app.open_home_page()
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(middlename="New contact middlename"))
    app.contact.return_to_home_page()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
