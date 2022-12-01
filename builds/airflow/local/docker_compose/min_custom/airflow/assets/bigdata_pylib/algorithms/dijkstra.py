

import sys
import numpy as np

"""
maintained by: Christopher R Harty (ascii1011@gmail.com)
hand rolled from dijstra requirements

Currently this is a linear process... but perhaps it could be broken up into separate processes for building each row of the resulting truth table.
and then the target path (i.e. shortest as 1 option) by following the relavant references
"""


__all__ = ["dijk_spla"]




def dijk_spla(edges, debug=False):
    """shortest_path_linear_approach"""

    if debug: print('\n\n----------  ## Dijkstra Sortest Path ##  ----------------')
    vertices = sorted(edges.keys())
    dist, prev = init(vertices)
    unvisited = vertices[:]
    visited = []
    v_count = len(vertices)
    
    cur = unvisited.pop(0)
    #print(f'\nInitially visiting: {cur}')
    if debug: o(dist, prev, vertices)

    #while is_uncomplete(visited, vertices):
    while len(visited) != len(vertices):
        if debug: 
            print('\n\n_______________________________')
            print(f'visiting: {cur}')

        if cur not in visited:

            min_d = 0
            min_v = None

            # neighbors
            if debug: print(f'neighbors: {edges[cur]}')
            for edge, weight in edges[cur]:
                if edge not in visited:

                    current_calculated_distance = dist[cur] + weight
                    
                    if dist[edge] > current_calculated_distance:
                        if debug: print(f'\tneighbor: {edge}(weight:{weight}) [{dist[edge]} > {dist[cur]} + {weight}] !!UPDATED')
                        dist[edge] = current_calculated_distance
                        prev[edge] = cur
                    else:
                        if debug: print(f'\tneighbor: {edge}(weight:{weight}) [{dist[edge]} > {dist[cur]} + {weight}] !!NOT UPDATED')

                    # track which cur neighbor is the shortest for the next visit
                    # so we don't need to cycle through results again
                    if min_v == None:
                        #print(f'\tmin_vertex is None, so "{edge}" is the shortest')
                        min_d = dist[edge]
                        min_v = edge
                    elif dist[edge] < min_d:
                        #print(f'\tupdated as shortest because dist[edge]:{dist[edge]} is < min_d:{min_d}')
                        min_d = dist[edge]
                        min_v = edge

                    #print(f'\tedge: {edge} ({dist[edge]}) [min {min_d}:{min_v}]')
                else:
                    if debug: print(f'\tedge: {edge} already visited...')
                    pass

            visited.append(cur)
            
            if debug:
                o(dist, prev, vertices)
                print(f'Visited: {visited}, Unvisited: {unvisited}')
            
            if min_v == None:
                if debug: print('min_d == None')
                # This means there are no neighbors to visit.
                #  if there were no new neighbors to visit, check unvisited
                
                if len(unvisited) > 0:
                    cur = unvisited.pop()

                else:
                    # is unvisited is empty then break
                    pass

            else:
                print(f'\tshortest neighbor "{min_v}"')
                cur = unvisited.pop(unvisited.index(min_v)) if min_v in unvisited else 'unvisited OOR err'
                print(f'\tgrabbing "{min_v}" from unvisited, cur is not "{cur}"')
                
            v_count -= 1
            #print(f'cur(min_v): {cur}')

    res = []
    #print('\n Vert | Dist | Prev')
    for v in vertices:
        res.append((v, dist[v], prev[v]))
        #print(f' {v}    | {dist[v]}    | {prev[v]}')

    if debug: print('\n\n___________ end ______________\n\n')
    return res


def init(_vertices):
    """preprocess of DS"""
    distance = {}
    previous = {}
    for v in _vertices:

        if not distance:
            distance[v] = 0
        else:
            distance[v] = np.inf

        previous[v] = ""

    return distance, previous


def is_uncomplete(_visited, _vertices):
    return len(_visited) != len(_vertices)
    

def dsp(vertices, edges):

    print('\n\n----------  ## Dijkstra Sortest Path ##  ----------------')
    dist, prev = init(vertices)
    unvisited = vertices[:]
    visited = []
    v_count = len(vertices)
    
    cur = unvisited.pop(0)
    #print(f'\nInitially visiting: {cur}')
    o(dist, prev, vertices)

    #while is_uncomplete(visited, vertices):
    while len(visited) != len(vertices):
        print('\n\n_______________________________')
        print(f'visiting: {cur}')

        if cur not in visited:

            min_d = 0
            min_v = None

            # neighbors
            print(f'neighbors: {edges[cur]}')
            for edge, weight in edges[cur]:
                if edge not in visited:

                    current_calculated_distance = dist[cur] + weight
                    
                    if dist[edge] > current_calculated_distance:
                        print(f'\tneighbor: {edge}(weight:{weight}) [{dist[edge]} > {dist[cur]} + {weight}] !!UPDATED')
                        dist[edge] = current_calculated_distance
                        prev[edge] = cur
                    else:
                        print(f'\tneighbor: {edge}(weight:{weight}) [{dist[edge]} > {dist[cur]} + {weight}] !!NOT UPDATED')

                    # track which cur neighbor is the shortest for the next visit
                    # so we don't need to cycle through results again
                    if min_v == None:
                        #print(f'\tmin_vertex is None, so "{edge}" is the shortest')
                        min_d = dist[edge]
                        min_v = edge
                    elif dist[edge] < min_d:
                        #print(f'\tupdated as shortest because dist[edge]:{dist[edge]} is < min_d:{min_d}')
                        min_d = dist[edge]
                        min_v = edge

                    #print(f'\tedge: {edge} ({dist[edge]}) [min {min_d}:{min_v}]')
                else:
                    print(f'\tedge: {edge} already visited...')
                    pass

            visited.append(cur)
            
            o(dist, prev, vertices)
            print(f'Visited: {visited}, Unvisited: {unvisited}')
            
            if min_v == None:
                print('min_d == None')
                # This means there are no neighbors to visit.
                #  if there were no new neighbors to visit, check unvisited
                
                if len(unvisited) > 0:
                    cur = unvisited.pop()

                else:
                    # is unvisited is empty then break
                    pass

            else:
                print(f'\tshortest neighbor "{min_v}"')
                cur = unvisited.pop(unvisited.index(min_v)) if min_v in unvisited else 'unvisited OOR err'
                print(f'\tgrabbing "{min_v}" from unvisited, cur is not "{cur}"')
                
            v_count -= 1
            #print(f'cur(min_v): {cur}')


    print('\n\n___________ end ______________\n\n')


def o(dist, prev, vertices):
    print('\n Vert | Dist | Prev')
    for v in vertices:
        print(f' {v}    | {dist[v]}    | {prev[v]}')

    


def main():
    
    vertices = ['A', 'B', 'C', 'D', 'E']
    edges = {
        'A': [('B', 6), ('D', 1)],
        'B': [('A', 6), ('C', 5), ('D', 2), ('E', 2)],
        'C': [('B', 5), ('E', 5)],
        'D': [('A', 1), ('B', 2), ('E', 1)],
        'E': [('B', 2), ('C', 5), ('D', 1)],
    }

    dsp(vertices, edges)


if __name__ == "__main__":
    main()