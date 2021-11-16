# -*- coding: utf-8 -*-
from model.group_model import Group


def test_add_group(app):
    app.group.create(Group(name="adile", header="adile", footer="adile"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))
