"""
Simple graph implementation compatible with BokehGraph class.
"""
class Vertex:
    def __init__(self, label, component=-1):
        self.label = str(label)
        self.component = component

    def __repr__(self):
        return 'Vertex: ' + self.label

    """Trying to make this Graph class work..."""
class Graph:
    def __init__(self):
        self.vertices = {}
        self.components = 0

    def add_vertex(self, vertex, edges=()):
        self.vertices[vertex] = set(edges)

    def add_edge(self, start, end, bidirectional=True):
        if start not in self.vertices or end not in self.vertices:
            raise Exception('Error - vertices not in graph!')
        self.vertices[start].add(end)
        if bidirectional:
            self.vertices[end].add(start)

    def dfs(self, start, target=None):
        stack = []
        stack.append(start)
        visited = set(stack)

        while stack:
            current = stack.pop()
            if current == target:
                break
            visited.add(current)
            stack.extend(self.vertices[current] - visited)

        return visited

    def graph_rec(self, start, target=None):
        x = set()
        x.add(start)
        for v in self.vertices[start]:
            self.graph_rec(v)
        return x

    def find_components(self):
        visited = set()
        current_component = 0

        for vertex in self.vertices:
            if vertex not in visited:
                reachable = self.dfs(vertex)
                for other_vertex in reachable:
                    other_vertex.component = current_component
                current_component += 1
                visited.update(reachable)
        self.components = current_component

def main():
    graph = Graph()
    graph.add_vertex('0')
    graph.add_vertex('1')
    graph.add_vertex('2')
    graph.add_vertex('3')
    graph.add_edge('0', '1')
    graph.add_edge('0', '3')
    print(graph.vertices)
    print(graph.find_components)
    print(graph.graph_rec)

if __name__ == "__main__":
    main()