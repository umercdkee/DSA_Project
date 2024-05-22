#key is title
#Value is dictionary of the entire book data
#tree[0]=key, tree[1]=leftsubtree, tree[2]=rightsubtree, tree[3]=height, tree[4]=data
def create_node(key,value,height,left=None,right=None):
    return [key,left,right,height,value]


def insert(tree,key,value):
    if tree==None: #checks for empty (sub)tree
        tree=create_node(key,value,1)
        return tree
    
    if key<tree[0]: #checks if key is lesser than current node
        tree[1]=insert(tree[1],key,value)
    elif key>tree[0]: #checks if key is greater than current node
        tree[2]=insert(tree[2],key,value)
    
    tree=update_height(tree)
    tree=rebalance(tree)
    return tree
    

def update_height(tree):
    if tree==None: #leaf node
        return
    
    if tree[1]==None: #height of left child
        left_height=0
    else: 
        left_height=tree[1][3]

    if tree[2]==None: #height of right child
        right_height=0
    else:
        right_height=tree[2][3]
    
    height=max(left_height,right_height)+1
    tree=[tree[0],tree[1],tree[2],height,tree[4]]
    return tree


def find_balance_factor(tree):
    if tree==None:
        return 0
    
    if tree[1]==None: #finding height of left subtree
        left_subtree_height=0
    else:
        left_subtree_height=tree[1][3]
    
    if tree[2]==None: #finding height of right subtree
        right_subtree_height=0
    else:
        right_subtree_height=tree[2][3]
    
    factor=left_subtree_height-right_subtree_height
    return factor
    

def left_rotation(tree):
    root=tree[2] #right subtree of tree becomes root
    tree[2]=root[1] #left subtree of root becomes right subtree of tree
    root[1]=tree #left subtree of root becomes tree
    update_height(tree)
    update_height(root)
    return root


def right_rotation(tree):
    root=tree[1] #left subtree of tree becomes root
    tree[1]=root[2] #right subtree of root becomes left subtree of root
    root[2]=tree #right subtree of root becomes tree
    update_height(tree)
    update_height(root)
    return root
    

def rebalance(tree):
    if tree==None:
        return
    
    balance_factor=find_balance_factor(tree)

    if balance_factor>1: #checking left cases
        sub_balance_factor=find_balance_factor(tree[1])
        if sub_balance_factor>=0: #left left case
            tree=right_rotation(tree)
        else:
            tree[1]=left_rotation(tree[1]) #left right case
            tree=right_rotation(tree)
    
    elif balance_factor<-1: #checking right cases
        sub_balance_factor=find_balance_factor(tree[2])
        if sub_balance_factor>0: #righy left case
            tree[2]=right_rotation(tree[2])
            tree=left_rotation(tree)
        else: #right right case
            tree=left_rotation(tree)
        
    tree=update_height(tree)
    return tree


def search(tree,key):
    if tree==None:
        return
    
    if tree[0]==key:
        return tree[4]
    
    if tree[0]>key:
        return search(tree[1],key)
    if tree[0]<key:
        return search(tree[2],key)


def delete(tree,key):
    if tree==None:
        return None
    
    elif tree[0]>key:
        tree[1]=delete(tree[1],key)
    elif tree[0]<key:
        tree[2]=delete(tree[2],key)

    else:
        if tree[1]==None: #checks if no left child
            tree=tree[2]
        elif tree[2]==None: #checks if no right child
            tree=tree[1]
        else:
            child_key,child_value=find_min_value_node(tree[2]) #finds successor
            tree[0],tree[4]=child_key,child_value #replaces current node
            tree[2]=delete(tree[2],child_key) #deletes successor

    tree=update_height(tree)
    tree=rebalance(tree)
    return tree

def find_min_value_node(tree):
    while tree[1]!=None:
        tree=tree[1]
    return tree[0],tree[4]


def inorder_traversal(node,result):
    if node is None:
        return []
    else:
        inorder_traversal(node[1],result)
        result.append(node[0])
        inorder_traversal(node[2],result)
    return result

def update(tree,key,record,new_data):
    if tree==None:
        return
    if key<tree[0]:
        update(tree[1],key,record,new_data)
    elif key>tree[0]:
        update(tree[2],key,record,new_data)

    else:
        tree[4][record]=new_data
    

# books_database=None
# for k,v in book_dict.items():
#     title=k
#     isbn=v
#     data={'Title':title, 'ISBN':v}
#     books_database=insert(books_database,title,data)

#data={'a':1,'b':2,'c':4,'d':5,'e':6,'f':7,'g':8}
#data={'z':1,'e':2,'f':3,'d':4,'g':5}
# data={1:'a',2}
#print_books_database_keys(books_database)
#print (print_books_database_keys(books_database))
# update(books_database,'The Enchanted Garden','ISBN',314542532432)
# print (search(books_database,'The Enchanted Garden')['ISBN'])


#have it printed alphabetical order
#inorder_traversal should be in order 
#try sorting according to titles
#