def test_delete_first_contact(app, prepare_contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_contact()
    app.open_home_page()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[0:1] = []
    assert old_contacts == new_contacts
