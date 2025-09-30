class BasePage:

    def click(self):
        print("clicking...")

    def find_element(self, locator):
        print("Searching.... ")

    def verify_text(self):
        print("Verify text... ")

class LoginPage(BasePage):
    LOGIN_BTN =''
    def find_login_btn(self):
        self.find_element(self.LOGIN_BTN)

class HomePage(BasePage):

    def verify_oage_opened(self):
        self.verify_text('home header')


login_Page = LoginPage()
login_Page.find_login_btn()

