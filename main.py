import os
import libs.auto_load as al
import flet
from flet import Theme

print("start app")

theme = Theme()
theme.page_transitions.android = "cupertino"
theme.page_transitions.ios = "cupertino"
theme.page_transitions.macos = "cupertino"
theme.page_transitions.linux = "cupertino"
theme.page_transitions.windows = "cupertino"

config = {
    "base_path" : os.getcwd(),
    "view": flet.FLET_APP,
    # "view":flet.WEB_BROWSER,
    "home":"/scheduler/scheduler",
    "theme": theme,
    "title": "test",
    "database": None,
    "migration": True
}

al.fletify(config).run()