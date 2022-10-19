from libs.controller import Controller
from modules.home.views.template import template
from modules.scheduler.models.entities import Scheduler
from modules.scheduler.views.scheduler_list import *

class scheduler(Controller):

    def index(self):
        def add(name,cron):
            s = Scheduler(name=name,cron=cron)
            s.save()
            
        def edit(e):
            pass
        body = scheduler_list(list(Scheduler),self.page,add,edit)
        return template(body, self.page)
