class PropertyController:
    def __init__(self, propertyService):
        self.propertyService= propertyService

    def add_property(self, property_id, property_title, loc, price, type, size, rooms, nearby, available):
        self.propertyService.add_property(property_id, property_title, loc, price, type, size, rooms, nearby, available)

    def mark_sold(self, property_id):
        self.propertyService.mark_sold(property_id)

    def search_properties(self, filters=None, sort_by='size'):
        filtered_properties = self.propertyService.get_all_property()
        if filters:
            for key, value in filters.items():
                if key == 'location':
                    filtered_properties = [prop for prop in filtered_properties if prop.location.lower() == value.lower()]
                elif key == 'pricerange':
                    price_range = value.split('-')
                    if len(price_range) == 2:
                        filtered_properties = [prop for prop in filtered_properties if
                                               int(price_range[0]) <= prop.price <= int(price_range[1])]
                    else:
                        filtered_properties = [prop for prop in filtered_properties if prop.price >= int(price_range[0])]
                elif key == 'type':
                    filtered_properties = [prop for prop in filtered_properties if prop.property_type.lower() == value.lower()]
                elif key == 'sizerange':
                    size_range = value.split('-')
                    if len(size_range) == 2:
                        filtered_properties = [prop for prop in filtered_properties if
                                               int(size_range[0]) <= int(prop.size[:-4]) <= int(size_range[1])]
                    else:
                        filtered_properties = [prop for prop in filtered_properties if
                                               int(prop.size[:-4]) >= int(size_range[0])]
                elif key == 'rooms':
                    filtered_properties = [prop for prop in filtered_properties if prop.rooms.lower() == value.lower()]
        sorted_properties = sorted(filtered_properties, key=lambda x: getattr(x, sort_by))
        for prop in sorted_properties:
            print(prop.title)

        

