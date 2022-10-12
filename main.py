import os
import libs.auto_load as al

config = {
    "base_path" : os.getcwd()
}

al.fletify(config).run()