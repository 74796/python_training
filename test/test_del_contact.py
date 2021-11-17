from model.contact_model import Contact


def test_delete_first_contact(app):
    app.open_home_page()
    if app.contact.count() == 0:
        app.open_home_page()
        app.contact.open_add_new_contact_page()
        app.contact.create_contact(Contact(firstname="test"))
        app.contact.return_to_home_page()
    app.contact.delete_first_contact()
