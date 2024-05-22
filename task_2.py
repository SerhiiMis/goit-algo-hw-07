class AVLTreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.height = 1

def insert_avl(root, key):
    if not root:
        return AVLTreeNode(key)
    elif key < root.val:
        root.left = insert_avl(root.left, key)
    else:
        root.right = insert_avl(root.right, key)

    root.height = 1 + max(get_height(root.left), get_height(root.right))

    balance = get_balance(root)

    if balance > 1 and key < root.left.val:
        return right_rotate(root)
    if balance < -1 and key > root.right.val:
        return left_rotate(root)
    if balance > 1 and key > root.left.val:
        root.left = left_rotate(root.left)
        return right_rotate(root)
    if balance < -1 and key < root.right.val:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root

def left_rotate(z):
    y = z.right
    T2 = y.left
    y.left = z
    z.right = T2
    z.height = 1 + max(get_height(z.left), get_height(z.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))
    return y

def right_rotate(z):
    y = z.left
    T3 = y.right
    y.right = z
    z.left = T3
    z.height = 1 + max(get_height(z.left), get_height(z.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))
    return y

def get_height(root):
    if not root:
        return 0
    return root.height

def get_balance(root):
    if not root:
        return 0
    return get_height(root.left) - get_height(root.right)

def find_min_avl(root):
    current = root
    while current.left is not None:
        current = current.left
    return current.val

# Приклад використання
root = None
keys = [50, 30, 20, 40, 70, 60, 80]

for key in keys:
    root = insert_avl(root, key)

print("Найменше значення в AVL:", find_min_avl(root))
