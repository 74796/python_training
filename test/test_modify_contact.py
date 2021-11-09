from model.contact_model import Summ


def test_modify_first_contact(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.contact.open_add_new_contact_page()
    app.contact.modify_first_contact(Summ(name="Adile_modified", middlename="Shemshedinova", lastname="Revanovna",
                                          nickname="Adile", company="Django stars", address="Nauki 62A",
                                          mobile="+380935121990", email="adileshemshedinovaa@gmail.com", bday="5",
                                          bmonth="December", byear="1990"))
    app.contact.return_to_home_page()
    app.session.logout()
