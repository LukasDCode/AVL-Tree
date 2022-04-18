verbose = False

class Node:
    """
    Node objects have to handle all the heavy lifting of this data structure.
    All operations either happen on the level of the node or recursively down the line.
    Nodes with smaller values are stored in the 'smaller' value, as the name indicates,
    but bigger AND EQUAL (!) values are stored in the 'bigger' value.
    """
    
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.smaller = None
        self.bigger = None
        self.height_smaller = 0
        self.height_bigger = 0


    def print_node(self):
        # print looks like this <value>hs<height_of_smaller_subtree>hb<height_of_bigger_subtree>
        return str(self.value)+"hs"+str(self.height_smaller)+"hb"+str(self.height_bigger)


    def search(self, item):
        """
        If the value is not found in this node,
        the node lets its child nodes continue the search based on the value.
        """
        if item == self.value:
            return True
        else:
            if item < self.value:
                if self.smaller:
                    return self.smaller.search(item)
                else:
                    return False
            else:
                if self.bigger:
                    return self.bigger.search(item)
                else:
                    return False


    def insert(self, item):
        """
        If the corresponding child of this node is empty, the new node with
        the new value is placed in this position
        otherwise the task is handed on to the corresponding child node.
        After insertion the tree checks its balance and rotates accordingly.
        """
        if item < self.value:
            if self.smaller:
                self.smaller.insert(item)
            else:
                self.smaller = Node(item)
                self.smaller.parent = self
            self.smaller.__adjust_parent_height()

        else:
            if self.bigger:
                self.bigger.insert(item)
            else:
                self.bigger = Node(item)
                self.bigger.parent = self
            self.bigger.__adjust_parent_height()


    def __fix_parent_relation(self, parent, swap):
        """
        Sets the pointer to a smaller Node of a parent Node.
        Returns the swap Node if it is the tree of the root (= has no parent).
        """
        if parent:
            if parent.smaller == self:
                parent.smaller = swap
            else:
                parent.bigger = swap            
            return None
        else:
            return swap

    def __adjust_parent_height(self):
        """
        Recursively goes the tree back up to the root and updates all the smaller and bigger heights.
        Heights only get updated when the value actually changes, this is important for verbose reasons.
        Checks are done while inserting and while rotating, so the verbose output does not get overblown.
        """
        if self.parent:
            new_value = max(self.height_bigger, self.height_smaller) + 1
            if self == self.parent.smaller:
                if self.parent.height_smaller != new_value:
                    if verbose: print("update smaller height of", self.parent.value, "to", new_value)
                    self.parent.height_smaller = new_value
            else:
                if self.parent.height_bigger != new_value:
                    if verbose: print("update bigger height of", self.parent.value, "to", max(self.height_bigger, self.height_smaller) + 1)
                    self.parent.height_bigger = new_value
            self.parent.__adjust_parent_height()


    def left_rotation(self):
        # rearranging all the pointers
        parent = self.parent
        swap = self.bigger

        _tmp = swap.smaller
        swap.smaller = self
        self.parent = swap
        self.bigger = _tmp
        swap.parent = parent
        
        return_node = self.__fix_parent_relation(parent, swap)
        
        # updating the heights
        if _tmp:
            self.height_bigger = max(_tmp.height_smaller, _tmp.height_bigger) + 1
        else:
            self.height_bigger = 0
        
        swap.height_smaller = max(self.height_smaller, self.height_bigger) + 1
        swap.__adjust_parent_height()

        return return_node # either the new root or None
        

    def right_rotation(self):
        # rearranging all the pointers
        parent = self.parent
        swap = self.smaller

        _tmp = swap.bigger
        swap.bigger = self
        self.parent = swap
        self.smaller = _tmp
        swap.parent = parent
        
        return_node = self.__fix_parent_relation(parent, swap)
        
        # updating the heights
        if _tmp:
            self.height_smaller = max(_tmp.height_smaller, _tmp.height_bigger) + 1
        else:
            self.height_smaller = 0
        
        swap.height_bigger = max(self.height_smaller, self.height_bigger) + 1
        swap.__adjust_parent_height()

        return return_node # either the new root or None
        

