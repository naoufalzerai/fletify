from modules.home.views.login   import login
from modules.home.views.template import template

def index(page):
    body = login()
    return template(body, page)
