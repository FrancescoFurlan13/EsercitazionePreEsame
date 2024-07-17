from database.DAO import DAO
import networkx as nx


class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._nodes=[]
        self._edges=[]

        self._localization = []
        self._interactions = []

    def loadLoc(self):
        self._localization = DAO.getLoc()

    def loadInter(self):
        self._interactions = DAO.getLocInter()


    def buildGraph(self):
        self._nodes = DAO.getLoc()
        self._graph.add_nodes_from(self._nodes)

        for i in DAO.getLocInter():
            self._graph.add_edge(i[0], i[1], weight=i[2])

    def get_connected_localizations(self, localization):
        if localization not in self._graph:
            return []

        # Recupera le localizzazioni connesse e i dettagli dell'arco
        connected = list(self._graph[localization].items())
        return connected
















