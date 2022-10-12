import os
import flet
import importlib
from flet import Page,View,TemplateRoute

class fletify:

    def __init__(self,config) -> None:
        super().__init__()
        self.config = config
        self.modules = []
        self.routes = []
        self.page = {}


    def load_main_page(self,page: Page):
        self.page = page
        # self.page.add(Text(f"Initial route: {self.page.route}"))
        
        self.route_change(TemplateRoute("/"))
        self.page.on_route_change = self.route_change
        self.page.update()

    def route_change(self, route=[]):
        self.page.views.clear()
        
        route_arr = route.route.split("/") if route.route!="/" else self.config["home"].split("/")
        module, controller, function, params = route_arr[1] if len(route_arr)>1 else None, route_arr[2]  if len(route_arr)>2 else None, route_arr[3]  if len(route_arr)>3 else None, route_arr[4:]  if len(route_arr)>4 else None
     
        if module is not None and controller is not None and module != '' and controller != '':
            controller_path = os.path.join(self.config["base_path"], "modules",module,"controllers",controller+".py")
            if os.path.exists(controller_path):
                spec  = importlib.util.spec_from_file_location("controller",controller_path)
                c = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(c)   
                if hasattr(c,controller):
                    controller_instance = getattr(c,controller)(self.page,params)
                else:
                    raise Exception("404")

                if(function is None or function == ""):
                    if(hasattr(controller_instance, "index")):                        
                        # self.page.add(controller_instance.index())
                        self.page.views.append(View(
                            "/".join(route_arr),
                            [controller_instance.index()]
                        )
                        )
                        self.page.update()
                    else:
                        raise Exception("404")
                else:
                    if(hasattr(controller_instance, function)):
                        # self.page.add(getattr(controller_instance, function)())
                        self.page.views.append(View(
                            "/".join(route_arr),
                            [getattr(controller_instance, function)()]
                            )
                        )
                        self.page.update()
                    else:
                        raise Exception("404")
            else:
                raise Exception("404")
        else:
            raise Exception("404")
     

    def run(self):
        # self.load_modules()
        flet.app(target=self.load_main_page, view=self.config["view"])        

    def load_modules(self):       
        module_folder = os.path.join(self.config["base_path"],"modules")
        self.modules += [{"name":m,"path":os.path.join(module_folder,m)} for m in os.listdir(module_folder) if os.path.isdir(os.path.join(module_folder,m))]

        pass
