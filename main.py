import flet as ft
import time

GOLD: list = [
    (0, 273.60),
    (1, 279.00),
    (2, 348.20),
    (3, 363.70),
    (4, 438.40),
    (5, 518.90),
    (6, 638.00),
    (7, 833.75),
    (8, 874.75),
    (9, 1096.50),
    (10, 1226.75),
    (11, 1577.00),
    (12, 1668.75),
    (13, 1200.00),
    (14, 1184.75),
    (15, 1061.25),
    (16, 1151.00),
    (17, 1257.25),
    (18, 1301.50),
    (19, 1493.25),
    (20, 1906.25),
    (21, 1753.90),
    (22, 1980.40),
]

BTC: list= [
    (9, 0.0008),
    (10, 0.07),
    (11, 0.95),
    (12, 13.44),
    (13, 817.36),
    (14, 314.24),
    (15, 430.05),
    (16, 963.74),
    (17, 13880.74),
    (18, 3843.52),
    (19, 7191.68),
    (20, 29001.19),
    (21, 39800.00),
]


class TimeChart(ft.UserControl):
    def __init__(self):
        self.data_points: list = []
        self.points: list = GOLD

        self.chart = ft.LineChart(
            tooltip_bgcolor=ft.colors.with_opacity(0.8, ft.colors.WHITE),
            expand=True,
            min_y=int(min(self.points, key=lambda y: y[1])[1]),
            max_y=int(max(self.points, key=lambda y: y[1])[1]),
            min_x=int(min(self.points, key=lambda x: x[0])[0]),
            max_x=int(max(self.points, key=lambda x: x[0])[0]),

            left_axis=ft.ChartAxis(labels_size=50),
            bottom_axis=ft.ChartAxis(labels_size=40, labels_interval=1),
        )

        super().__init__()

    
    def build(self):

        self.line_chart.data_points = self.data_points
        self.chart.data_series = [self.line_chart]

        return ft.Column(
            horizontal_alignment="center",
            controls=[
                ft.Text(
            "Yearly Historical Prices for Bitcoin and Gold",
            size=16,
            weight="bold",

                ),
                self.chart,
            ]
        )


def main(page: ft.Page):
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    chart = TimeChart()
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
                    content=chart, 
                ),
            ]
        )
    )

    page.update()


if __name__ == "__main__":
    ft.flet.app(target=main)
