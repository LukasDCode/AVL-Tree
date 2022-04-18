# AVL-Tree
personal implementation of an avl tree


## How to Use
Simple call to run the avl tree:  
```$ python avl_tree.py```  
An empty binary-avl-tree is created and execution is set to manual & insertion mode, meaning that every Integer that is typed in the command line will be added to the tree. Everything that can not be casted into an Integer is rejected with an output message on the command line.

### Manual Mode
```$ !c <some_item>``` activates searching mode and it searches wheter ```<some_item>``` is in the tree. Everything entered in the command line from now on is checked against the content of the tree and not added to it. In order to add more items to the tree insertion mode has to be switched back on again with the following command: ```$ !i```  


This is an exhaustive list of all possible commands:  

- ```$ !q``` quit the running execution  
- ```$ !i``` toggles insertion mode  
- ```$ !s``` toggles searching mode  
- ```$ !p``` prints the current avl tree  
- ```$ !v``` activates verbose mode  

The commands can be used with an additional item (like seen above) separated by space. For example switching back to insertion mode and directly insert some new item: ```$ !i <some_item>```  
