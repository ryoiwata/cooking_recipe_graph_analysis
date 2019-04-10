"""
Takes entire data, and then makes a graph based off of nodes of ingredients and molecules
"""
#Python Library for Dataframe usage
import pandas as pd
import numpy as np

#Serializing to a file
import _pickle as pickle

#Libraries for Graph
import networkx as nx

#PandaDF of ingredients and their associated flavor molecules (with ingredients that are not cooked and have recipes)
#Opening the pickled file
pickle_in = open("./data/ingredients/ingredient_only_pd.pickle", "rb")

#Getting the dictionary from the pickle
ingredient_only_pd = pickle.load(pickle_in)


#Initializing Graph
G=nx.Graph()

x = 0
#iterate through each row of flavorDB based on if index is in random sample
for index, row in ingredient_only_pd.iterrows():
    x += 1

    #name of the ingredient from the "rows" 
    ingredient_1 = row["ingredient"]

    #set of the ingredient from the "rows"
    set_of_molecules= row["set_molecules"]

    #category of the ingredient from the "rows"
    category = row["category"]

    # to keep track of what's going on
    for molecule in set_of_molecules:
        #creating an ingredient node and adding attributes
        G.add_node(ingredient_1)
        G.node[ingredient_1]["ingredient_node"] = True
        G.node[ingredient_1]["molecule_node"] = False
        G.node[ingredient_1]["category"] = category
        
        #creating a molecule node and adding attribute
        G.add_node(molecule)
        G.node[molecule]["molecule_node"] = True
        G.node[molecule]["ingredient_node"] = False
        G.add_edge(ingredient_1, molecule)

#writes the pickle into the data file
#makes it so that needs to be called in src folder
with open('./data/graph/molecule_full_graph.pickle', 'wb') as file:
    file.write(pickle.dumps(G))
    file.close()

list_of_ingredients = list(ingredient_only_pd["ingredient"])
#writes the pickle into the data file
#makes it so that needs to be called in src folder
with open('./data/ingredients/ingredient_full_list.pickle', 'wb') as file:
    file.write(pickle.dumps(list_of_ingredients))
    file.close()
