import flet as ft


def main(page: ft.Page):
    page.title ="Flet Icon Button Example"
    page.window.width = 400
    page.window.height = 600


    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER


    page.add(
        ft.IconButton(
            icon = ft.Icons.REMOVE,
            icon_color = "white",
            bgcolor = "grey",
            icon_size =30,
            tooltip= "Remove Item"


        )

    )
    

ft.run(main)