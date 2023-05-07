from nicegui import ui
from nicegui.events import KeyEventArguments
from pydantic import BaseModel

from app.data_providers.dummy_data_provider import DataProvider
from app.services.contacts_service import ContactsService


@ui.page("/add")
def add_contact():
    def add_contact_clicked(*_, **__):
        contacts_service.add_contact(name=item.name, phone=item.phone)
        ui.open("/")

    class Item(BaseModel):
        name: str | None = None
        phone: str | None = None

    data_provider = DataProvider()
    contacts_service = ContactsService(data_provider)
    item = Item()
    with ui.header(elevated=True).style('background-color: #3874c8').classes('items-center justify-between'):
        ui.label("New contact")
    ui.input().bind_value(item, "name")
    ui.input().bind_value(item, "phone")
    ui.button(on_click=add_contact_clicked)


@ui.page("/")
def contact_list():
    def handle_key(event: KeyEventArguments) -> None:
        if event.action.keydown:
            if event.key.arrow_right:
                contacts_service.next()
            if event.key.arrow_left:
                contacts_service.prev()

    data_provider = DataProvider()
    contacts_service = ContactsService(data_provider)
    ui.html().bind_content(contacts_service, "html")
    ui.keyboard(on_key=handle_key)  # handle keyboard events


ui.run(port=9999)
