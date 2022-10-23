import os
import libs.auto_load as al
import flet
from flet import Theme
from peewee import *

print("start app")

theme = Theme()
theme.page_transitions.android = "cupertino"
theme.page_transitions.ios = "cupertino"
theme.page_transitions.macos = "cupertino"
theme.page_transitions.linux = "cupertino"
theme.page_transitions.windows = "cupertino"

db = SqliteDatabase('../mydb.db', 
                                pragmas={
                                'journal_mode': 'wal',
                                'cache_size': -1024 * 64}
                    )

config = {
    "base_path" : os.getcwd(),
    "view": flet.FLET_APP,
    "home":"/scheduler/scheduler",
    "theme": theme,
    "title": "test",
    "database": db,
    "migration": True
}

al.fletify(config).run()