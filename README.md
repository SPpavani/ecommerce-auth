# ecommerce-auth

## 📌 Overview
`ecommerce-auth` is a portfolio project demonstrating secure authentication workflows for e‑commerce applications.  
It includes Python modules for user login, registration, and session handling, with GitHub best practices.

---

## ✨ Features
- User signup and login  
- Password hashing for security  
- Session/token management basics  
- Modular Python code structure  

---

## 🛠 Tech Stack
- **Python** (authentication logic)  
- **Git & GitHub** (version control)  
- **Optional DB integration** (SQLite/MySQL/PostgreSQL)  

---

## 🚀 How to Run
1. Clone the repo:
   ```bash
   git clone https://github.com/SPpavani/ecommerce-auth.git
   cd ecommerce-auth
## 🚀 Usage Example

```python
from auth import AuthSystem

auth = AuthSystem()
print(auth.signup("user@example.com", "securepassword"))
print(auth.login("user@example.com", "securepassword"))
Signup successful
Login successful
