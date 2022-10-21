from flet import (
    Column,
    Icon,
    NavigationRail,
    NavigationRailDestination,
    Row,
    Text,
    VerticalDivider,
    Page,
    Text,
    icons,
)

MENU = [
    "/scheduler/scheduler",
    "/scheduler/scheduler/vault",
    "/home/home"
]


def template(body, page: Page):

    def auto_redirect(e):
        try:
            page.go(e)
        except Exception(e):
            print(e)

    rail = NavigationRail(
        selected_index=MENU.index(page.route),
        label_type="all",
        # extended=True,
        min_width=100,
        min_extended_width=400,
        group_alignment=-0.9,
        destinations=[
            NavigationRailDestination(
                icon=icons.EVENT_OUTLINED, 
                selected_icon=icons.EVENT, 
                label="Sceduler"
            ),
            NavigationRailDestination(
                icon_content=Icon(icons.PASSWORD_OUTLINED),
                selected_icon_content=Icon(icons.PASSWORD),
                label="Vault",
            ),
            NavigationRailDestination(
                icon=icons.SETTINGS_OUTLINED,
                selected_icon_content=Icon(icons.SETTINGS),
                label_content=Text("Settings"),
            ),
        ],
        on_change=lambda e: auto_redirect(MENU[e.control.selected_index]),
    )

    return Row(
            [
                rail,
                Column([body], expand=True, scroll="auto"),
            ],
            expand=True,
            
    )
    
