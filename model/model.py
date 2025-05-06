import networkx as nx

from database.DAO import DAO


class Model:

    def __init__(self):
        self._graph = nx.Graph()
        self._idMap={}
        for v in self._nodes:
            self._idMap[v.CCode]= v




    def buildGraph(self,year):
        self._nodes = DAO.getAllNodes()
        self.addAllEdges(year)
        self._graph.add_nodes_from(self._nodes)



    def addAllEdges(self,inputyear):
        edges = DAO.getAllEdges(self._idMap, inputyear)
        for edge in edges:
            self._graph.add_edge(edge.state1no, edge.state2no)



    def getNumNodes(self):
        return len(self._graph.nodes)

    def getNumEdges(self):
        return len(self._graph.edges)







