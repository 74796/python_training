# -*- coding: utf-8 -*-
from model.contact_model import Summ


def test_contact_add_group(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.contact.open_add_new_contact_page()
    app.contact.create_contact(Summ(name="Adile", middlename="Shemshedinova", lastname="Revanovna", nickname="Adile",
                                    company="Django stars", address="Nauki 62A", mobile="+380935121990",
                                    email="adileshemshedinovaa@gmail.com", bday="5", bmonth="December", byear="1990"))
    app.contact.return_to_home_page()
    app.session.logout()
