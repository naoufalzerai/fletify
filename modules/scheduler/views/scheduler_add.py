from distutils.command.build import build
from flet import (
    Text, 
    Column,
    AlertDialog,
    TextButton,
    TextField,
    UserControl,
    Row
)

class scheduler_add(UserControl):
    def __init__(self,save_dlg_add):
        super().__init__()
        self.nameInput = TextField(label="Name")
        self.cronInput = TextField(label="Cron")
        self.descriptionInput =TextField(
            label="Description",
            multiline=True,
            min_lines=3,
        )

        self.save_dlg_add = save_dlg_add


    def build(self):
        return Column(
                [   
                    self.nameInput,
                    self.cronInput,
                    self.descriptionInput,
                    Row(
                        [
                            TextButton("Save", on_click=self.save_dlg_add)
                        ]
                    )
                ],
                expand=True)