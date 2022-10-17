from libs.controller import Controller
from modules.home.views.template import template
from modules.scheduler.models.entities import Scheduler
from modules.scheduler.views.scheduler_list import *

class home(Controller):

    def index(self):

        body = scheduler_list(list(Scheduler))
        return template(body, self.page)
