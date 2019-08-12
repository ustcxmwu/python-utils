


def get_graph():
    graph = dict()
    graph["start"] = {}
    graph["start"]["a"] = 6
    graph["start"]["b"] = 2
    graph["a"] = {}
    graph["a"]["fin"] = 1
    graph["b"] = {}
    graph["b"]["a"] = 3
    graph["b"]["fin"] = 5
    graph["fin"] = {}
    return graph


def get_cost():
    infinity = float("inf")
    costs = dict()
    costs["a"] = 6
    costs["b"] = 2
    costs["fin"] = infinity
    return costs


def get_parent():
    parents = dict()
    parents["a"] = "start"
    parents["b"] = "start"
    parents["fin"] = None
    return parents


def dijkstra():
    graph = get_graph()
    costs = get_cost()
    parent = get_parent()
    processed = []

    node = find_lowest_cost_node(costs, processed)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for key in neighbors.keys():
            new_cost = cost + neighbors[key]
            if costs[key] > new_cost:
                costs[key] = new_cost
                parent[key] = node
        processed.append(node)
        node = find_lowest_cost_node(costs, processed)
    print(parent)


def find_lowest_cost_node(costs, processed):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


if __name__ == '__main__':
    # dijkstra()
    a = zip(range(5), [[x] for x in range(5)])
    print(dict(a))
    b = zip(range(5), [x for x in range(5)])
    print(dict(b))