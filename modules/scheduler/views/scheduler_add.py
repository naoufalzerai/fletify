from distutils.command.build import build
from flet import (
    Text, 
    Column,
    AlertDialog,
    TextButton,
    TextField,
    UserControl
)

class scheduler_add(UserControl):
    def __init__(self,save_dlg_add,close_dlg_add):
        super().__init__()
        self.nameInput = TextField(label="Name")
        self.cronInput = TextField(label="Cron")
        self.descriptionInput =TextField(
            label="Description",
            multiline=True,
            min_lines=3,
        )

        self.save_dlg_add = save_dlg_add
        self.close_dlg_add = close_dlg_add
        self.dlg = AlertDialog(
            modal=True,
            title=Text("New cron "),
            content=Column([
                    self.nameInput,
                    self.cronInput,
                    self.descriptionInput,
                ],
                expand=False),
            actions=[
                TextButton("Save", on_click=self.save_dlg_add),                
                TextButton("Cancel", on_click=self.close_dlg_add),
            ],
            actions_alignment="end",
            on_dismiss=lambda e: print("Modal dialog dismissed!"),
        )

    def toggle(self):
        self.dlg.open = not self.dlg.open
        if self.dlg.page is not None:
            self.dlg.update()


    def build(self):
        return self.dlg