from repositories.task_repository import TaskRepository
from models.task import Task

class TaskService:
    def __init__(self):
        self.task_repo = TaskRepository()

    def create_task(self, task_id, title):
        task = Task(task_id, title)
        self.task_repo.add_task(task)
        return task
