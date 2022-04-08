class Node:

    def __init__(self, value):
        self.value = value
        self.parent = None
        self.smaller = None
        self.bigger = None
        pass

    def get_value():
        return self.value


class Tree:
    def __init__(self):
        self.root = None

    def insert(item):
        if root == None:
            root = Node(item)
        else:
            pass

    def search(item):
        pass


    # not implemented for this project
    def delete(item):
        pass

    # not implemented for this project
    def range_search():
        pass


def manual_mode(tree):
    is_insert_mode = True
    print("setup avl tree")
    print("'!q' to quit, '!i' to toggle insertion mode, '!s' to toggle search mode")
    print("!p to print the current filter array, !v to toggle verbose mode")
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
                #elif user_input[1].lower() == "p": # print
                #    tree.print_filter()
                elif user_input[1].lower() == "v": # verbose
                    tree.toggle_verbose()
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
            if is_insert_mode:
                tree.insert(item)
            else:
                in_set = tree.search(item)
                if in_set:
                    print(item, "is probably in the set")
                else:
                    print(item, "is definitely not in the set")
        else:
            print("no useful input detected")
    

def main(args):
    tree = Tree()
    manual_mode(tree)

if __name__ == "__main__":
    main()