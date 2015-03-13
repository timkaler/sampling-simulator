import random
import math
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
  
sample_array = dict()
def compute_max_path(parent):
  global sample_array
  if len(edges[parent]) == 0:
    if parent in sample_array:
      return 1
    else:
      return 0

  max_path = 0
  count = 0
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

generate_tree(20, -1)

p = 0.1

sample_dag(vertices, p)


#print vertices
#print edges

print compute_max_path(0)*(1/p)

print len(vertices)*p/compute_max_path(0)

