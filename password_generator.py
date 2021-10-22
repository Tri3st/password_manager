# Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
           'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


class PasswordGenerator:

    def __init__(self, numbers1: int, letters1: int, symbols1: int):
        """
        Generate a password class
        :param numbers1: amount of numbers in the password
        :param letters1: amount of letters in the password (lower and uppercase mixed)
        :param symbols1: amount of special symbols in the password
        """
        self.password_string = None
        self.numbers = numbers1
        self.letters = letters1
        self.symbols = symbols1
        self.password = []
        self.generate_pass()

    def get_pass(self) -> str:
        """
        return a generated password
        :return: the string representation of a generated password
        """
        return self.password_string

    def generate_pass(self):
        for i in range(self.numbers):
            self.password.append(random.choice(numbers))
        for j in range(self.letters):
            self.password.append(random.choice(letters))
        for k in range(self.symbols):
            self.password.append(random.choice(symbols))
        random.shuffle(self.password)
        self.password_string = "".join(self.password)

    def __str__(self) -> str:
        return self.password_string
