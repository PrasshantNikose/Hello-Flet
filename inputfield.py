import flet as ft


def main(page: ft.Page):
    page.title ="Flet Input TextField Example"
    page.window.width = 400
    page.window.height = 600


    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    page. horizontal_alignment = ft.CrossAxisAlignment.CENTER


    # 1. Define the TextField
    user_input = ft.TextField(label="Enter Name")

    page.add(user_input)
    

ft.run(main)