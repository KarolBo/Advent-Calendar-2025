from math import sqrt

class Node:
    def __init__(self, x, y, z):
        self.x = int(x)
        self.y = int(y)
        self.z = int(z)
        self.parent = self
        self.cardinality = 1

    @property
    def head(self):
        cur = self
        while cur.parent != cur:
            cur = cur.parent
        return cur
    
    def __str__(self):
        return f'{self.x} {self.y} {self.z}'

def solution(nodes: list[Node], limit=None):
    # Calculate distances
    distances = []
    for i, n in enumerate(nodes[:-1]):
        for m in nodes[i+1:]:
            distances.append((distance(n, m), n, m))
    distances.sort(key=lambda d: d[0])

    # Join into circuits 
    circuits = []
    if limit:
        distances = distances[:limit]
    last_joined = (None, None)
    for _, n, m in distances:
        n_head = n.head
        m_head = m.head
        if n_head is m_head: 
            continue
        circuits.append(join(n_head, m_head))
        last_joined = (n, m)
    
    # Calculate the solution
    circuits = list(set(circuits))
    circuits.sort(key=lambda n: n.cardinality, reverse=True)   
    solution = 1
    for circ in circuits[:3]:
        solution *= circ.cardinality
    return solution, last_joined[0].x * last_joined[1].x

# Commons
def load_input(path: str) -> list[Node]:
    with open(path) as f:
        data = f.readlines()
    nodes = []
    for line in data:
        line = line.strip().replace('\n', '')
        nodes.append(Node(*line.split(',')))
    return nodes

def distance(n: Node, m: Node) -> float:
    dist = sqrt((n.x-m.x)**2 + (n.y-m.y)**2 + (n.z-m.z)**2)
    return dist

def join(n: Node, m: Node):
    m.parent = n
    n.cardinality += m.cardinality
    m.cardinality = 0
    return n

# Main
if __name__ == '__main__':
    nodes = load_input('input.txt')
    # for node in nodes:
    #     print(node)
    # result, _ = solution(nodes, 1000)
    _, result = solution(nodes)
    print(f'Solution: {result}')