import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_graph(self, e):
        self._model.buildGraph()
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f"Numero vertici: {self._model._graph.number_of_nodes()}"
                                                      f"numero archi: {self._model._graph.number_of_edges()}"))
        for l in self._model._nodes:
            self._view.ddLoca.options.append(ft.dropdown.Option(l))
        self._view.update_page()



    def handle_stats(self, e):
        local = self._view.ddLoca.value

        self._view.txt_result2.controls.clear()
        self._view.txt_result2.controls.append(ft.Text(f"Localizzazione selezionata: {local}"))

        connected_localizations = self._model.get_connected_localizations(local)
        for loc, edge_data in connected_localizations:
            weight = edge_data['weight']
            self._view.txt_result2.controls.append(ft.Text(f"Localizzazione: {loc}, Peso dell'arco: {weight}"))

        self._view.update_page()

    def handle_search(self, e):
        pass