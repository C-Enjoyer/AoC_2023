import networkx as nx

path = 'input.txt'

knots = {}

with open(path, 'r') as file:
    for row in file:
        left, right = row.strip().split(': ')
        knots[left] = tuple([r for r in right.split(' ')])


def part1(knots):
    """ part 1 """

    g = nx.Graph()

    for key, values in knots.items():
        for value in values:
             g.add_edge(key, value)

    g.remove_edges_from(nx.minimum_edge_cut(g))
    cc = list(nx.connected_components(g))
    return len(cc[0]) * len(cc[1])

    
def part2(knots):
    """ part 2 """
    
    return "OH YEAH"

print(part1(knots))
print(part2(knots))