from flet import Text
from flet import ListView, Checkbox, Text,Row,Divider,Column

def favorite():
    lv = ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
    for i in range(100):
        lv.controls.append(Row([Checkbox(),Text(f"Line {i}")]))

    return Column([Row([Checkbox(),Text("Select all")]),lv], alignment="start", expand=True)