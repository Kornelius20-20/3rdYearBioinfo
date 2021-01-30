import networkx as nx


with open('string_interactions.tsv') as f:
    lines = f.readlines()[1:]

gr = nx.Graph()

for line in lines:
    hold = line.rstrip().split('\t')

    gr.add_edge(hold[0],hold[1],weight=hold[-1])

print(gr.degree['ERF24'])

