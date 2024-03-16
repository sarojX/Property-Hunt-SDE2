import sys
sys.path.append('/Users/91977/Desktop')

from flipkart.controllers.user_controller import UserController
from flipkart.controllers.property_controller import PropertyController

from flipkart.services.user_service import UserService
from flipkart.services.property_service import PropertService

usercontroller = UserController(UserService())
propertycontroller = PropertyController(PropertService())

user1 = usercontroller.login("Ajay")
user2 = usercontroller.login("Golu")
user2 = usercontroller.login("Rohit")
user2 = usercontroller.login("Piyus")
user2 = usercontroller.login("Raj")


user1.list_property()
user1.logout("Ajay")
user1.list_property() #shouldn't show, not logged in
