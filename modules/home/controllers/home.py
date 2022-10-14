from libs.controller import Controller
from modules.home.models.test import Testo
from modules.home.views.hello import hello
from modules.home.views.template import template

class home(Controller):

    def index(self):
        l = (Testo.select())
        body = hello()
        return template(body, self.page)
