from flet import Text
from modules.home.views.template import template
from modules.test.models.entities import *
from modules.test.views.bookmark import bookmark
from modules.test.views.favorite import favorite
from libs.controller import Controller
from libs.uow import UOW

class test(Controller):

    
    def home(self):        
        return template(Text("from test home"), self.page)

    def scheduler(self):
        print(self.params)
        return template(favorite(self.page), self.page)

    def vault(self):
        print(self.params)
        return template(bookmark(), self.page)