Idea how to build expression while traversing parsing tree

```python
class TreeTraversal:
    def get_child(self, id):
        return self._childs[id]._traversal()
    
    def _traversal(self):
        if len(self.childs) == 1:
            return self.get_child(0).traversal()
        elif len(self.childs) == 3:
            oper = self.get_child(0)
            arg1 = self.get_child(1)
            arg2 = self.get_child(2)
            
            if oper == "+":
                return Add(arg1, arg2)
            elif oper == "-":
                return Sub(arg1, arg2)
            elif oper == "*":
                return Mul(arg1, arg2)
            elif oper == "/":
                return Div(arg1, arg2)
            else:
                raise TraversalError()
            

```