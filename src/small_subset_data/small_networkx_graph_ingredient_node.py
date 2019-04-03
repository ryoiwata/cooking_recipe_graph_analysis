#For graphing
import matplotlib.pyplot as plt
import networkx as nx

#For using a pickled dictionary
import pickle

#Opening the pickled file
pickle_in = open("small_flavor_matrix_dict_ingredient_node.pickle","rb")

#Getting the dictionary from the pickle
flavor_matrix_dict = pickle.load(pickle_in)

print(flavor_matrix_dict)



#Converting a dictionary of dictionaries to a graph
G = nx.from_dict_of_dicts(flavor_matrix_dict)

print(G.edges.data('shared_molecules', default=1))
print(G.number_of_edges())
print(G.number_of_nodes())

# #getting all the weights of each edge
# all_weights = []
# for (node1,node2,data) in G.edges(data=True):
#     all_weights.append(data['shared_molecules'])

# #getting the unique weights of all the edges
# unique_weights = list(set(all_weights))

# for weight in unique_weights:
#         #4 d. Form a filtered list with just the weight you want to draw
#         weighted_edges = [(node1,node2) for (node1,node2,edge_attr) in G.edges(data=True) if edge_attr['shared_molecules']==weight]
#         width = weight*G.number_of_nodes()/sum(all_weights)
#         nx.draw_networkx_edges(G,pos=nx.spring_layout(G), edgelist=weighted_edges,width=width)
# # plt.axis('off')
# # plt.show() 


#Plotting the Graph 
fig, ax = plt.subplots(1, 1, figsize=(8, 6))
nx.draw_networkx(G, ax=ax)
plt.show()