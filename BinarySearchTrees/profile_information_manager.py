from user import User
from user_database import UserDatabase
from binary_tree import TreeNode


# Binary Tree Practice


#   QUESTION 2: Implement a binary tree using Python, and show its usage with some examples.

    ## Answer
tree = TreeNode.parse_tuple(((1,3,None), 2, ((None, 3, 4), 5, (6, 7, 8))))
print("Binary Tree \n")
print("\t",TreeNode.display_keys(tree, '  '),"\n")

#   QUESTION 3: Write a function to perform the inorder traversal of a binary tree.

    ## Answer
inordered_tree = TreeNode.tree_inorder_traversal(tree)
print("Inordered Tree: ",inordered_tree, '\n')

#   QUESTION 4: Write a function to perform the preorder traversal of a binary tree.

    ## Answer
preordered_tree = TreeNode.tree_preorder_traversal(tree)
print("Preordered Tree: ",preordered_tree, '\n')

#   QUESTION 5: Write a function to perform the postorder traversal of a binary tree.

    ## Answer
postordered_tree = TreeNode.tree_postorder_traversal(tree)
print("Postordered Tree: ",postordered_tree, '\n')


#   QUESTION 1: As a senior backend engineer at Jovian, you are tasked with developing a fast in-memory data structure to manage profile information (username, name and email)
# of for 100 million users. It should allow the following operations to be performed efficiently:

#     Insert the profile information for a new user.
#     Find the profile information of a user, given their username
#     Update the profile information of a user, given their username
#     List all the users of the platform, sorted by username

# You can assume that usernames are unique.

    ## Answer
alice = User('alice24', 'Alice', 'alice@example.com')
bob = User('bob88', 'Bob', 'bob@example.com')
charlie = User('charlie15', 'Charlie', 'charlie@example.com')
emma = User('emma27', 'Emma', 'emma@example.com')
frank = User('frank42', 'Frank', 'frank@example.com')
grace = User('grace33', 'Grace', 'grace@example.com')
henry = User('henry77', 'Henry', 'henry@example.com')
isabella = User('isabella19', 'Isabella', 'isabella@example.com')
jack = User('jack10', 'Jack', 'jack@example.com')
lily = User('lily55', 'Lily', 'lily@example.com')

users = [alice, bob, charlie, emma, frank, grace, henry, isabella, jack, lily]

# Insert the list of users into the database
database = UserDatabase()
i=0
while( i < len(users)):
    database.insert(users[i])
    i += 1



