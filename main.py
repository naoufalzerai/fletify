import os
import libs.auto_load as al
import flet
from flet import Theme

theme = Theme()
theme.page_transitions.android = "openUpwards"
theme.page_transitions.ios = "cupertino"
theme.page_transitions.macos = "fadeUpwards"
theme.page_transitions.linux = "fadeUpwards"
theme.page_transitions.windows = "fadeUpwards"

config = {
    "base_path" : os.getcwd(),
    "view": flet.FLET_APP,
    # "view":flet.WEB_BROWSER,
    "home":"/home/home",
    "theme": theme,
    "title": "test"
}

al.fletify(config).run()