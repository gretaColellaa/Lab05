import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff

        self.txt_matricola = None
        self.txt_cognome = None
        self._page = page
        self._page.title = "Lab O5 - segreteria studenti"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txt_nome = None
        self.btn_hello = None
        self.txt_result = None
        self.txt_container = None
        self.ddCorso = None

    def load_interface(self):
        """Function that loads the graphical elements of the view"""
        # title
        self._title = ft.Text("App gestione studenti", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW with some controls
        self.ddCorso = ft.Dropdown(label = "Corso",
                                   width=550,
                                   hint_text="Selezionare un corso",
                                   options=[],
                                   autofocus=True,
                                   on_change=self._controller.leggi_corso)

        self._controller.populate_dd_corso()

        self.btn_cercaIscritti = ft.ElevatedButton(text = "Cerca iscritti", on_click=self._controller.handle_cercaiscritti)


        row1 = ft.Row([self.ddCorso, self.btn_cercaIscritti],
                      alignment=ft.MainAxisAlignment.CENTER)

        # text field for the name
        self.txt_matricola = ft.TextField(
            label="matricola",
            width=200,
            hint_text="matricola"
        )
        self.txt_nome = ft.TextField(
            label="nome",
            width=250,
            hint_text="nome",
            read_only = True

        )
        self.txt_cognome = ft.TextField(
            label="cognome",
            width=250,
            hint_text="cognome",
            read_only = True
        )

        row2 = ft.Row([self.txt_matricola, self.txt_nome, self.txt_cognome], alignment=ft.MainAxisAlignment.CENTER)

        self.btn_cercaStudente = ft.ElevatedButton(text = "Cerca studente", on_click = self.controller.handle_cercaStudente)
        self.btn_cercaCorsi = ft.ElevatedButton(text = "cerca corsi", on_click = self.controller.cerca_corsi)
        self.btn_iscrivi = ft.ElevatedButton(text = "iscrivi", on_click = self.controller.iscrivi)
        row3 = ft.Row([self.btn_cercaStudente,self.btn_cercaCorsi, self.btn_iscrivi], alignment=ft.MainAxisAlignment.CENTER)

        self._page.controls.append(row1)
        self._page.controls.append(row2)
        self._page.controls.append(row3)



        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        """Function that opens a popup alert window, displaying a message
        :param message: the message to be displayed"""
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
