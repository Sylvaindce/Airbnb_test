def isPresent (root, val):
    node_val = [root.value]
    if root.left:
        node_val.append(root.left.value)
    if root.right:
        node_val.append(root.right.value)
    if val in node_val:
        return 1

    if root.left and val < root.value:
        return isPresent(root.left, val)
    elif root.right:
        return isPresent(root.right, val)
    return 0