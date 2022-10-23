from flet import (
    GridView,
    Container, 
    colors, 
    UserControl,
    TextButton,
    ButtonStyle
)
from flet.buttons import (
    CountinuosRectangleBorder
)

class scheduler_list(UserControl):
    def __init__(self,list,on_select):
        super().__init__()
        self.list = list
        self.on_select = on_select

        self.s_list = GridView(
            expand=1,
            runs_count=5,
            max_extent=150,
            child_aspect_ratio=1.0,
            spacing=5,
            run_spacing=5                   
        )
        self.update_list()

    def update_list(self,list = None):
        if list is not None:
            self.list = list

        self.s_list.controls.clear()
        for s in self.list:
            self.s_list.controls.append(
                    Container(
                        content=TextButton(
                                f"{s.name}\n {s.date}\n {s.cron}",
                                style=ButtonStyle(
                                    shape=CountinuosRectangleBorder(radius=30),    
                                    padding=0,
                                    color= colors.WHITE,    
                                    bgcolor=colors.CYAN_200                                                    
                                ),
                            ),
                        margin=5
                    )                                 
                )
        if list is not None:                
            self.update()

    def build(self):      
        return self.s_list