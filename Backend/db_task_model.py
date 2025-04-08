
from pydantic import BaseModel

from sqlmodel import Field, Session, SQLModel, create_engine, select



class Task(SQLModel, table=True):
    
    id: int | None = Field(default=None, primary_key=True)
    description: str = Field(default="")
    isComplete: bool = Field(default=False)


mysql_name = "db_task_service"

mysql_url = f"mysql+pymysql://root:ponce2310@localhost:3306/{mysql_name}"

engine = create_engine(mysql_url)

def create_db_and_tables():
    
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session