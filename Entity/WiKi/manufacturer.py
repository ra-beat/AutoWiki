class Manufacturer:
    def __init__(self, name: str, url: str):
        self.name = name
        self.url = url

    def get_name(self) -> str:
        return self.name

    def get_url(self) -> str:
        return self.url

    def set_name(self, name: str):
        self.name = name

    def set_url(self, url: str):
        self.url = url