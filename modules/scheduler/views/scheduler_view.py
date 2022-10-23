from enum import auto
from tkinter import E
from typing import Callable
from flet import (
    Page, 
    Text, 
    Column,
    FloatingActionButton, 
    icons,
    FloatingActionButton,
    Row,
    Container,
    ListView,
    UserControl,
    colors
)

from modules.scheduler.models.entities import Scheduler
from modules.scheduler.views.scheduler_add import scheduler_add
from modules.scheduler.views.scheduler_list import scheduler_list


class scheduler_view(UserControl):

    def __init__(self, page: Page,schedulers: Callable,add: Callable,edit: Callable):
        super().__init__()

        self.page = page
        self.schedulers = schedulers
        self.add = add
        self.edit = edit

        self.s_list = scheduler_list(self.schedulers(),self.on_select)     
        self.s_add = scheduler_add(self.save_s_add)   


    def save_s_add(self,e):
        s = Scheduler(name=self.s_add.nameInput.value,cron=self.s_add.cronInput.value)
        self.add(s)
        self.s_list.update_list(self.schedulers())
        self.page.update()
        
    
    def on_select(self,e):
        print(e.content)

    def build(self):
        
        log_list = ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        
        for i in range(0, 60):
            log_list.controls.append(Text(f"Line {i}"))
            
        return Column(
                    controls=[
                        Container(expand=2, content= self.s_add),
                        Container(expand=3, content= self.s_list),
                        Container(expand=1, content= log_list),
                    ],
                    alignment="start"
                ) 