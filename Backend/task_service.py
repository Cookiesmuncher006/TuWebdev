from fastapi import APIRouter
from task_model import Task

tasks = [
 Task(),
 Task()
]

def get_all_tasks():
 return tasks

def create_task(task: Task):
 task.append(task)
 return "Task Added"

def update_task(task_id: int , updated : Task):
 for task in tasks:
  if task.id == task_id:
   task.description = updated.description
   task.isComplete = updated.isComplete
   return "Updated task"
 return "Task not found"

def delete_task ( task_id : int ):
 for index , task in enumerate (task):
  if task.id == task_id:
   task.pop(index)
   return "Deleted Task"
 return "Task not found"

def get_task(task_id : int):
 for task in tasks:
  if task.id == task_id:
   return task
 return "Not Found"