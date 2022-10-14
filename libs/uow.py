from peewee import *
from libs.singleton import Singleton

class UOW(metaclass=Singleton):
    db = Proxy()

    def set_db(self,db):
        self.db.initialize(db)
        pass

    def __init__(self):
        print("load db")


class BaseModel(Model):
    class Meta:
        database = UOW().db