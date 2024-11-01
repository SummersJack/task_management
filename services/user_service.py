from werkzeug.security import generate_password_hash, check_password_hash
from repositories.user_repository import UserRepository
from models.user import User
import re

class UserService:
    def __init__(self):
        self.user_repo = UserRepository()

    def create_user(self, username, password):
        # Check if the username already exists
        existing_user = self.user_repo.get_user(username)
        if existing_user:
            raise ValueError("Username already exists.")

        # Validate password
        self.validate_password(password)

        # Hash the password
        password_hash = generate_password_hash(password)
        
        # Create a new user with hashed password
        user = User(username=username, password_hash=password_hash)
        self.user_repo.add_user(user)
        return user

    def authenticate_user(self, username, password):
        user = self.user_repo.get_user(username)
        if user and check_password_hash(user.password_hash, password):
            return user
        return None

    def validate_password(self, password):
        # Password must be at least 8 characters long, contain at least one uppercase letter,
        # one lowercase letter, one digit, and one special character.
        if (len(password) < 8 or 
            not re.search(r"[A-Z]", password) or 
            not re.search(r"[a-z]", password) or 
            not re.search(r"[0-9]", password) or 
            not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)):
            raise ValueError("Password must be at least 8 characters long and include an uppercase letter, "
                             "a lowercase letter, a number, and a special character.")
