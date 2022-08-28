from pages.apply_page import ApplyPage


class ErrorTest(ApplyPage):

    def test(self):
        self.load()
        self.enter_name()
        self.enter_email()
        self.random_phone()
        self.submit()
