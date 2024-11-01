from services.user_service import UserService
from services.task_service import TaskService
from utils.logger import setup_logger

logger = setup_logger()

def main():
    user_service = UserService()
    task_service = TaskService()

    logger.info("Creating user...")
    user = user_service.create_user(1, "john_doe")

    logger.info("Creating task...")
    task = task_service.create_task(101, "Complete Python project")

    logger.info(f"User created: {user.username}, Task created: {task.title}")

if __name__ == "__main__":
    main()
