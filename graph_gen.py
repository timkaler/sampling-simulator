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
  edges[vertex_id-1] = []
  return vertex_id-1


def generate_chain(n, parent):
  if n == 0:
    return
  v = checkout_vertex()
  edges[v] = []
  edges[parent].append(v)
  generate_chain(n-1,v)

did_long_one = False

def generate_binary_tree_closed(depth, parent):
  if depth == 0:
    if parent == None:
      print "WHAT!?"
    return parent
  v = checkout_vertex()
  edges[v] = []
  if parent >= 0:
    edges[parent].append(v)

  left = generate_binary_tree_closed(depth-1, v)
  right = generate_binary_tree_closed(depth-1, v)
  w = checkout_vertex()
  edges[left].append(w)
  edges[right].append(w)
  return w

def generate_tree(depth, parent):
  if depth == 0:
    if not did_long_one:
      did_lone_one = True
      generate_chain(600, parent)
      return
    generate_chain(100, parent)
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
visited_array = dict()
def compute_max_path(parent):
  global sample_array

  if parent in visited_array:
    return visited_array[parent] 

  if len(edges[parent]) == 0:
    if parent in sample_array:
      if parent in sample_array2:
        return (1,1)
      else:
        return (1,0)
    else:
      if parent in sample_array2:
        return (0,1)
      else:
        return (0,0)

<<<<<<< HEAD
  max_path = (0,0)
  count = 0
=======
  max_path = 0
>>>>>>> a6f64b63a6b18453058cbc8b08faf84995e9822c
  for v in edges[parent]:
    vspan = compute_max_path(v)
    visited_array[v] = vspan
    if vspan[0] > max_path[0]:
      max_path = vspan

  if v in sample_array:
    if v in sample_array2:
      return (max_path[0]+1, max_path[1]+1)
    else:
      return (max_path[0]+1, max_path[1])
  else:
    if v in sample_array2:
      return (max_path[0], max_path[1]+1)
    else:
      return max_path 

<<<<<<< HEAD

sample_array2 = dict()

=======
>>>>>>> a6f64b63a6b18453058cbc8b08faf84995e9822c
def sample_dag(vertices, p):
  global sample_array
  global sample_array2

  sampled = random.sample(vertices, int(p*len(vertices)))
  for x in sampled:
    sample_array[x] = True

<<<<<<< HEAD
  sampled = random.sample(vertices, int(p*len(vertices)))
  for x in sampled:
    sample_array2[x] = True


def generate_charles_example(k, n):
  parent = checkout_vertex()
  orig_parent = parent
  while k > 0:
    v = checkout_vertex()
    edges[parent].append(v)

    parent = generate_binary_tree_closed(n, v)
    #parent = checkout_vertex()
    #edges[u].append(parent)
    k = k-1 
  return orig_parent


#generate_tree(15, -1)

root = generate_charles_example(50,8)

p = 0.016
#p = 1 

        
delta = 1/math.sqrt(p)

print "delta is " + str(1/math.sqrt(p))

sample_dag(vertices, p)


print len(vertices)
#print edges

span = compute_max_path(root)

print "the span is " + str(span[0] * (1/p)) +" and other is " + str(span[1] * (1/p))

print str(len(vertices)*p/span[1])
=======
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

>>>>>>> a6f64b63a6b18453058cbc8b08faf84995e9822c

