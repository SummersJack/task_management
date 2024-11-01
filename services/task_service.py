from repositories.task_repository import TaskRepository
from models.task import Task

class TaskService:
    def __init__(self):
        self.task_repo = TaskRepository()

    def create_task(self, task_id, title):
        if self.task_repo.get_task_by_id(task_id):
            raise ValueError(f"Task with ID {task_id} already exists.")

        task = Task(task_id, title)
        self.task_repo.add_task(task)
        return task

    def get_task(self, task_id):
        task = self.task_repo.get_task_by_id(task_id)
        if not task:
            raise ValueError(f"Task with ID {task_id} not found.")
        return task

    def update_task(self, task_id, title):
        task = self.task_repo.get_task_by_id(task_id)
        if not task:
            raise ValueError(f"Task with ID {task_id} not found.")
        
        task.title = title
        self.task_repo.update_task(task)
        return task

    def delete_task(self, task_id):
        if not self.task_repo.get_task_by_id(task_id):
            raise ValueError(f"Task with ID {task_id} not found.")
        
        self.task_repo.delete_task(task_id)

    def list_tasks(self):
        return self.task_repo.get_all_tasks()
