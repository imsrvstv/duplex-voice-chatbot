from peewee import *
from starterkit.fallback_module.conf import db

class BaseModel(Model):
    class Meta:
        
        database = db
