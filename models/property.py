class Property:
    def __init__(self, title, location, price, type, size, rooms, nearby=None):
        self.title = title
        self.location = location
        self.price = price
        self.type = type
        self.size = size
        self.rooms = rooms
        self.nearby = nearby
        self.available = True

    ##implement setter/getter to set and get values

