print('User authentication module')

# auth.py

class AuthSystem:
    def __init__(self):
        self.users = {}

    def signup(self, email, password):
        if email in self.users:
            return "User already exists"
        self.users[email] = password
        return "Signup successful"

    def login(self, email, password):
        if email not in self.users:
            return "User not found"
        if self.users[email] != password:
            return "Invalid password"
        return "Login successful"

