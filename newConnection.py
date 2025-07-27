import itertools
import copy

start = input('Starting Station: ')
def djikistri(startStation, graph):
    weights = {node: float('inf') for node in graph}
    previous = {node: None for node in graph}
    weights[startStation] = 0
    visitedPlaces = set()

    while len(visitedPlaces) < len(graph):
        current = None
        for node in graph:
            if node not in visitedPlaces and (current is None or weights[node] < weights[current]):
                current = node

        if current is None:
            break

        for nextNode, weight in graph[current]:
            if nextNode not in visitedPlaces:
                newWeight = weights[current] + weight
                if newWeight < weights[nextNode]:
                    weights[nextNode] = newWeight
                    previous[nextNode] = current

        visitedPlaces.add(current)

    route = {}
    for node in graph:
        l = 0
        if weights[node] == float('inf'):
            route[node] = None
        else:
            temp = node
            tempPath = []
            while temp is not None :
                tempPath.insert(0, temp)
                temp = previous[temp]   
            route[node] = tempPath

    return weights, route

graph = {
    'CA':[('WC', 2.47),('EL',2.47),('NC',2.47),('ST',2.47)],
    'IP':[('NC',0.8)],
    'NC':[('IP',0.96),('WC',0.96),('CA',0.96)],
    'WC':[('CA', 1.75),('EL',1.75),('NC',1.75),('ST',1.75)],
    'ST':[('WC', 1.28),('NNP',1.28),('CA',1.28)],
    'NNP':[('ST',1.63)],
    'EL': [('WC',1.01),('CA',1.01)]
}

graphweights={}

notGraph = {nodes:[]for nodes in graph}
for i in graph:
    connected_nodes= []
    for nexto in graph[i]:
        connected_nodes.append(nexto[0])
        #graphweights.append({i:nexto[1]})
        graphweights[i] = nexto[1]

    #connected_nodes = {[nexto for nexto in graph[i][1]]} 
    notGraph['X']=[('Y',0)] #This is used by not adding any new nodes
    for j in graph:
        if j != i and j not in connected_nodes:
            notGraph[i].append((j, graphweights[i]))
        
dataFile = open('/Users/vem0001/desktop/Table1.csv', 'w')

dataFile.write(f"Sequence#cost#with path#with hops#Added connection between \n")

trustedGraphCopy =  copy.deepcopy(graph)

for o in notGraph:
    
        for z in notGraph[o]:
            
            graph =  copy.deepcopy(trustedGraphCopy)

            if o != 'X': #Dont add a new connections
                graph[o].append(z)
                idk = ( o,graphweights[z[0]])
                graph[z[0]].append(idk)

            #dataFile.write(f"Added connection between {o} and {z[0]} \n")

            places = {node: [] for node in graph}
            iterplaces = [node for node in graph]
            for source in graph:
                weights, routes = djikistri(source, graph)
                for target in graph:
                    if target != source and routes[target] is not None:
                        #places[source].append({target: [str(round(weights[target],2)), routes[target]]})#
                        places[source].append({target: [(round(weights[target],2)), routes[target] ]})

                    elif target != source:
                        places[source].append({target: ["inf", []]})
 
            allsequence = list(itertools.permutations(iterplaces))

            for i in allsequence:
                if i[0] != start and start != '':
                    continue
                count = 0
                weight = 0
                route = []
                route_str = ''
                k = 0
                m = 0
                for j in i:
                    m = m + 1    
                    
                    if (count) < (len(i) - 1):
                            to = i[count + 1]
                            currentLoc = places[j]
                            toLoc = next((entry[to] for entry in currentLoc if to in entry), None)
                            
                            if k==0:
                                route.append(i[0])
                            #else:I am so sorry that you failed else block, you served us well.
                            if (len(i) -1) == m: # and to not in route:
                                if to not in copyroute:
                                    route.append(toLoc[1])     
                                    k = k + 1
                                    weight = (toLoc[0]) + weight
                            else:
                                route.append(toLoc[1])     
                                k = k + 1
                                weight = (toLoc[0]) + weight
                            count=count+1
                    copyroute = []
                    copyroute.append(route[0])
                    for i1 in route[1:]:
                        for j in i1:
                            copyroute.append(j)
                
                #below code removes duplicates
                copyroute = [copyroute[0]] + [b for a, b in zip(copyroute, copyroute[1:]) if a != b]

                countNodes = len(copyroute)
                dataFile.write(f"{'--> '.join(i)} # {round(
 
