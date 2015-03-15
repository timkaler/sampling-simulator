#!/usr/bin/python
import random
import sys

vertices = []
edges = dict()

vertex_id = 0

def checkout_vertex():
  global vertex_id
  vertex_id=vertex_id+1
  vertices.append(vertex_id-1)
  return vertex_id-1

def generate_tree(depth, parent):
  if depth == 0:
    return
  v = checkout_vertex()
  edges[v] = []
  if parent >= 0:
    edges[parent].append(v)

  generate_tree(depth-1, v)
  generate_tree(depth-1, v) 

def generate_tree_parallel_radix(sq_root_n, parent, is_parent=False):
    """
    Construct a dag representative of one for parallel radix sort.
    """
    if sq_root_n == 0:
        return
    v = checkout_vertex()
    edges[v] = []
    if is_parent:
        for i in range(sq_root_n):
            generate_tree_parallel_radix(sq_root_n, v)
    else:
        edges[parent].append(v)
        generate_tree_parallel_radix(sq_root_n - 1, v)
  
sample_array = dict()
def compute_max_path(parent):
  global sample_array
  if len(edges[parent]) == 0:
    if parent in sample_array:
      return 1
    else:
      return 0

  max_path = 0
  for v in edges[parent]:
    vspan = compute_max_path(v)
    if vspan > max_path:
      max_path = vspan

  max_path = max_path
  if v in sample_array:
    return max_path+1
  else:
    return max_path

def sample_dag(vertices, p):
  global sample_array
  sampled = random.sample(vertices, int(p*len(vertices)))
  for x in sampled:
    sample_array[x] = True

def run(p):
    #generate_tree(20, -1)
    generate_tree_parallel_radix(300, -1, True)
    sample_dag(vertices, p)

    work = len(vertices)
    span = compute_max_path(0)*(1/p)
    parallelism = work / span
    print "Work: %d" % work 
    print "Span estimate: %.2f" % span
    print "Parallelism estimate: %.2f" %  parallelism

if __name__ == "__main__":
    p = 0.1
    if len(sys.argv) == 2:
        p = float(sys.argv[1])
    run(p)


