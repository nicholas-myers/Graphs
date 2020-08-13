# recursive solution
# count = 0
# def earliest_ancestor(ancestors, starting_node):
#     parents = {}
#     children = {}
#     for pc in ancestors:
#         parent = pc[0]
#         child = pc[1]
#         parents[parent] = child
#         children[child] = [parent]
#     for p, c in parents.items():
#         children[c] = children[c] + [p]
#     # print(children)
#     global count
    
#     if starting_node in children:
#         for c, p in children.items():
#             if starting_node == c:
#                 count += 1
#                 print(parent)
#                 return earliest_ancestor(ancestors, min(p))
                
#     else:
#         if count == 0:
#             return -1
#         for p, c in parents.items():
#             if starting_node == p:
#                 print(p)
#                 count = 0
#                 return p
            
from util import Queue
def earliest_ancestor(ancestors, starting_node):
    # check to see if the starting node has any parents
    parents = {}
    children = {}
    for pc in ancestors:
        parent = pc[0]
        child = pc[1]
        parents[parent] = child
        children[child] = [parent]
    print(parents)
    for p, c in parents.items():
        if p not in children[c]:
            children[c] += [p]
    print(children)
    q = Queue()
    q.enqueue(starting_node)
    count = 1
    while q.size() > 0:
        v = q.dequeue()
        if v not in children and count == 1:
            return -1
        if v not in children:
            return v
        print(children[v])
        count += 1
        q.enqueue(min(children[v]))
        
        
    # if it has parents add those to the queue
    # keep checking for parents
    # if no more parents
    # return the lowest value with no parents

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
earliest_ancestor(test_ancestors, 9)