import bayesianpia2 as bnp
# create a Bayesian Network
nodes = ["C", "S", "R", "W"]
edges = {
    "C": {},
    "S": {"C"},
    "R": {"C", "S"},
    "W": {"R"}
}
bn = bnp.BayesianNetwork(nodes, edges)

# define the conditional probabilities for each node
bn.factors["C"] = {(): 0.5}
bn.factors["S"] = {(True,): 0.8, (False,): 0.2}
bn.factors["R"] = {
    (True, True): 0.99, (True, False): 0.9,
    (False, True): 0.6, (False, False): 0.01
}
bn.factors["W"] = {
    (True,): 0.9, (False,): 0.1
}

# check if the network is fully described
print(bn.is_fully_described())  # True

# get the compact representation of the network
print(bn.get_compact_representation())

# compute the factor for the node "R" with evidence {"C": True, "S": False}
bn.compute_factor("R", {"C": True, "S": False})
print(bn.factors["R"])
