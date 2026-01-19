from abc import ABC,abstractmethod

class BankApp(ABC):         # imp we must inherit built in ABC support class

    def connect_db(self):
        print('connected to DB')

    # abstract class , must be implemented by the child classes
    @abstractmethod
    def security_auth(self):        # abstract method is an empty method 
        pass


# child class
class mobileapp(BankApp):
    
    def security_auth(self):
        print("security auth for mobile app successful")

    def mobile_login(self):
        print("logged in from mobile")


# child class
class web_app(BankApp):
    def security_auth(self):
        print("security auth for web app successful")

    def web_login(self):
        print("logged in from mobile")


u1 =mobileapp()
u1.security_auth()
u1.mobile_login()

u2 = web_app()
u2.security_auth()
u2.web_login()