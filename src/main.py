import flet as ft


def main(page: ft.Page):
    page.title = "Hello Flet"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    page.add(
        ft.Text("Hello, World! 👋", size=32, weight=ft.FontWeight.BOLD),
        ft.Text("Built with Flet 1.0"),
    )


ft.run(main)
