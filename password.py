# password class
class Password:

    def __init__(self):
        self.website = None
        self.email = None
        self.password = None

    def set_website(self, website):
        self.website = website

    def set_password(self, password):
        self.password = password

    def set_email(self, email):
        self.email = email

    def set_all(self, website, email, password):
        self.website = website
        self.email = email
        self.password = password

    def get_website(self):
        return self.website

    def get_email(self):
        return self.email

    def get_password(self):
        return self.password

    def get_all(self) -> tuple:
        return self.website, self.email, self.password

    def __str__(self):
        return f"{self.website} {self.email} '{self.password}'"
