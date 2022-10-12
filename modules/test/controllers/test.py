from flet import Text
from modules.home.views.template import template
from libs.controller import Controller
class test(Controller):
    def home(self):
        
        return template(Text("from home"), self.page)
    def index(self):
        print(self.params)
        return template(Text("from test index"), self.page)
