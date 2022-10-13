from libs.controller import Controller
from modules.home.views.hello import hello
from modules.home.views.template import template

class home(Controller):

    def index(self):
        body = hello()
        return template(body, self.page)
