import random
import math
import sys
import time
vertices = []
edges = dict()
sys.setrecursionlimit(100000)

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
stack = list()
in_stack = dict()

def compute_max_path_stack_version(root):
  global stack
  global in_stack
  stack.append(root)
  for v in vertices:
    in_stack[v] = False
  in_stack[root] = True
  while len(stack) > 0:
    parent = stack[-1]
    #print parent
    #time.sleep(0.1)
    ret = compute_max_path_stack(parent)
    if ret != None:
      stack.pop()
      in_stack[parent] = False
    

def compute_max_path_stack(parent):
  global sample_array
  global stack

  if parent in visited_array:
    return visited_array[parent] 

  if len(edges[parent]) == 0:
    c1 = 0
    c2 = 0
    c3 = 0
    c4 = 0
    if parent in sample_array:
      c1 = 1
    if parent in sample_array2:
      c2 = 1
    if parent in sample_array3:
      c3 = 1
    if parent in sample_array4:
      c4 = 1
    visited_array[parent] = (c1,c2,c3,c4)
    return (c1,c2,c3,c4)

  max_path = (0,0,0,0)
  count = 0
  max_value = 0
  for v in edges[parent]:
    if v not in visited_array:
      if not in_stack[v]:
        in_stack[v] = True
        stack.append(v)
        #print "appending " + str(v)
      return None

    vspan = compute_max_path(v)
    visited_array[v] = vspan
    #value = math.pow((vspan[0]+1)*(vspan[1]+1)*(min(vspan[0],vspan[1])+1), 3)
   
    #if vspan[0] < 2:
    #  value = vspan[0]
    #else: 
    #value=max(vspan[0],vspan[1]) - abs(vspan[0]-vspan[1])/2
    value=vspan[0]
    #value = vspan[0]
    #if vspan[0] > max_path[0]:
    if value > max_value:
      max_path = vspan
      max_value=value

  # (two) now four choices approach.
  if max_path[0] > (max_path[1]+1):
    max_path=(max_path[1],max_path[0], max_path[2], max_path[3])
  if max_path[0] > (max_path[2]+1):
    max_path=(max_path[2],max_path[1], max_path[0], max_path[3])
  if max_path[0] > (max_path[3]+1):
    max_path=(max_path[3],max_path[1], max_path[2], max_path[0])

  c1 = 0
  c2 = 0
  c3 = 0
  c4 = 0
  if parent in sample_array:
    c1 = 1
  if parent in sample_array2:
    c2 = 1
  if parent in sample_array3:
    c3 = 1
  if parent in sample_array4:
    c4 = 1 
  visited_array[parent] = (max_path[0]+c1, max_path[1]+c2, max_path[2] + c3, max_path[3] + c4)
  return (max_path[0]+c1, max_path[1]+c2, max_path[2] + c3, max_path[3] + c4)

def compute_max_path(parent):
  global sample_array
  global visited_array
  if parent in visited_array:
    return visited_array[parent] 

  print "danger danger!"

  if len(edges[parent]) == 0:
    c1 = 0
    c2 = 0
    c3 = 0
    c4 = 0
    if parent in sample_array:
      c1 = 1
    if parent in sample_array2:
      c2 = 1
    if parent in sample_array3:
      c3 = 1
    if parent in sample_array4:
      c4 = 1
    visited_array[parent] = (c1,c2,c3,c4) 
    return (c1,c2,c3,c4)

  max_path = (0,0,0,0)
  count = 0
  max_value = 0
  for v in edges[parent]:
    vspan = compute_max_path(v)
    visited_array[v] = vspan
    #value = math.pow((vspan[0]+1)*(vspan[1]+1)*(min(vspan[0],vspan[1])+1), 3)
   
    #if vspan[0] < 2:
    #  value = vspan[0]
    #else: 
    #value=max(vspan[0],vspan[1]) - abs(vspan[0]-vspan[1])/2
    value=vspan[0]
    #value = vspan[0]
    #if vspan[0] > max_path[0]:
    if value > max_value:
      max_path = vspan
      max_value=value

  # (two) now four choices approach.
  if max_path[0] > (max_path[1]+1):
    max_path=(max_path[1],max_path[0], max_path[2], max_path[3])
  if max_path[0] > (max_path[2]+1):
    max_path=(max_path[2],max_path[1], max_path[0], max_path[3])
  if max_path[0] > (max_path[3]+1):
    max_path=(max_path[3],max_path[1], max_path[2], max_path[0])

  c1 = 0
  c2 = 0
  c3 = 0
  c4 = 0
  if parent in sample_array:
    c1 = 1
  if parent in sample_array2:
    c2 = 1
  if parent in sample_array3:
    c3 = 1
  if parent in sample_array4:
    c4 = 1
  visited_array[parent] = (max_path[0]+c1, max_path[1]+c2, max_path[2] + c3, max_path[3] + c4)
  return (max_path[0]+c1, max_path[1]+c2, max_path[2] + c3, max_path[3] + c4)

sample_array2 = dict()
sample_array3 = dict()
sample_array4 = dict()

