import flet as ft
import time

def main(page: ft.Page):
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    page.add(
        ft.Column(
            expand=True,
            alignment="center",
            horizontal_alignment="center",
            controls=[
                ft.Container(
                    expand=1,
                    border_radius=6,
                    bgcolor=ft.colors.with_opacity(0.025, ft.colors.WHITE10),
                    content=ft.Row(alignment="center", controls=[]),
                ),
                ft.Container(
                    expand=4,
                    border_radius=6,
                    bgcolor=ft.colors.with_opacity(0.025, ft.colors.WHITE10),
                ),
            ]
        )
    )

    page.update()


if __name__ == "__main__":
    ft.flet.app(target=main)
