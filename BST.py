print("------------------------------------------------------------------------------")
print("Welcome, please enter the numbers (at least 10 numbers), then press the 'q' key to exit.")
print("!!!!Note: If it is less than 10 numbers, it gives an error!!!!")
print("------------------------------------------------------------------------------")





class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val),
        inorder(root.right)

r = None

numbers = []
while True:
    num = input("Enter the number: ")
    if num == 'q':
        if len(numbers) < 10:
            print("Error: You must enter at least 10 numbers.")
            continue
        else:
            break
    else:
        numbers.append(int(num))


for num in numbers:
    r = insert(r, num)
print("------------------------------------------------------------------------------")
print("List=",numbers)
print("BST:")
inorder(r)
input()
