import flet as ft

class AlertDialog():

    def __init__(self, page: ft.page):
        self.page = page

        btn1 = ft.ElevatedButton(text="ABRIR", on_click=self.open_ad)
        self.page.add(btn1)

        self.ad1 = ft.AlertDialog(
            title = ft.Text(value="Aviso importante"),
            content= ft.Text(value="voce esta prestes a deletar os dados da sessão, quer mesmo seguir?"),
            content_padding= ft.padding.all(30), # espaçamento interno 
            inset_padding = ft.padding.all(10), # espaçamento externo
            modal = True, # valor padrao falso, se clicar fora d0 popup ele fecha, deixe verdadeiro para ser obrigatorio, porem devera add um botao
            shape= ft.RoundedRectangleBorder(radius=5), # arredonda os cantos do popup
            on_dismiss = lambda _:print("fechando "),#função que sera executada quando o usuario fechar o poppup
            actions=[ # lista com elementos flet, onde ficara dentro do pop up, botoes de aceitar ou cancelar por exemplo
                ft.TextButton(text="cancelar", style=ft.ButtonStyle(color=ft.colors.RED)),
                ft.TextButton(text="Salvar", style=ft.ButtonStyle(color=ft.colors.WHITE, bgcolor=ft.colors.GREEN), on_click=self.salvando),

            ],
            actions_alignment=ft.MainAxisAlignment.CENTER, # alinha os elementos flet passando dentro do actions em alguma posição
    
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
    
class Banner():
    def __init__(self, page: ft.Page):

        #CRIA UM POPUP NA PARTE SUPERIOR DA APLICAÇÃO EMPURRANDO O CENTEUDO PARA BAIXO E DESTACANDO ELE MESMO, USADO PARA ANUNCIAR QUE HOUVE ALGUM ERRO AO SINCRONIZAR ALGO, OU CARREGAR
        self.page = page

        self.botao = ft.ElevatedButton(text="ABRIR", on_click=self.open_banner)
        self.page.add(self.botao)




        self.banner1 = ft.Banner(
            actions=[
                ft.TextButton(text="cancelar", style=ft.ButtonStyle(color=ft.colors.RED), on_click=self.close_banner),
                ft.ElevatedButton(text="tentar novamente", style=ft.ButtonStyle(bgcolor=ft.colors.GREEN, color=ft.colors.WHITE), on_click=self.close_banner),
            ],
            content= ft.Text(value="Ops, parece que nao conseguimos processar sua solicitação no momento"),
            content_padding= ft.padding.all(20), #espaçamento interno do conteudo
            leading= ft.Icon(name=ft.icons.WARNING_AMBER), # adiciona um icone de alerta no inicio do texto
            force_actions_below= True, #faz que as ações sempre deixa os botoes de opções como cancelar e continuar na parte inferior deixando responsivo
            bgcolor= ft.colors.BLACK
        )


    def close_banner(self, e):
        self.page.banner.open = False
        self.page.update()

    def open_banner(self, e):
                
        self.page.banner = self.banner1
        self.banner1.open = True
        self.page.update()



ft.app(target=Banner)