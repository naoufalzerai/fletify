from flet import Text
from modules.home.views.template import template
from modules.test.views.bookmark import bookmark
from modules.test.views.favorite import favorite
from libs.controller import Controller


class test(Controller):
    
    def home(self):        
        return template(Text("from test home"), self.page)

    def favorite(self):
        print(self.params)
        return template(favorite(self.page), self.page)

    def bookmark(self):
        print(self.params)
        return template(bookmark(), self.page)