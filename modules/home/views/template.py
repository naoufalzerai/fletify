from flet import (
    Column,
    FloatingActionButton,
    Icon,
    NavigationRail,
    NavigationRailDestination,
    Row,
    Text,
    VerticalDivider,
    AlertDialog,
    TextButton,
    Page,
    Text,
    icons,
)

MENU = [
    "/test/test/favorite",
    "/test/test/bookmark",
    "/home/home"
]


def template(body, page: Page):


    dlg = AlertDialog(
        title=Text("Hello, you!"), on_dismiss=lambda e: print("Dialog dismissed!")
    )

    def close_dlg(e):
        dlg_modal.open = False
        page.update()

    dlg_modal = AlertDialog(
        modal=True,
        title=Text("Please confirm"),
        content=Text("Do you really want to delete all those files?"),
        actions=[
            TextButton("Yes", on_click=close_dlg),
            TextButton("No", on_click=close_dlg),
        ],
        actions_alignment="end",
        on_dismiss=lambda e: print("Modal dialog dismissed!"),
    )

    def open_dlg(e):
        page.dialog = dlg
        dlg.open = True
        page.update()

    def open_dlg_modal(e):
        page.dialog = dlg_modal
        dlg_modal.open = True
        page.update()


    rail = NavigationRail(
        selected_index=MENU.index(page.route),
        label_type="all",
        # extended=True,
        min_width=100,
        min_extended_width=400,
        leading=FloatingActionButton(icon=icons.CREATE, text="Add",on_click=open_dlg_modal),
        group_alignment=-0.9,
        destinations=[
            NavigationRailDestination(
                icon=icons.FAVORITE_BORDER, 
                selected_icon=icons.FAVORITE, 
                label="First"
            ),
            NavigationRailDestination(
                icon_content=Icon(icons.BOOKMARK_BORDER),
                selected_icon_content=Icon(icons.BOOKMARK),
                label="Second",
            ),
            NavigationRailDestination(
                icon=icons.SETTINGS_OUTLINED,
                selected_icon_content=Icon(icons.SETTINGS),
                label_content=Text("Settings"),
            ),
        ],
        on_change=lambda e: page.go(MENU[e.control.selected_index]),
    )

    return Row(
            [
                rail,
                VerticalDivider(width=1),
                Column([body], alignment="start", expand=True),
            ],
            expand=True,
        )
    
