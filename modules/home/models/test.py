from libs.uow import BaseModel
from peewee import *

class Testo(BaseModel):
    name = CharField()