def sample_dag(vertices, p):
  global sample_array
  global sample_array2
  global sample_array3
  global sample_array4

  sampled = random.sample(vertices, int(p*len(vertices)))
  for x in sampled:
    sample_array[x] = True

  sampled = random.sample(vertices, int(p*len(vertices)))
  for x in sampled:
    sample_array2[x] = True

  sampled = random.sample(vertices, int(p*len(vertices)))
  for x in sampled:
    sample_array3[x] = True

  sampled = random.sample(vertices, int(p*len(vertices)))
  for x in sampled:
    sample_array4[x] = True



def generate_challenge(k, n):

  root = checkout_vertex()

  final = checkout_vertex()
  right=generate_charles_example_new(k,n, final)
   
  chain_start = checkout_vertex()

  edges[root].append(chain_start)
  edges[root].append(right)

  chain_head = chain_start

  for i in range(0,k*(2**n)):
    vertex = checkout_vertex()
    edges[chain_head].append(vertex)
    chain_head = vertex
  edges[chain_head].append(final)

  return root

def generate_charles_example_new(k, n, succ):
  parent = checkout_vertex()
  orig_parent = parent
  while k > 0:
    v = checkout_vertex()
    edges[parent].append(v)

    parent = generate_binary_tree_closed(n, v)
    #parent = checkout_vertex()
    #edges[u].append(parent)
    k = k-1
  # append the successor
  edges[parent].append(succ) 
  return orig_parent


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

in_edges = dict()
def deduplicate_edges(vertices):
  global edges
  global in_edges
  new_edges = dict()
  for v in vertices:
    new_edges[v] = []
  for v in vertices:
    D = dict()
    for e in edges[v]:
      if e not in D:
        new_edges[v].append(e)
      D[e] = True
  edges = new_edges
  for v in vertices:
    in_edges[v] = 0

  for v in vertices:
    for e in edges[v]:
      in_edges[e] += 1
       
def compute_pedigrees(pmap, parent, pedigree, real_parent):
  if parent in visited_array:
    return
  if in_edges[parent] > 1:
    in_edges[parent] -= 3
    return

  # this is a join edge
  if in_edges[parent] == -1:
    #print "reduced length before " + str(pedigree)
    #pmap[parent] = tuple(pedigree[:len(pedigree)-1])
    pmap[parent] = tuple(pedigree[:len(pedigree)])
    pmap[parent] = list(pmap[parent])
    pmap[parent][len(pmap[parent])-1] = 3
    pmap[parent] = pmap[parent] + [0]
    pmap[parent] = tuple(pmap[parent]) 
    #print "reduced length after " + str(pmap[parent])
  else: 
    pmap[parent] = tuple(pedigree)

  visited_array[parent] = True
  index = 0 
  if len(edges[parent]) > 1:
    for v in edges[parent]:
      compute_pedigrees(pmap, v, list(pmap[parent]) + [index], parent)
      index += 1
  else:
    for v in edges[parent]:
      compute_pedigrees(pmap, v, list(pmap[parent]), parent)
  

#root = generate_charles_example(3000,6)

root = generate_challenge(6000,6)
#root = generate_challenge(1,2)

#p = 1.0/(2**12)
p = 400.0/len(vertices)
#p=1.0
#print p*len(vertices)
#p = 1.0/16
p = 1.0 

def sample(pmap, vertices):
  v1 = random.randint(0,len(vertices)-1)
  v2 = random.randint(0,len(vertices)-1)
  if v1 == v2:
    return sample(pmap,vertices)
  #print str((v1,v2)) 
  #print pmap[v1]
  #print pmap[v2]
  min_length = min(len(pmap[v1]), len(pmap[v2]))

  # count outstanding spawns.
  outstanding_spawns = 0
  for i in range(0,min_length):
    if pmap[v1][i] != pmap[v2][i] and pmap[v1][i] != 3 and pmap[v2][i] != 3:
      outstanding_spawns += 1

  # now count outstanding syncs.
  larger_p = None
  if len(pmap[v1]) == min_length:
    larger_p = pmap[v2]
  else:
    larger_p = pmap[v1]
  for i in range(min_length,len(larger_p)):
    if larger_p[i] == 3:
      outstanding_spawns -= 1
    if outstanding_spawns <= 0:
      #print "serial"
      return 0
  #print "parallel"
  return 1
 

        
delta = 1/math.sqrt(p)

print "delta is " + str(1/math.sqrt(p))

sample_dag(vertices, p)


#print len(vertices)
#print edges

deduplicate_edges(vertices)
compute_max_path_stack_version(root)
span = visited_array[root] 

print "the span is " + str(span)
print "the corrected span is " + str((span[0]*(1/p), span[1]*(1/p)))
print str(len(vertices) / (span[1]*(1/p)))
#exit()
#exit()
pmap = dict()

#compute_pedigrees(pmap, root, [0], root)

#sample(pmap, vertices)


#print edges
#print pmap
#exit()
#count = 1
#total = 5000
#for i in range(0,total):
#  count+=sample(pmap, vertices)

#fraction= total/(1.0*(total-count))
#probability_in_parallel = (1.0)*(total-count) / total
#print fraction
#print str(1/probability_in_parallel)
#print str( len(vertices)*probability_in_parallel)
#print count

#print total
#print "the span is " + str(span[0] * (1/p)) +" and other is " + str(span[1] * (1/p))

#print str(len(vertices)/span[0])

