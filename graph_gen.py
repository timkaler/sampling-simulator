import random
import math
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

  max_path = (0,0)
  count = 0
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


sample_array2 = dict()

def sample_dag(vertices, p):
  global sample_array
  global sample_array2

  sampled = random.sample(vertices, int(p*len(vertices)))
  for x in sampled:
    sample_array[x] = True

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

