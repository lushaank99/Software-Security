import graphviz

# Creates Graph in Question 2 and for POI event in Question 3 with nodes being just processes and process ids and representing the type of action they represent on edge
def create_graph_q2(logs):
    graph = graphviz.Digraph()
    for log in logs:
        # print(type(log[0]), type(log[2]))
        new_log = log[2].split(',')[0] + ', ' + log[2].split(',')[1]
        if "read" in log[1]:    
            graph.edge(new_log, log[0], label=log[1])
        elif "write" in log[1]:
            graph.edge(log[0], new_log, label=log[1])
	
    #print(graph)
    return graph

# Create Graph especially for Question 3 Backtracking in which nodes are represented by processes and process ids and representing the start and end time on the edges for the nodes
def create_graph_q3(logs):
    graph = graphviz.Digraph()
    for log in logs:
        # print(type(log[0]), type(log[2]))
        time = log[2].split(',')[3] + ',' + log[2].split(',')[4]
        new_log = log[2].split(',')[0] + ', ' + log[2].split(',')[1]
        if "read" in log[1]:   
            graph.edge(new_log, log[0], label=time)
        elif "write" in log[1]:
            graph.edge(log[0], new_log, label=time)
    # print(graph)
    return graph
    
fileOpen = open("file8.txt", 'r')
lines = fileOpen.readlines()
log_entries = []

# Initial creation of the nodes into the format mentioned in question 1
for line in lines:
    words = line.split(" ")
    sub = words[5] + ", " + words[6].replace('(','').replace(')','')
    oper = words[8]
    obj = words[3] + ", " + words[4].replace('(','').replace(')','') + ", " + words[-1].replace('\n','') + ', ' + words[1] + ', ' + words[-3].replace('latency=','')
    entry = (sub, oper, obj)
    log_entries.append(entry)
# print(log_entries)
    
new_log = []
for log in log_entries:
    if log not in new_log:
        new_log.append(log)
# print(len(log_entries), len(new_log))

parsedG = create_graph_q2(new_log)
# parsedG.view()
parsedG.render(filename='parsedGraph_01.dot')

# Iteratively going through each node and checking for the given POI Event and mentioning the same in the graph. Example used in this model is "gnome-shell -> mozStorage"
poievent = input("Give an POI event in the format a -> b: ")
a, b = poievent.split('->')
a, b = a.strip(), b.strip()
# print(a, b)
in_events = []
for log in new_log:
    if (log[0].split(',')[0] == a) and (log[2].split(',')[0] == b):
        in_events.append(log)
# print(in_events)

nodes = [a, ]
for node in nodes:
    for log in log_entries:
        new_node = log[2].split(',')[0].strip()
        # print(new_node, node)
        if new_node == node:
            # print(new_node)
            nodes.append(log[0].split(',')[0].strip())
            in_events.append(log)
# print(in_events)

eventG = create_graph_q2(in_events)
# eventG.view()
eventG.render(filename='poiGraph_01.dot')

# Implementing the Backtracking Algorithm mentioned in question 3
back_events = []
for log_1 in log_entries:
    for log_2 in log_entries:
        node_1 = log_1[2].split(',')[0].strip() + ',' + log_1[2].split(',')[1].strip()
        node_2 = log_2[0].split(',')[0].strip() + ',' + log_2[0].split(',')[1].strip()
        # print(node_1, node_2)
        if node_1 == node_2:
            end_1 = float(log_1[2].split(',')[-2]) + float(log_1[2].split(',')[-1])
            start_2 = float(log_2[2].split(',')[-2])
            if start_2 >= end_1:
                if log_1 not in back_events:
                    back_events.append(log_1)
                if log_2 not in back_events:
                    back_events.append(log_2)

backtrackG = create_graph_q3(back_events)
# backtrackG.view()
backtrackG.render(filename='backtrackGraph_01.dot')
