import unittest
from services.user_service import UserService

class TestUserService(unittest.TestCase):
    def setUp(self):
        self.user_service = UserService()

    def test_create_user_success(self):
        user = self.user_service.create_user(1, "john_doe")
        self.assertEqual(user.username, "john_doe")
        self.assertEqual(user.id, 1)

    def test_create_user_with_invalid_id(self):
        with self.assertRaises(ValueError):  
            self.user_service.create_user(-1, "invalid_user")  # Negative ID

    def test_create_user_without_username(self):
        with self.assertRaises(ValueError):  
            self.user_service.create_user(2, "")  # Empty username

    def test_get_user_returns_correct_user(self):
        self.user_service.create_user(3, "alice")
        user = self.user_service.get_user(3)
        self.assertIsNotNone(user)
        self.assertEqual(user.username, "alice")

    def test_get_user_non_existent(self):
        user = self.user_service.get_user(999)  
        self.assertIsNone(user)

    def test_update_user_username(self):
        self.user_service.create_user(4, "bob")
        updated_user = self.user_service.update_user(4, "bob_updated")
        self.assertEqual(updated_user.username, "bob_updated")

    def test_update_user_non_existent(self):
        with self.assertRaises(Exception):  
            self.user_service.update_user(999, "non_existent")

    def test_delete_user_success(self):
        self.user_service.create_user(5, "charlie")
        self.user_service.delete_user(5)
        user = self.user_service.get_user(5)
        self.assertIsNone(user)

    def test_delete_user_non_existent(self):
        with self.assertRaises(Exception):  
            self.user_service.delete_user(999)  

if __name__ == '__main__':
    unittest.main()
