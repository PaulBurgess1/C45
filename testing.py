import c45
import tree

C_45 = c45.C45("Data/iris.data")
C_45.data_fill()
C_45.build_decision_tree()