import sys
from peewee import *


from modules.get_welcome_msg.get_welcome_msg import get_welcome_msg
from modules.get_random_question.get_random_question import get_random_question
from modules.get_random_fact.get_random_fact import get_random_fact
from entities.ent_enabled_module import EnabledModule

def db_loadEnabledModules():
    enabled_modules = []
    for module in EnabledModule.select():
        enabled_modules.append(
            
            getattr(sys.modules[__name__], module.class_name)()
        )
    return enabled_modules



