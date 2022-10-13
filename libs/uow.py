from peewee import *
from libs.singleton import Singleton

class UOW(metaclass=Singleton):
    db = SqliteDatabase('app.db', pragmas={
        'journal_mode': 'wal',
        'cache_size': -1024 * 64})

    def __init__(self):
        print("load db")


class BaseModel(Model):
    class Meta:
        database = UOW.db