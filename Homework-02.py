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

# Функція для обчислення суми всіх вузлів
def sum_tree(node):
    if node is None:
        return 0
    return node.key + sum_tree(node.left) + sum_tree(node.right)


values = [20, 10, 30, 5, 15, 8, 7]   # список чисел
root = None

# Будуємо дерево зі списку
for v in values:
    root = insert(root, v)

# Обчислюємо суму
total = sum_tree(root)
print("Сума всіх значень у дереві:", total)  
