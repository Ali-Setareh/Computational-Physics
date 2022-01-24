import matplotlib.pyplot as plt
from networkx import nx
import collections
from sys import getsizeof

n=500 #number of nodes
mean_deg=1 #mean degree
p=mean_deg/n #probability of connecting an edge
G=nx.fast_gnp_random_graph(n,p) #erdos renyi graph
degree_sequence = sorted([d for n, d in G.degree()], reverse=True)  # degree sequence
degreeCount = collections.Counter(degree_sequence)
clusting=nx.clustering(G).values()
deg, cnt = zip(*degreeCount.items())
fig=plt.figure()
ax=fig.add_subplot(111)
#ax.set_title('mean degree distribution')
ax.set_xlabel('degree')
ax.set_ylabel('number of nodes')
ax.bar(deg,cnt)
#plt.savefig("deg distribution"+str(mean_deg)+".png")
fig2,ax2=plt.subplots()
ax2.hist(clusting)
#ax2.set_title('clustering distribution')
ax2.set_xlabel('clustering')
ax2.set_ylabel('number of nodes')
#plt.savefig('clutering distribution%s.png'%str(mean_deg))
edges=nx.to_edgelist(G)
adj_matrix=nx.to_numpy_array(G)
adj_list=nx.generate_adjlist(G)
fig3=plt.figure()
nx.draw(G,pos=nx.circular_layout(G),node_size=0.5)
#plt.savefig('graph %s.png'%str(mean_deg))
print('memory size of edge list in bytes:',getsizeof(list(edges)))
print('memory size of adjacency matrix in bytes:',getsizeof(adj_matrix))
print('memory size of adjacency list in bytes:',getsizeof(list(adj_list)))

plt.show()

