import unittest
from graph import Vertex, Edge, Graph


class TestGraphADT(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()
        self.v1 = self.graph.add_vertex("A")
        self.v2 = self.graph.add_vertex("B")
        self.v3 = self.graph.add_vertex("C")
        self.v4 = self.graph.add_vertex("D")
        self.edge1 = self.graph.add_edge(self.v1, self.v2, 1)
        self.edge2 = self.graph.add_edge(self.v2, self.v3, 2)
        self.edge3 = self.graph.add_edge(self.v3, self.v4, 3)

    def test_vertex_creation(self):
        v = Vertex("X")
        self.assertEqual(v.element(), "X")

    def test_edge_creation(self):
        e = Edge(self.v1, self.v2, 5)
        self.assertEqual(e.start(), self.v1)
        self.assertEqual(e.end(), self.v2)
        self.assertEqual(e.element(), 5)

    def test_add_vertex(self):
        v = self.graph.add_vertex("E")
        self.assertIn(v, self.graph.vertices())

    def test_add_duplicate_vertex(self):
        v1 = self.graph.add_vertex_if_new("B")
        v2 = self.graph.add_vertex_if_new("B")
        self.assertEqual(v1, v2)
        self.assertEqual(self.graph.num_vertices(), 4)  # Should not increase

    def test_add_edge(self):
        e = self.graph.add_edge(self.v1, self.v3, 4)
        self.assertIn(e, self.graph.edges())

    def test_get_edge(self):
        self.assertEqual(self.graph.get_edge(self.v1, self.v2), self.edge1)
        self.assertEqual(self.graph.get_edge(self.v2, self.v3), self.edge2)
        self.assertIsNone(self.graph.get_edge(self.v1, self.v4))

    def test_get_vertex_by_label(self):
        self.assertEqual(self.graph.get_vertex_by_label("A"), self.v1)
        self.assertEqual(self.graph.get_vertex_by_label("C"), self.v3)
        self.assertIsNone(self.graph.get_vertex_by_label("Z"))

    def test_get_edges_for_vertex(self):
        edges = self.graph.get_edges(self.v2)
        self.assertEqual(len(edges), 2)
        self.assertIn(self.edge1, edges)
        self.assertIn(self.edge2, edges)

    def test_num_vertices(self):
        self.assertEqual(self.graph.num_vertices(), 4)

    def test_num_edges(self):
        self.assertEqual(self.graph.num_edges(), 3)

    def test_degree(self):
        self.assertEqual(self.graph.degree(self.v1), 1)
        self.assertEqual(self.graph.degree(self.v2), 2)
        self.assertEqual(self.graph.degree(self.v3), 2)
        self.assertEqual(self.graph.degree(self.v4), 1)

    def test_highest_degree_vertex(self):
        self.assertEqual(self.graph.highestdegreevertex(), self.v2)

    def test_remove_vertex(self):
        self.graph.remove_vertex(self.v3)

        print("Vertices after removal:", self.graph.vertices())
        print("Edges after removal:", self.graph.edges())

        self.assertNotIn(self.v3, self.graph.vertices())  # Ensure vertex is gone
        self.assertNotIn(self.v3,
                         [v for e in self.graph.edges() for v in e.vertices()])  # Ensure it's not part of any edge

        print("get_edge(v2, v3):", self.graph.get_edge(self.v2, self.v3))
        print("get_edge(v3, v4):", self.graph.get_edge(self.v3, self.v4))

        self.assertIsNone(self.graph.get_edge(self.v2, self.v3))  # Ensure edge is removed
        self.assertIsNone(self.graph.get_edge(self.v3, self.v4))  # Ensure all edges to v3 are gone

    def test_remove_edge(self):
        self.graph.remove_edge(self.v2, self.v3)
        self.assertIsNone(self.graph.get_edge(self.v2, self.v3))


if __name__ == "__main__":
    unittest.main()