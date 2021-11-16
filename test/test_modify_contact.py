from model.contact_model import Contact


def test_modify_contact_name(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(firstname="New contact name"))
    app.contact.return_to_home_page()
    app.session.logout()


def test_modify_contact_lastname(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(lastname="New contact lastname"))
    app.contact.return_to_home_page()
    app.session.logout()


def test_modify_contact_middlename(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(middlename="New contact middlename"))
    app.contact.return_to_home_page()
    app.session.logout()
