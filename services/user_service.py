from flipkart.models.user import User
from flipkart.services.user_service_interface import UserServiceInterface

class UserService(UserServiceInterface):
    userDetails = {}
    
    def login(self, name):
        if self.__class__.userDetails.get(name):
            self.__class__.userDetails[name].active = True
        else:
            user = User(name)
            self.__class__.userDetails[name] = user
        print(f"Welcome {name}")

    def logout(self, name):
        self.__class__.userDetails[name].active = False
    
    def list_property(self, name, property_id):
        if self.__class__.userDetails[name].active:
            self.__class__.userDetails[name].listed_properties.append(property_id)
            print("Listing created successfully.")
        else:
            print("You aren't logged in.")

    def view_listed_properties(self, name):
        if self.__class__.userDetails[name].active:
            return self.__class__.userDetails[name].listed_properties
        else:
            print("You aren't logged in.")

    def shortlist(self, name, property_id):
        if self.__class__.userDetails[name].active:
            self.__class__.userDetails[name].shortlisted_properties.append(property_id)
        else:
            print("You aren't logged in.")

    def view_shortlisted_properties(self, name):
        if self.__class__.userDetails[name].active:
            return self.__class__.userDetails[name].shortlisted_properties
        else:
            print("You aren't logged in.")
            