# demo.py

from auth import AuthSystem

auth = AuthSystem()
print(auth.signup("user@example.com", "securepassword"))
print(auth.login("user@example.com", "securepassword"))
