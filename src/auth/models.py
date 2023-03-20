from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, Boolean, ForeignKey
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from database import Base
from datetime import datetime

metadata = MetaData()

users = Table(
    "users",
    metadata,
    Column("user_id", Integer, primary_key=True),
    Column("email", String, nullable=False, unique=True),
    Column("name", String, nullable=False),
    Column("surname", String, nullable=False),
    Column("patronymic", String),
    Column("is_hr", Boolean, default=False),
    Column("registered_at", TIMESTAMP, default=datetime.utcnow),
    Column("hashed_password", String(length=1024), nullable=False),
    Column("is_active", Boolean, default=True, nullable=False),
    Column("is_superuser", Boolean, default=False, nullable=False),
    Column("is_verified", Boolean, default=False, nullable=False)
)

class User(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = 'users'
    id = Column("user_id", Integer, primary_key=True)
    email = Column("email", String, nullable=False, unique=True)
    name = Column("name", String, nullable=False)
    surname = Column("surname", String, nullable=False)
    patronymic = Column("patronymic", String)
    registered = Column("registered_at", TIMESTAMP, default=datetime.utcnow)