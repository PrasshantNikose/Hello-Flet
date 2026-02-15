import flet as ft

def main(page: ft.Page):
    page.title = "Flet Button Example"
    page.window.width = 400
    page.window.height = 600


    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    page.horizontal_alignment = ft.CrossAlignment.CENTER



    page.add( ft.ElevatedButton("Submit"))


 

ft.run(main)

