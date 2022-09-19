from ormar import String, Integer, Model

from .base_class import MetaClass


class User(Model):
    class Meta(MetaClass):
        tablename = "user"

    id: int = Integer(primary_key=True)
    name: str = String(max_length=30, unique=True)
    password: str = String(max_length=100)
