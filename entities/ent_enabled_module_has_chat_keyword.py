from peewee import *
from entities.ent_base_model import BaseModel
from entities.ent_chat_keyword import ChatKeyword
from entities.ent_enabled_module import EnabledModule


class EnabledModuleHasChatKeyword(BaseModel):
    enabled_module_id = ForeignKeyField(EnabledModule)
    chat_keyword_id = ForeignKeyField(ChatKeyword) 