from typing import Callable
from flet import (
    Page, 
    GridView,
    Container, 
    Text, 
    alignment, 
    colors, 
    Column,
    FloatingActionButton, 
    icons,
    FloatingActionButton,
    AlertDialog,
    TextButton,
    TextField,
    Row
)


def scheduler_list(schedulers,page: Page,add: Callable,edit: Callable):
    s_list = GridView(
        expand=1,
        runs_count=5,
        max_extent=150,
        child_aspect_ratio=1.0,
        spacing=5,
        run_spacing=5,
    )
    for s in schedulers:
        s_list.controls.append(
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

    def save_dlg_add(_e):
        add("name","cron")        
        dlg_add.open = False
        page.update()


        
    def close_dlg_add(e):
        dlg_add.open = False
        page.update()

    def open_dlg_add(e):
        page.dialog = dlg_add
        dlg_add.open = True
        page.update()

    dlg_add = AlertDialog(
        modal=True,
        title=Text("New cron"),
        content=Column([
                Row([Text("Name :"),TextField()]),
                Row([Text("Cron :"),TextField(width=300)])
            ]),
        actions=[
            TextButton("Save", on_click=save_dlg_add),
            TextButton("Cancel", on_click=close_dlg_add),
        ],
        actions_alignment="end",
        on_dismiss=lambda e: print("Modal dialog dismissed!"),
    )

    return Column([
        FloatingActionButton(icon=icons.CREATE, text="Add",on_click=open_dlg_add),
        s_list
    ]) 