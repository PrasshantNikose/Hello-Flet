import flet as ft

def main(page: ft.Page):
    page.title = "Toggle Button Example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def toggle_icon(e):
        # Toggle the 'selected' state
        e.control.selected = not e.control.selected
        e.control.update()
        print(f"Toggled to: {e.control.selected}")

    toggle_btn = ft.IconButton(
        icon=ft.Icons.FAVORITE_BORDER,
        selected_icon=ft.Icons.FAVORITE,
        selected=False,
        icon_color=ft.Colors.GREY,
        selected_icon_color=ft.Colors.RED,
        on_click=toggle_icon,
    )

    page.add(ft.Text("Click to Favorite:"), toggle_btn)

ft.run(main)