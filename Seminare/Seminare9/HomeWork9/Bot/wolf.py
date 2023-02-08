class Quote:
    
    my_li = []
    link = ''

    def __init__(self, path: str = r'Seminare\Seminare9\HomeWork9\Bot\quo.txt'):
        self.link = path

    def open(self):
        with open(self.link, 'r', encoding='UTF-8') as file:
            self.my_li = file.readlines()

    def get(self) -> list:
        return self.my_li

qu = Quote()