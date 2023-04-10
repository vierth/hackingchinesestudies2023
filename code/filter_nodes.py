import time
with open('edges.tsv', 'r', encoding='utf8') as rf:
    edge_data = rf.read().split("\n")
    header= edge_data[0]
    edge_data = edge_data[1:]
    edge_data = [d.split("\t") for d in edge_data]
    
seen_nodes = set()
for d in edge_data:
    print(seen_nodes)
    seen_nodes.add(d[0])
    seen_nodes.add(d[1])
    

with open('nodes.tsv', 'r', encoding='utf8') as rf:
    node_data = rf.read().split("\n")
    node_data = [d.split("\t") for d in node_data]

filtered_nodes = ["\t".join(d) for d in node_data if d[0] in seen_nodes]

with open('filtered_nodes.tsv','w', encoding='utf8') as wf:
    wf.write(header+"\n")
    wf.write("\n".join(filtered_nodes))