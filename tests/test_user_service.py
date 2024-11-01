import unittest
from services.user_service import UserService

class TestUserService(unittest.TestCase):
    def setUp(self):
        self.user_service = UserService()

    def test_create_user(self):
        user = self.user_service.create_user(1, "john_doe")
        self.assertEqual(user.username, "john_doe")

if __name__ == '__main__':
    unittest.main()
