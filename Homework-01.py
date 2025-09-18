# Клас вузла дерева
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Вставка елемента у BST
def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

# Пошук мінімального значення
def find_min(node):
    if node is None:
        return None
    while node.left:
        node = node.left
    return node.key

# --- Приклад використання ---
values = [20, 10, 30, 5, 15, 7, 8, 4, 56, 15 ,100, 8, 16]   # довільний список
root = None
for v in values:
    root = insert(root, v)     # будуємо BST

print("Мінімальне значення:", find_min(root))  # 5
