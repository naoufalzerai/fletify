from peewee import *

class DBSingleton(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(DBSingleton, cls).__new__(
                                cls, *args, **kwargs)
        return cls._instance

class Base(Model):
    class Meta:
        database = DBSingleton()