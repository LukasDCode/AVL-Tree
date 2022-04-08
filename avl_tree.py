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
        node_value = str(self.value)+"hs"+str(self.height_smaller)+"hb"+str(self.height_bigger)
        if self.smaller != None: node_value += " " + self.smaller.print_node()
        if self.bigger != None: node_value += " " + self.bigger.print_node()
        return node_value

    def search(self, item):
        """
        If the value is not found in this node,
        the node lets its child nodes continue the search based on the value.
        """
        if item == self.value:
            return True
        else:
            if item < self.value:
                if self.smaller == None:
                    return False
                else:
                    return self.smaller.search(item)
            else:
                if self.bigger == None:
                    return False
                else:
                    return self.bigger.search(item)


    def insert(self, item):
        """
        If the corresponding child of this node is empty, the new node with
        the new value is placed in this position
        otherwise the task is handed on to the corresponding child node.
        After insertion the tree checks its balance and rotates accordingly.
        """
        if item < self.value:
            if self.smaller == None:
                self.smaller = Node(item)
                self.smaller.parent = self
            else:
                self.smaller.insert(item)
            self.height_smaller += 1
        else:
            if self.bigger == None:
                self.bigger = Node(item)
                self.bigger.parent = self
            else:
                self.bigger.insert(item)
            self.height_bigger += 1

        # TODO after insertion check for imbalance and rotate if necessary
        if self.height_smaller > self.height_bigger + 1:
            print("imbalance to the smaller side at Node", self.value)
            pass
        elif self.height_smaller + 1 < self.height_bigger:
            print("imbalance to the bigger side at Node", self.value)
            pass


class Tree:
    """
    The main work of the tree is basically burdened onto the individual nodes.
    Tree objects only consist of one root node.
    """

    def __init__(self):
        self.root = None

    def print_tree(self):
        print(self.root.print_node())

    def search(self, item):
        return self.root.search(item)

    def insert(self, item):
        if self.root == None:
            self.root = Node(item)
        else:
            self.root.insert(item)


    # not implemented for this project
    def delete(self, item):
        pass


def manual_mode(tree):
    is_insert_mode = True
    print("setup avl tree")
    print("'!q' to quit, '!i' to toggle insertion mode, '!s' to toggle search mode")
    print("!p to print the current tree as an array")
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