from convert import mat_to_list

class Testcase:
  def __init__(self, name, input_adj_list, expected_output):
    self.name = name
    self.input_adj_list = input_adj_list
    self.expected_output = expected_output
  
  def run_test(self):
    output = mat_to_list(self.input_adj_list)
    print("running ", self.name)
    print ("Input   :", self.input_adj_list)
    print ("Output  :", output)
    print ("Expected:", self.expected_output)
    if output == self.expected_output:
      print ("✅ PASSED")
      return True
    else:
      print ("❌ FAILED")
      return False

test_suite = []

adj_mat =   [[0, 1, 0, 1, 0, 0],
             [0, 0, 1, 0, 0, 0],
             [1, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 1, 0],
             [0, 0, 0, 1, 0, 0],
             [0, 0, 0, 0, 0, 0]]
adj_list = [[1, 3], [2], [0], [4], [3], []]
test_suite.append(Testcase("Sample graph", adj_mat, adj_list))

adj_mat = []
adj_list = []
test_suite.append(Testcase("Empty graph, no vertices", adj_mat, adj_list))

adj_mat = [[0]]
adj_list = [[]]
test_suite.append(Testcase("Graph with 1 vertice", adj_mat, adj_list))

adj_mat = [[0, 1],
           [0, 0]]
adj_list = [[1],[]]
test_suite.append(Testcase("2 vertices, one direction", adj_mat, adj_list))

adj_mat = [[0, 1],
           [1, 0]]
adj_list = [[1],[0]]
test_suite.append(Testcase("2 vertices, bi-direction", adj_mat, adj_list))

adj_mat = [[0, 1, 0],
           [0, 0, 1],
           [1, 0, 0]]
adj_list = [[1],[2], [0]]
test_suite.append(Testcase("3 vertices, one direction", adj_mat, adj_list))

adj_mat = [[0, 1, 1],
           [1, 0, 1],
           [1, 1, 0]]
adj_list = [[1, 2],[0, 2], [0, 1]]
test_suite.append(Testcase("3 vertices, bi-direction", adj_mat, adj_list))

for testcase in test_suite:
  if testcase.run_test() == False:
    print("🆘 [TEST FAILED] Please fix your bug!")
    break
