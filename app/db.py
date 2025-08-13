from sqlmodel import create_engine, SQLModel, Session
from pydantic import Field

class Demo1(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"
engine = create_engine(sqlite_url)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session


if __name__ == "__main__":
    create_db_and_tables()