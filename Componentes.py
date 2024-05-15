import flet as ft


class AlertDialog:

    def __init__(self, page: ft.page):
        self.page = page

        btn1 = ft.ElevatedButton(text="ABRIR", on_click=self.open_ad)
        self.page.add(btn1)

        self.ad1 = ft.AlertDialog(
            title=ft.Text(value="Aviso importante"),
            content=ft.Text(
                value="voce esta prestes a deletar os dados da sessão, quer mesmo seguir?"
            ),
            content_padding=ft.padding.all(30),  # espaçamento interno
            inset_padding=ft.padding.all(10),  # espaçamento externo
            modal=True,  # valor padrao falso, se clicar fora d0 popup ele fecha, deixe verdadeiro para ser obrigatorio, porem devera add um botao
            shape=ft.RoundedRectangleBorder(radius=5),  # arredonda os cantos do popup
            on_dismiss=lambda _: print(
                "fechando "
            ),  # função que sera executada quando o usuario fechar o poppup
            actions=[  # lista com elementos flet, onde ficara dentro do pop up, botoes de aceitar ou cancelar por exemplo
                ft.TextButton(
                    text="cancelar", style=ft.ButtonStyle(color=ft.colors.RED)
                ),
                ft.TextButton(
                    text="Salvar",
                    style=ft.ButtonStyle(
                        color=ft.colors.WHITE, bgcolor=ft.colors.GREEN
                    ),
                    on_click=self.salvando,
                ),
            ],
            actions_alignment=ft.MainAxisAlignment.CENTER,  # alinha os elementos flet passando dentro do actions em alguma posição
        )

    def salvando(self, e):
        print("salvando seu arquivo")
        self.ad1.open = False
        self.page.update()

    def open_ad(self, e):
        # Carrega apenas um alerta por vez (crie outros page.dialog, caso precise de mais algum),
        self.page.dialog = self.ad1
        self.ad1.open = True
        self.page.update()


class Banner:
    def __init__(self, page: ft.Page):

        # CRIA UM POPUP NA PARTE SUPERIOR DA APLICAÇÃO EMPURRANDO O CENTEUDO PARA BAIXO E DESTACANDO ELE MESMO, USADO PARA ANUNCIAR QUE HOUVE ALGUM ERRO AO SINCRONIZAR ALGO, OU CARREGAR
        self.page = page

        self.botao = ft.ElevatedButton(text="ABRIR", on_click=self.open_banner)
        self.page.add(self.botao)

        self.banner1 = ft.Banner(
            actions=[
                ft.TextButton(
                    text="cancelar",
                    style=ft.ButtonStyle(color=ft.colors.RED),
                    on_click=self.close_banner,
                ),
                ft.ElevatedButton(
                    text="tentar novamente",
                    style=ft.ButtonStyle(
                        bgcolor=ft.colors.GREEN, color=ft.colors.WHITE
                    ),
                    on_click=self.close_banner,
                ),
            ],
            content=ft.Text(
                value="Ops, parece que nao conseguimos processar sua solicitação no momento"
            ),
            content_padding=ft.padding.all(20),  # espaçamento interno do conteudo
            leading=ft.Icon(
                name=ft.icons.WARNING_AMBER
            ),  # adiciona um icone de alerta no inicio do texto
            force_actions_below=True,  # faz que as ações sempre deixa os botoes de opções como cancelar e continuar na parte inferior deixando responsivo
            bgcolor=ft.colors.BLACK,
        )

    def close_banner(self, e):
        self.page.banner.open = False
        self.page.update()

    def open_banner(self, e):

        self.page.banner = self.banner1
        self.banner1.open = True
        self.page.update()


class BottomSheet:
    def __init__(self, page: ft.Page):

        self.page = page

        self.btn = ft.ElevatedButton(text="Abrir", on_click=self.show_bs)
        self.page.add(self.btn)

        # componente muito utilizado para projetos mobile, para mostrar detralhes de algo para o usuario sem precisar ter uma demora de renderização
        self.bs = ft.BottomSheet(
            content=ft.Container(
                ft.Column(
                    controls=[
                        ft.Text(value="Titulo", style=ft.TextThemeStyle.HEADLINE_LARGE),
                        ft.Text(
                            value="Conteudo do bottomsheet",
                            style=ft.TextThemeStyle.HEADLINE_MEDIUM,
                        ),
                        ft.FilledButton(text="Fechar", on_click=self.close_bs),
                    ]
                ),
                padding=20,
            ),
            dismissible=False,  # Caso estiver FALSE sera necessario criar um  botao que feche o BS, se True, clicando em qualquer lugar da tela ele fecha sozinho
            enable_drag=True,  # Consegue esticar o BS para aumentar ou diminuir a visualização
            is_scroll_controlled=False,  # Habilita o scrol do mouse porem aumenta o tamanho max do BS, e no mobile habilita arrastar
            maintain_bottom_view_insets_padding=True,  # Usada para os mobile, para nao sobrepor na visuzaliação dos botos de navegação do celular, add um espaçamento
            show_drag_handle=True,  # Icone visual para ilustrar que é possiveis mover o BS para cima ou para baixo
        )
        self.page.overlay.append(self.bs)

    def show_bs(self, e):
        self.bs.open = True
        self.page.update()

    def close_bs(self, e):
        self.bs.open = False
        self.page.update()


