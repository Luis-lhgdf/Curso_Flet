import flet as ft


def main(page: ft.Page):

    page.title = "Contador"

    text_number = ft.TextField(
        value="0",
        width=100,
        text_align=ft.TextAlign.CENTER,
        input_filter=ft.NumbersOnlyInputFilter(),
        col={"xs": 12, "sm": 4},
    )

    def somar(e):
        text_number.value = str(int(text_number.value) + 1)
        text_number.update()

    def subtrair(e):
        text_number.value = str(int(text_number.value) - 1)
        text_number.update()

    page.add(
        ft.ResponsiveRow(
            controls=[
                ft.IconButton(
                    icon=ft.icons.ADD,
                    on_click=somar,
                    col={"xs": 12, "sm": 4},
                ),
                text_number,
                ft.IconButton(
                    icon=ft.icons.REMOVE,
                    on_click=subtrair,
                    col={"xs": 12, "sm": 4},
                ),
            ],
            expand=True,
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

    page.update()


ft.app(target=main, assets_dir="assets")
