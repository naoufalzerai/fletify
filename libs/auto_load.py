import os

class fletify:

    def __init__(self,config) -> None:
        super().__init__()
        self.config = config

    def run(self):
        self.load_modules()
        pass

    def load_modules(self):
        module_folder = os.path.join(self.config["base_path"],"modules")
        modules = [(m,os.path.join(module_folder,m)) for m in os.listdir(module_folder) if os.path.isdir(os.path.join(module_folder,m))]
        pass
