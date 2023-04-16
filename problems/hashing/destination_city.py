"""You are given the array paths, where paths[i] = [cityAi, cityBi] means there
exists a direct path going from cityAi to cityBi. Return the destination city,
that is, the city without any path outgoing to another city.

It is guaranteed that the graph of paths forms a line without any loop,
therefore, there will be exactly one destination city."""


def find_destination_city(paths: list[list[str]]) -> str:
    origins = set()
    destinations = set()

    for o, d in paths:
        origins.add(o)
        destinations.add(d)

    for origin in origins:
        if origin in destinations:
            destinations.remove(origin)

    return destinations.pop()