class SnackBar:
    def __init__(self, page: ft.Page):
        self.page = page

        self.btn = ft.ElevatedButton(text="executar", on_click=self.show_snackbar)
        self.page.add(self.btn)

        # Usado para criar uma mini notificação na parte inferirior do app
        self.page.snack_bar = ft.SnackBar(
            content=ft.Text(value="Não foi possivel processar os dados nesse momento"),
            bgcolor=ft.colors.RED_100,
            show_close_icon=True,
            close_icon_color=ft.colors.RED,
            padding=ft.padding.all(12),
            duration=10000,
            behavior=ft.SnackBarBehavior.FLOATING,  # botao flutuante
            margin=ft.margin.all(50),
            dismiss_direction=ft.DismissDirection.START_TO_END,  # ação que fecha a notificação arrastanto para o lado informado
            action="Confirmar",
            action_color=ft.colors.GREEN,
            on_action=lambda _: print(
                "ação selecionada"
            ),  # função que é chamada no aciton
        )

    def show_snackbar(self, e):
        self.page.snack_bar.open = True
        self.page.update()


class DatePicker:

    def __init__(self, page: ft.page):

        import datetime

        self.page = page

        # criação de calendario
        dp = ft.DatePicker(
            cancel_text="Cancelar",
            confirm_text="Confirmar",
            error_format_text="Data invalida",
            field_hint_text="MM/DD/YYYY",
            field_label_text="Digite uma data",
            help_text="Selecione uma data no Calendario",
            switch_to_calendar_icon=ft.icons.CALENDAR_MONTH,
            switch_to_input_icon=ft.icons.EDIT,
            date_picker_mode=ft.DatePickerMode.YEAR,
            date_picker_entry_mode=ft.DatePickerEntryMode.INPUT,
            value=datetime.date(2024, 1, 5),  # valor padrao
            first_date=datetime.date(2024, 1, 1),  # data minima
            last_date=datetime.date(2024, 1, 20),  # data maxima
            error_invalid_text="Data fora do limite permitido",
            on_change=lambda _: print(dp.value),
            keyboard_type=ft.KeyboardType.NUMBER,  # libera apenas o teclado numerico em dispositivos moveis
        )
        self.page.overlay.append(dp)
        btn = ft.ElevatedButton(text="abrir", on_click=lambda _: dp.pick_date())
        self.page.add(btn)


class TimePicker:
    def __init__(self, page: ft.Page):
        import datetime

        self.page = page

        # Cria um relogio para o usuario selecionar um horario

        tp = ft.TimePicker(
            cancel_text="Cancelar",
            confirm_text="Confirmar",
            error_invalid_text="Hora invalida",
            hour_label_text="Hora",
            minute_label_text="Minutos",
            help_text="Selecione a hora",
            time_picker_entry_mode=ft.TimePickerEntryMode.INPUT,
            value=datetime.time(10, 31, 18),
            on_change=lambda _: print(tp.value),
        )
        self.page.overlay.append(tp)

        btn = ft.ElevatedButton("abrir", on_click=lambda _: tp.pick_time())
        self.page.add(btn)


class Tabs:
    def __init__(self, page: ft.Page):
        self.page = page

        # Usado para separar varias informações em telas diferentes, sendo de facil visualização

        t = ft.Tabs(
            tabs=[
                ft.Tab(
                    text="Tab 1",
                    content=ft.Container(
                        padding=ft.padding.all(30), content=ft.Text("conteudo da TAB1")
                    ),
                ),
                ft.Tab(icon=ft.icons.SETTINGS, content=ft.Text("Conteudo da tab 3")),
                ft.Tab(  # pode add qualquer componente flet
                    tab_content=ft.Container(
                        content=ft.Badge(
                            bgcolor=ft.colors.GREEN,
                            content=ft.CircleAvatar(
                                foreground_image_url="data:image/webp;base64,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",
                                tooltip="bagreham",
                            ),
                            small_size=10,
                        ),
                    ),
                ),
            ],
            selected_index=2,  # qual tab vai ficar selecionada quando abrir o sistema
            animation_duration=100,  # tempo para mudar de tab - animação
            divider_color=ft.colors.AMBER,  # linha que divide toda a tela com as tabs
            indicator_border_radius=ft.border_radius.all(
                10
            ),  # borda da linha que seleciona a tab,
            indicator_color=ft.colors.RED,  # cor da linha que seleciona a tab,
            indicator_padding=ft.padding.all(5),
            indicator_tab_size=True,  # se a linha deve ter o tamanho da tab ou nao
            label_color=ft.colors.GREEN,  # cor da tab quando é selecionada,
            unselected_label_color=ft.colors.BLUE,  # Cor quando a tab nao esta selecionada,
            overlay_color={  # um dicionario com todos os estados de um botao, e mouse
                ft.MaterialState.HOVERED: ft.colors.PINK
            },
            scrollable=False,  # quando tiver poucas tabs habilite este modo em modo False, ele ira
        )

        self.page.add(t)


class Basics:
    def __init__(self, page: ft.Page):
        self.page = page

        self.page.add(
            ft.Text(value="Text"),
            ft.Divider(),
            ft.Image(src="images/negao.png", width=100, height=100),
            ft.Divider(),
            ft.Icon(name=ft.icons.BOLT_SHARP, size=50, tooltip="icone"),
            ft.Divider(),
            ft.ElevatedButton(text="ElevatedButton"),
            ft.FilledButton(text="FilledButton"),
            ft.FilledTonalButton(text="FilledTonalButton"),
            ft.FloatingActionButton(icon=ft.icons.ADD),
            ft.Divider(),
            ft.IconButton(icon=ft.icons.PEOPLE_OUTLINE_OUTLINED),
            ft.Divider(),
            ft.PopupMenuButton(
                items=[ft.PopupMenuItem("item 1"), ft.PopupMenuItem("item2")]
            ),
            ft.Divider(),
            ft.TextButton(text="TextButton"),
            ft.Divider(),
        )


ft.app(target=Basics, assets_dir="assets")
