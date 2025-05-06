from model.model import Model

mymodel = Model()
mymodel.buildGraph(1900)
print(f" n nodi : {mymodel.getNumNodes()} e n archi: {mymodel.getNumEdges()}")

