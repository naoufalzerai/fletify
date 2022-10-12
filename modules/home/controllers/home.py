from libs.controller import Controller
from modules.home.views.login   import login
from modules.home.views.template import template

class home(Controller):

    def index(self):
        body = login()
        return template(body, self.page)
