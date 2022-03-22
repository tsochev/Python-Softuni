class Profile:
    min_username_letters = 5
    max_username_letters = 15

    min_password_chars = 8
    min_password_digits = 1
    min_password_upper_letters = 1

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __validate_username(self, username):
        if len(username) < self.min_username_letters or len(username) > self.max_username_letters:
            raise ValueError("The username must be between 5 and 15 characters.")

    def __validate_password(self, password):
        if len(password) < self.min_password_chars:
            raise ValueError(f"The password must be {self.min_password_chars} or more characters with "
                             f"at least {self.min_password_digits} digit and {self.min_password_upper_letters} "
                             f"uppercase letter.")

        if len([x for x in password if x.isupper()]) < self.min_password_upper_letters:
            raise ValueError(f"The password must be {self.min_password_chars} or more characters with "
                             f"at least {self.min_password_digits} digit and {self.min_password_upper_letters} "
                             f"uppercase letter.")

        if len([x for x in password if x.isdigit()]) < self.min_password_digits:
            raise ValueError(f"The password must be {self.min_password_chars} or more characters with "
                             f"at least {self.min_password_digits} digit and {self.min_password_upper_letters} "
                             f"uppercase letter.")

    def __str__(self):
        return f'You have a profile with username: "{self.username}" and password: {self.password}'

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        self.__validate_username(value)
        self.__username = value

    @property
    def password(self):
        return "".join("*" * len(self.__password))

    @password.setter
    def password(self, value):
        self.__validate_password(value)
        self.__password = value


correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)

