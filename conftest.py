import pytest
from fixture.application import Application
from model.contact_model import Contact

fixture = None


@pytest.fixture
def app(request):
    global fixture
    if fixture is None:
        fixture = Application()
    else:
        if not fixture.is_valid():
            fixture = Application()
    fixture.session.ensure_login(username="admin", password="secret")
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture


@pytest.fixture
def prepare_contact(app):
    if app.contact.count() == 0:
        app.open_home_page()
        app.contact.open_add_new_contact_page()
        app.contact.create_contact(Contact(firstname="Added contact"))
        app.contact.return_to_home_page()
