CARD_DATA = [
    {"name": "foo", "phone": "123"},
    {"name": "bar", "phone": "345"},
    {"name": "baz", "phone": "678"},
]


class DataProvider:
    _data = CARD_DATA

    def get_items(self, offset, limit):
        return self._data[offset : offset + limit]

    def add_item(self, **kwargs):
        self._data.append(kwargs)
