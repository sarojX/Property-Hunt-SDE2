class UserController:
    def __init__(self, userService):
        self.userService = userService
        
    def login(self, name):
        self.userService.login(name)

    def logout(self, name):
        self.userService.logout(name)

    def list_property(self, name):
        prop = self.userService.list_property(name)

   