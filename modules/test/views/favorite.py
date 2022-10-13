
from flet import ListView, Checkbox, Text,Row,TextButton,Column,Text,Page

def favorite(page: Page):
    lv = ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
    for i in range(100):
        lv.controls.append(Row([Checkbox(),Text(f"Line {i}")]))
    def back(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)
        
    return Column(
        [
            TextButton("test",on_click= back),
            Row([Checkbox(), Text("Select all")]),
            lv
        ], alignment="start", expand=True)