class Tree:
    """
    The main work of the tree is basically burdened onto the individual nodes.
    Tree objects only consist of one root node.
    """

    def __init__(self):
        self.root = None
        verbose = False

    def print_tree(self):
        """
        Source: https://stackoverflow.com/a/1894914 (slightly modified)
        Smaller values get printed first, bigger values last.
        The printing is NOT optimal! When a node only has a right child its output still does get aligned left!
        """
        if not self.root:
            print("tree is empty")
            return
        this_level = [self.root]
        while this_level:
            next_level = list()
            this_level_values = ""
            for node in this_level:
                this_level_values += " " + node.print_node() # space is important for multidigit integer
                if node.smaller: next_level.append(node.smaller)
                if node.bigger: next_level.append(node.bigger)
            print(this_level_values)
            this_level = next_level


    def search(self, item):
        return self.root.search(item)

    def insert(self, item):
        """
        After each insertion, the heights of the nodes are checked and specific subtrees are rotated if necessary.
        The first inserted Node is stored as the root of the Tree object.
        """
        if self.root:
            self.root.insert(item)
            return_node = self.check_imbalance_and_rotate(self.root)
            if return_node:
                self.root = return_node
        else:
            self.root = Node(item)
            

    # not implemented for this project
    def delete(self, item):
        pass

    def check_imbalance_and_rotate(self, node):
        """
        Goes down to the leafs and recursively checks whether rotations, simple or double, are necessary.
        Returns a rotated Node as the new root, if the root of the tree has changed.
        """
        return_node = None # None if root of the tree does not change
        if node.smaller: _ = self.check_imbalance_and_rotate(node.smaller)
        if node.bigger: _ = self.check_imbalance_and_rotate(node.bigger)

        if node.height_smaller > node.height_bigger + 1:
            # simple right rotation
            if node.smaller.height_smaller > node.smaller.height_bigger:
                if verbose: print("imbalance at node", node.value, "to the smaller side\n--> simple right rotation")
                return_node = node.right_rotation()
            # left and then right rotation
            else:
                if verbose: print("imbalance at node", node.value, "to the smaller side and then to the bigger side"
                    + "\n--> left rotation and then right rotation")
                _ = node.smaller.left_rotation()
                return_node = node.right_rotation()
        elif node.height_smaller + 1 < node.height_bigger:
            # simple left rotation
            if node.bigger.height_smaller < node.bigger.height_bigger:
                if verbose: print("imbalance at node", node.value, "to the bigger side\n--> simple left rotation")
                return_node = node.left_rotation()
            # right and then left rotation
            else:
                if verbose: print("imbalance at node", node.value, "to the bigger side and then to the smaller side"
                    + "\n--> right rotation and then left rotation")
                _ = node.bigger.right_rotation()
                return_node = node.left_rotation()
        
        return return_node # only returns a non-None node, when the root is rotated


def manual_mode(tree):
    is_insert_mode = True
    print("setup avl tree")
    print("'!q' to quit, '!i' to toggle insertion mode, '!s' to toggle search mode")
    print("!p to print the current tree as an array, !v to toggle verbose")
    print("insertion mode activated")
    while(True):
        user_input = input().lstrip() # lstrip removes leading spaces & tabs
        if user_input == "":
            print("no useful input detected, try again")
            continue
        
        if user_input[0] == "!":
            try:
                if user_input[1].lower() == "i": # insert
                    is_insert_mode = True
                    print("insertion mode activated")
                elif user_input[1].lower() == "s": # search
                    is_insert_mode = False
                    print("search mode activated")
                elif user_input[1].lower() == "p": # print
                    tree.print_tree()
                elif user_input[1].lower() == "v": # print
                    global verbose
                    verbose = not verbose
                elif user_input[1].lower() == "q": # quit
                    break
                else:
                    print("unknown symbol after '!' - no action executed")
                    continue
            except IndexError:
                print("letter after '!' expected - no action executed")
                continue

            try: # tries switching modes and applying new item
                item = user_input.split()[1]
            except IndexError:
                continue # only switching modes, without inserting or checking
        else:
            item = user_input.split()[0]

        if item:
            try:
                item = int(item)
            except ValueError:
                print("value error, only Integers allowed - no action executed")
                continue

            if is_insert_mode:
                tree.insert(item)
            else:
                in_set = tree.search(item)
                if in_set:
                    print(item, "is stored in the tree")
                else:
                    print(item, "is NOT stored in the tree")
        else:
            print("no useful input detected")
    

def main():
    tree = Tree()
    manual_mode(tree)

if __name__ == "__main__":
    main()