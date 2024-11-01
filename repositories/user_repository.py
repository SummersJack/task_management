from models.user import User

class UserRepository:
    def __init__(self):
        self.users = {}

    def add_user(self, user):
        self.users[user.user_id] = user

    def get_user(self, user_id):
        return self.users.get(user_id)
