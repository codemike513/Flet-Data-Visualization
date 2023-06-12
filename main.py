import flet as ft
import time

def main(page: ft.Page):
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"


    page.update()


if __name__ == "__main__":
    ft.flet.app(target=main)
