from graphviz import Digraph
class Node:

    def __init__(self, info,ID):

        self.left = None  #less than value
        self.right = None #greater than value
        self.id = ID
        self.info = info
        self.childrenID = None

    def print_tree(self,tree):
        if ( tree is not None):
            if (tree.childrenID is None):
                print("ID : " +str(tree.id)+ " , Class : "+tree.info)
            else:
                print("ID : " +str(tree.id)+ " , Info : "+tree.info+ " , Left Child ID: "+str(tree.childrenID[0])+" , Right Child ID: "+str(tree.childrenID[1]))
                self.print_tree(tree.left)
                self.print_tree(tree.right)
    def tree_queue(self,tree,queue):
        if ( tree is not None):
            if (tree.childrenID is None):
                queue.append(tree)
            else:
                queue.append(tree)
                self.tree_queue(tree.left,queue)
                self.tree_queue(tree.right,queue)
        return queue
    def tree_graph(self,tree):
        f = Digraph('tree_graph', filename='tree_graph.gv')
        queue=[]
        queue=self.tree_queue(tree,queue)
        
        for n in queue:
            f.node(str(n.id)+"_"+n.info, label=n.info)
        for e in queue:
            if(e.childrenID is not None):
                f.edge(str(e.id)+"_"+e.info, str(e.left.id)+"_"+e.left.info)
                f.edge(str(e.id)+"_"+e.info, str(e.right.id)+"_"+e.right.info)
        f.view()