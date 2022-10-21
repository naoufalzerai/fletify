from flet import (
    Page, 
    GridView,
    Container, 
    Text, 
    alignment, 
    colors, 
    UserControl
)

class scheduler_list(UserControl):
    def __init__(self,list):
        super().__init__()
        self.list = list
        self.s_list = GridView(
            expand=1,
            runs_count=5,
            max_extent=150,
            child_aspect_ratio=1.0,
            spacing=5,
            run_spacing=5,
        )
        self.update_list()

    def update_list(self,list = None):
        if list is not None:
            self.list = list

        self.s_list.controls.clear()
        for s in self.list:
            self.s_list.controls.append(
                    Container(
                            content=Text(f"{s.name}\n {s.date}\n {s.cron}"),
                            margin=10,
                            padding=10,
                            alignment=alignment.center,
                            bgcolor=colors.CYAN_200,
                            width=150,
                            height=150,
                            border_radius=10,
                            ink=True,
                            on_click=lambda e: print("Clickable with Ink clicked!"),
                    )                                               
                )
        if list is not None:                
            self.update()

    def build(self):      
        return self.s_list