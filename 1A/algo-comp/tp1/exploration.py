locations = {
    "plaine" : {
        "linked": ["chateau", "forêt"]
    },
    "chateau": {
        "linked": ["plaine", "tour"]
    },
    "tour": {
        "linked": ["chateau", "cimetière"]
    },
    "cimetière": {
        "linked": ["tour", "village", "marais"]
    },
    "marais": {
        "linked": ["cimetière", "prairie"]
    },
    "prairie": {
        "linked": ["marais", "forêt"]
    },
    "forêt": {
        "linked": ["prairie", "plaine"]
    },
    "village": {
        "linked": ["forêt", "cimetière"]
    },
}


def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph.keys():
        return None
    for node in graph[start]["linked"]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath: return newpath
    return None


def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph.keys():
        return []
    paths = []
    for node in graph[start]["linked"]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

print(find_all_paths(locations, "plaine", "marais"))