from models.task import Task

class TaskRepository:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task):
        self.tasks[task.task_id] = task

    def get_task(self, task_id):
        return self.tasks.get(task_id)
