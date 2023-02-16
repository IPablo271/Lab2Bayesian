import bayesianpia2 as bnp
# Creacion de la red bayesiana
nodes = ["C", "S", "R", "W"]
edges = {
    "C": {},
    "S": {"C"},
    "R": {"C", "S"},
    "W": {"R"}
}
bn = bnp.BayesianNetwork(nodes, edges)

# Definicion de las probabilidades condicionales
bn.factors["C"] = {(): 0.5}
bn.factors["S"] = {(True,): 0.8, (False,): 0.2}
bn.factors["R"] = {
    (True, True): 0.99, (True, False): 0.9,
    (False, True): 0.6, (False, False): 0.01
}
bn.factors["W"] = {
    (True,): 0.9, (False,): 0.1
}

# Verificar si la red esta totalmente descrta
print("La red esta completamente descrita: "+str(bn.is_fully_described()))  

#Forma compacta de la red
print("Forma compacta de la red: "+bn.compact())

#Tabla de representacion de la red
print(bn.representation())

#Computar los factores 
bn.compute_factor("R", {"C": True, "S": False})
print(bn.factors["R"])


