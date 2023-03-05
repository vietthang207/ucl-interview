from reachable import reachable

class Testcase:
  def __init__(self, name, input_adj_list, input_start_node, expected_output):
    self.name = name
    self.input_adj_list = input_adj_list
    self.input_start_node = input_start_node
    self.expected_output = expected_output
  
  def run_test(self):
    output = reachable(self.input_adj_list, self.input_start_node)
    print("running ", self.name)
    print ("Input graph     :", self.input_adj_list)
    print ("Input start_node:", self.input_start_node)
    print ("Output          :", output)
    print ("Expected        :", self.expected_output)
    if output == self.expected_output:
      print ("✅ PASSED")
      return True
    else:
      print ("❌ FAILED")
      return False

test_suite = []


adj_list = [[1, 3], [2], [0], [4], [3], []]
start_node = 0
reachable_nodes = {0, 1, 2, 3, 4}
test_suite.append(Testcase("Sample graph, start node 0", adj_list, start_node, reachable_nodes))
start_node = 1
reachable_nodes = {0, 1, 2, 3, 4}
test_suite.append(Testcase("Sample graph, start node 1", adj_list, start_node, reachable_nodes))
start_node = 2
reachable_nodes = {0, 1, 2, 3, 4}
test_suite.append(Testcase("Sample graph, start node 2", adj_list, start_node, reachable_nodes))
start_node = 3
reachable_nodes = {3, 4}
test_suite.append(Testcase("Sample graph, start node 3", adj_list, start_node, reachable_nodes))
start_node = 4
reachable_nodes = {3, 4}
test_suite.append(Testcase("Sample graph, start node 4", adj_list, start_node, reachable_nodes))
start_node = 5
reachable_nodes = {5}
test_suite.append(Testcase("Sample graph, start node 5", adj_list, start_node, reachable_nodes))


adj_list = [[]]
start_node = 0
reachable_nodes = {0}
test_suite.append(Testcase("Graph with only 1 vertice", adj_list, start_node, reachable_nodes))

adj_list = [[],[]]
start_node = 0
reachable_nodes = {0}
test_suite.append(Testcase("2 vertices, unconnected, start 0", adj_list, start_node, reachable_nodes))
start_node = 1
reachable_nodes = {1}
test_suite.append(Testcase("2 vertices, unconnected, start 1", adj_list, start_node, reachable_nodes))

adj_list = [[1],[]]
start_node = 0
reachable_nodes = {0, 1}
test_suite.append(Testcase("2 vertices, one direction, start 0", adj_list, start_node, reachable_nodes))
start_node = 1
reachable_nodes = {1}
test_suite.append(Testcase("2 vertices, one direction, start 1", adj_list, start_node, reachable_nodes))

adj_list = [[1],[0]]
start_node = 0
reachable_nodes = {0, 1}
test_suite.append(Testcase("2 vertices, bidirectional, start 0", adj_list, start_node, reachable_nodes))
start_node = 1
reachable_nodes = {0, 1}
test_suite.append(Testcase("2 vertices, bidirectional, start 1", adj_list, start_node, reachable_nodes))

adj_list = [[1],[2],[0]]
start_node = 1
reachable_nodes = {0, 1, 2}
test_suite.append(Testcase("3 vertices, one direction cycle", adj_list, start_node, reachable_nodes))

adj_list = [[1, 2],[0, 2], [0, 1]]
start_node = 2
reachable_nodes = {0, 1, 2}
test_suite.append(Testcase("3 vertices, bidirectional", adj_list, start_node, reachable_nodes))

for testcase in test_suite:
  if testcase.run_test() == False:
    print("🆘 [TEST SUITE FAILED] Please fix your bug!")
    break
