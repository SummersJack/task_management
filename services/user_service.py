from werkzeug.security import generate_password_hash
from repositories.user_repository import UserRepository
from models.user import User

class UserService:
    def __init__(self):
        self.user_repo = UserRepository()

    def create_user(self, username, password):
        # Check if the username already exists
        existing_user = self.user_repo.get_user(username)
        if existing_user:
            raise ValueError("Username already exists.")

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

