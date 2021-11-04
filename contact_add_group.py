# -*- coding: utf-8 -*-
from summ import Summ
from application import Application
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_contact_add_group(app):
        app.open_home_page()
        app.login(username="admin", password="secret")
        app.open_add_new_contact_page()
        app.create_contact(Summ(name="Adile", middlename="Shemshedinova", lastname="Revanovna", nickname="Adile", company="Django stars", address="Nauki 62A",
                            mobile="+380935121990", email="adileshemshedinovaa@gmail.com", bday="5", bmonth="December", byear="1990"))
        app.return_to_home_page()
        app.logout()
