import flet as ft
import time

def main(page: ft.Page):
    first_name = ft.TextField(value="Gerard")
    last_name = ft.TextField(value="Dupont")
    first_name.disabled = False
    last_name.disabled = False
    page.add(first_name, last_name)



ft.app(main)