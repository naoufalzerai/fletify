import os
import libs.auto_load as al
import flet

config = {
    "base_path" : os.getcwd(),
    "view": flet.FLET_APP,
    # "view":flet.WEB_BROWSER,
    "home":"/home/home"
}

al.fletify(config).run()