from jinja2 import Template


class ContactsService:
    def __init__(self, data_provider):
        self._data_provider = data_provider
        self._index = 0
        self._items_on_page = 2

    def next(self):
        self._index += 1

    def prev(self):
        self._index -= 1

    @property
    def html(self):
        start = self._index * self._items_on_page
        end = start + self._items_on_page
        data = self._data_provider.get_items(start, end)
        tpl = Template(
            "<div>{% for item in data %}<h4>{{ item.name }}</p>{% endfor %}</div>"
            '<a href="/add" id="add-contact-link">add contact</a>'
        )
        return tpl.render({"data": data})

    def add_contact(self, name, phone):
        self._data_provider.add_item(name=name, phone=phone)
