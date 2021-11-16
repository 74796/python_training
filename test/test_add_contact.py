# -*- coding: utf-8 -*-
from model.contact_model import Contact


def test_add_contact(app):
    app.open_home_page()
    app.contact.open_add_new_contact_page()
    app.contact.create_contact(Contact(firstname="Adile", middlename="Revanovna", lastname="Shemshedinova",
                                       nickname="Adile", company="Django stars", address="Nauki 62A",
                                       mobile="+380935121990", email="adileshemshedinovaa@gmail.com"))
    app.contact.return_to_home_page()
