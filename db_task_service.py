from db_task_model import Task

from sqlmodel import select, Session


def get_all_tasks(session: Session):
    """
    Retrieve all tasks from the database.
    
    Args:
        session (Session): The database session object
        
    Returns:
        list: A list of all Task objects in the database
    """
    statement = select(Task)
    tasks = session.exec(statement).all()
    return tasks


def create_task(task: Task, session: Session):
    """
    Create a new task in the database.
    
    Args:
        task (Task): The Task object to be created
        session (Session): The database session object
        
    Returns:
        Task: The created Task object with updated fields (including ID)
    """
    session.add(task)
    session.commit()
    
    session.refresh(task)
    return task


def update_task(task_id: int, updated: Task, session: Session):
    """
    Update an existing task in the database.
    
    Args:
        task_id (int): The ID of the task to update
        updated (Task): Task object containing updated values
        session (Session): The database session object
        
    Returns:
        Task or str: The updated Task object if found, or error message if not found
    """
    task = session.get(Task, task_id)

    if not task:
        return "Task Not Found"
    
    task.description = updated.description
    task.isComplete = updated.isComplete
    session.commit()
    session.refresh(task)
    
    return task


def delete_task(task_id: int, session: Session):
    """
    Delete a task from the database.
    
    Args:
        task_id (int): The ID of the task to delete
        session (Session): The database session object
        
    Returns:
        str: Success message or error message
    """
    task = session.get(Task, task_id)
    
    if not task:
        return "Task not found"
    
    session.delete(task)
    session.commit()

    return "Task deleted successfully"


def get_task(task_id: int, session: Session):
    """
    Retrieve a specific task by ID from the database.
    
    Args:
        task_id (int): The ID of the task to retrieve
        session (Session): The database session object
        
    Returns:
        Task or str: The requested Task object if found, or error message if not found
    """
    task = session.get(Task, task_id)
    
    if not task:
        return "Task Not Found"
    
    return task