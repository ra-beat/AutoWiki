from Entity.WiKi.generation import Generation
from Entity.WiKi.manufacturer import Manufacturer


class Model:
    def __init__(self, manufacturer: Manufacturer, generation: Generation, name: str, key: str, url: str):
        self.manufacturer = manufacturer,
        self.generation = generation,
        self.name = name,
        self.key = key,
        self.url = url

    def get_manufacturer(self) -> Manufacturer:
        return self.manufacturer

    def get_generation(self) -> Generation:
        return self.generation

    def get_name(self) -> str:
        return self.name

    def get_key(self) -> str:
        return self.key

    def get_url(self) -> str:
        return self.url

    def set_manufacturer(self, manufacturer: Manufacturer):
        self.manufacturer = manufacturer

    def set_generation(self, generation: Generation):
        self.generation = generation

    def set_name(self, name: str):
        self.name = name

    def set_key(self, key: str):
        self.key = key

    def set_url(self, url: str):
        self.url = url
