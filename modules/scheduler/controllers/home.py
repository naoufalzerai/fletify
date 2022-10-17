from libs.controller import Controller
from modules.home.views.template import template
from modules.scheduler.models.entities import Scheduler
from modules.scheduler.views.scheduler_list import *

class home(Controller):

    def index(self):
        try:
            schedulers = list(Scheduler)
        except Exception as e:
            print(e)   
        body = scheduler_list()
        return template(body, self.page)
