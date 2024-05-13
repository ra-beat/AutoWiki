class Generation:
    def __init__(self, name: str, date: str, img_url: str, description: str):
        self.name = name
        self.date = date
        self.img_url = img_url
        self.description = description

    def get_name(self) -> str:
        return self.name

    def get_date(self) -> str:
        return self.date

    def get_img_url(self) -> str:
        return self.img_url

    def get_description(self) -> str:
        return self.description

    def set_name(self, name: str):
        self.name = name

    def set_date(self, date: str):
        self.date = date

    def set_img_url(self, img_url: str):
        self.img_url = img_url

    def set_description(self, description: str):
        self.description = description
