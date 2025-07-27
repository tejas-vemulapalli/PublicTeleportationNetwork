def djikistri(startStation, graph):
    weights = {node: float('inf') for node in graph}
    previous = {node: None for node in graph }

    weights[startStation] = 0
    vistedPlaces = set()

    while len(graph) > len(vistedPlaces):
        current = None

        for node in graph:
            if node not in vistedPlaces and (current is None or weights[node] < weights[current]):
                current = node

        if current is None:
            break

        for nextNode, weight in graph[current]:
            if nextNode not in vistedPlaces:
                newWeight = weights[current] + weight

                if newWeight < weights[nextNode]:
                    weights[nextNode] = newWeight
                    previous[nextNode] = current
        
        vistedPlaces.add(current)

    route = {}
    for node in graph:
        if weights[node] == float('inf'):
            route[node] = None
        else:
            temp = node
            tempPath = []
            while temp != None:
                tempPath.insert(0,temp)
                temp = previous[temp]
        
            route[node] = tempPath

    return weights, previous, route

graph = {
    'CA':[('WC', 2.47),('EL',2.47),('NC',2.47),('ST',2.47)],
    'IP':[('NC',0.8)],
    'NC':[('IP',0.96),('WC',0.96)],
    'WC':[('CA', 1.75),('EL',1.75),('NC',1.75),('ST',1.75)],
    'ST':[('WC', 1.28),('NNP',1.28) ,('CA',1.28)]
    'NNP':[('ST',1.63)],
    'EL': [('WC',1.01),('CA',1.01)]
}

startStation = input("Starting Station: ")
destStation = input("Ending Station: ")
pit1 = input ("Pit stop (if none don't type): ")

weights, previous, route = djikistri(startStation, graph)
#print(str(weights + previous + route))

if pit1 == "":
    print(f"Shortest distance from {startStation} to {destStation}: {round(weights[destStation],2)}, path: {'--> '.join(route[destStation])} ")
else:
    indexNumRemove= len(route[pit1]) - 1
    del route[pit1][indexNumRemove]
    pitRoute = '--> '.join(route[pit1])
    pitWeight = weights[pit1]
    weights, previous, route = djikistri(pit1, graph)
    print(f"Shortest distance from {startStation} to {destStation} via {pit1}: {round(weights[destStation]+ pitWeight, 2)}, path:{pitRoute}--> {'--> '.join(route[destStation])}  ")
