from distutils.command.build import build
from flet import Text,UserControl
class hello(UserControl):
    def build(self):        
        return Text("hello")