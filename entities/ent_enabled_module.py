from peewee import *
from entities.ent_base_model import BaseModel


class EnabledModule(BaseModel):
    class_name = CharField(unique=True)
    custom_json_settings = TextField()