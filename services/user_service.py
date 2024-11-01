from repositories.user_repository import UserRepository

class UserService:
    def __init__(self):
        self.user_repo = UserRepository()

    def create_user(self, user_id, username):
        user = User(user_id, username)
        self.user_repo.add_user(user)
        return user
