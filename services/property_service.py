from flipkart.services.property_service_interface import PropertyServiceInterface
from flipkart.models.property import Property

class PropertyService(PropertyServiceInterface):
    propertyDetails = {}

    def add_property(self, property_id, property_title, loc, price, type, size, rooms, nearby, available):
        property = Property(property_id, property_title, loc, price, type, size, rooms, nearby, available)
        self.propertyDetails[property_id] = property

    def mark_sold(self, property_id):
        property = self.__class__.propertyDetails.get(property_id)
        if property:
            property.available = False

    def get_property_by_id(self, property_id):
        return self.__class__.propertyDetails.get(property_id)
    
    def get_all_property(self):
        return [prop for prop in self.propertyService.propertyDetails]




        