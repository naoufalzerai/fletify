from typing import Callable
from flet import (
    Page, 
    Text, 
    Column,
    FloatingActionButton, 
    icons,
    FloatingActionButton,
    Row,
    ListView,
    UserControl
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

        self.s_list = scheduler_list(self.schedulers())     
        self.dlg_add = scheduler_add(self.save_dlg_add,self.close_dlg_add)   


    def save_dlg_add(self,e):
        s = Scheduler(name=self.dlg_add.nameInput.value,cron=self.dlg_add.cronInput.value)
        self.add(s)
        self.s_list.update_list(self.schedulers())
        self.dlg_add.toggle()
        self.page.update()
        
    def close_dlg_add(self,e):
        self.dlg_add.toggle()
        self.page.update()


    def build(self):

        def open_dlg_add(e):
            self.page.dialog = self.dlg_add
            self.dlg_add.toggle()
            self.page.update()
        
        log_list = ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        
        for i in range(0, 60):
            log_list.controls.append(Text(f"Line {i}"))

        return Column([
            FloatingActionButton(icon=icons.CREATE, text="Add",on_click=open_dlg_add),
            self.s_list,
            Row([log_list])
        ]) 