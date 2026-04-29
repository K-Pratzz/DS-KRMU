# -------- NODE CLASS --------
class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# -------- INSERT --------
def insert(root, key):
    # If tree is empty
    if root is None:
        return BSTNode(key)
    # Go left
    if key < root.key:
        root.left = insert(root.left, key)

    # Go right
    elif key > root.key:
        root.right = insert(root.right, key)
    return root


# -------- SEARCH --------
def search(root, key):
    if root is None:
        return False
    if root.key == key:
        return True

    if key < root.key:
        return search(root.left, key)
    return search(root.right, key)


# -------- INORDER (SORTED OUTPUT) --------
def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)

# -------- PREORDER --------
def preorder(root):
    if root:
        print(root.key, end=" ")
        preorder(root.left)
        preorder(root.right)

# -------- POSTORDER --------
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.key, end=" ")

# -------- FIND MIN --------
def find_min(root):
    while root.left:
        root = root.left
    return root

# -------- DELETE NODE --------
def delete(root, key):
    if root is None:
        return root

    if key < root.key:
        root.left = delete(root.left, key)
    elif key > root.key:
        root.right = delete(root.right, key)

    else:
        # Case 1: No child
        if root.left is None and root.right is None:
            return None

        # Case 2: One child
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        # Case 3: Two children
        temp = find_min(root.right)
        root.key = temp.key
        root.right = delete(root.right, temp.key)
    return root


# -------- MAIN --------
root = None

values = [50, 30, 70, 20, 40, 60, 80]

for v in values:
    root = insert(root, v)

print("Inorder (sorted):")
inorder(root)

print("\nSearch 60:", search(root, 60))
print("Search 25:", search(root, 25))

print("\nDelete 20:")
root = delete(root, 20)
inorder(root)

print("\nDelete 30:")
root = delete(root, 30)
inorder(root)

print("\nDelete 50:")
root = delete(root, 50)
inorder(root)