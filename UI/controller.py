import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.biblioteca_selezionata = None
        self.genere_selezionato = None

    # POPOLA DROPDOWN
    def popola_dropdown(self):
        """ Inizializza i dropdown con l'opzione 'Nessun filtro' e i dati presi dal DB """
        # Dropdown Biblioteche
        biblioteche = self._model.get_biblioteche()
        self._view.dd_biblioteca.options.clear()
        self._view.dd_biblioteca.options.append(ft.dropdown.Option(key="ALL", text="Nessun filtro"))
        for b in biblioteche:
            self._view.dd_biblioteca.options.append(ft.dropdown.Option(key=str(b.id), text=b.nome))

        # Dropdown Generi
        generi = self._model.get_generi()
        self._view.dd_genere.options.clear()
        self._view.dd_genere.options.append(ft.dropdown.Option(key="ALL", text="Nessun filtro"))
        for g in generi:
            self._view.dd_genere.options.append(ft.dropdown.Option(key=g, text=g))

        self._view.update()

    # CALLBACKS DROPDOWN
    def read_biblioteca(self, e):
        """ Callback al cambio di selezione nel Dropdown Biblioteca """
        val = self._view.dd_biblioteca.value
        if val is None or val == "ALL" or val == "Nessun filtro":
            self.biblioteca_selezionata = None
        else:
            self.biblioteca_selezionata = int(val)

    def read_genere(self, e):
        """ Callback al cambio di selezione nel Dropdown Genere """
        val = self._view.dd_genere.value
        if val is None or val == "ALL" or val == "Nessun filtro":
            self.genere_selezionato = None
        else:
            self.genere_selezionato = val

    # AZIONE: MOSTRA LIBRI
    def handle_mostra_libri(self, e):
        """ Gestisce il click sul pulsante 'Mostra Libri' e aggiorna la ListView """
        libri = self._model.get_libri_filtrati(self.biblioteca_selezionata, self.genere_selezionato)

        # Pulizia della ListView
        self._view.lst_libri.controls.clear()

        if not libri:
            self._view.show_alert("Nessun libro trovato per i filtri selezionati.")
        else:
            for libro in libri:
                self._view.lst_libri.controls.append(ft.Text(str(libro)))

        self._view.update()