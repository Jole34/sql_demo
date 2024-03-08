from . import Base
from sqlalchemy import Column, Integer, String, DateTime, func, Float, Boolean
from sqlalchemy.ext.hybrid import hybrid_property


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, unique=True, index=True, nullable=False, autoincrement=True)
    email = Column(String, unique=True, nullable=False, index=True)
    budget = Column(Float, nullable=False, default=0)
    name = Column(String, nullable=False)
    created_on = Column(DateTime, nullable=False, server_default=func.now())
    active = Column(Boolean, nullable=True)

    @hybrid_property
    def is_rich(self):
        return self.budget > 2_000_000

