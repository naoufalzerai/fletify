from flet import Text

from libs.controller import Controller
class test(Controller):
    def home(self):
        return Text("from home")
    def index(self):
        print(self.params)
        return Text("test from index")
