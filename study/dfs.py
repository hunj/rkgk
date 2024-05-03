"""
Given a tree structure that looks like:

1
 \
  2
 /
3

print out its in-order traversal

Input:
    root = [1, None, 2, 3]
Output:
    [1, 3, 2]
"""

sample_input = [1, None, 2, 3]


class Node:
    def __init__(self, key, left=None, right=None):
        self.left = None
        self.right = None
        self.val = key


sample_root = Node(1)
sample_root.right = Node(2)
sample_root.right.left = Node(3)


# https://stackoverflow.com/a/62856494
def print_tree(trav_node: Node, depth=0):
    if trav_node is not None:
        # right root left, look at the screen turned 90deg clockwise
        print_tree(trav_node.right, depth + 1)
        print(' ' * 2 * depth + '-> ' + str(trav_node.val))
        print_tree(trav_node.left, depth + 1)


# need to construct a tree from input
def deserialize(input_list):
    def dfs(nodes):
        if not nodes:
            return
        curr_value = nodes.pop()
        cur = Node(curr_value)
        cur.left = dfs(nodes)
        cur.right = dfs(nodes)
        return cur

    return dfs(input_list)


def serialize(root_node):
    res = []

    def dfs(node):
        if not node:
            return

        # in-order: left, current, right
        dfs(node.left)
        res.append(node.val)
        dfs(node.right)

    dfs(root_node)

    return res


# in-order traversal: left-root-right

tree = deserialize(sample_input)
print_tree(sample_root)

serialized = serialize(tree)
print(serialized)
