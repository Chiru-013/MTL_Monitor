import sys
class node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

def precedence(op):
    if op == '!':
        return 4
    elif op == '^':
        return 3
    elif op == 'v':
        return 2
    else:
        return 1
  
root = [node('')]
def construc_tree(r,expr):
    cur = r
    parent = []
    i = 0
    while i < len(expr):
        if expr[i] in ['^','v','>']:
            # first check the precedence of the operator to his parent operator
            # if the precedence of the operator is less than the parent operator   
            # then pop till the parent operator and make it the left child of the operator
            # if the parent is empty then make the operator as the root
            # if the parent is not empty then make the operator as the right child of the parent
            # and make the parent as the parent of the operator
            # make the operator as the current node
            par = None
            ch = False
            while parent and (precedence(expr[i]) < precedence(parent[-1].val)):
                par = parent.pop()
                ch = True
            if ch:
                new = node(expr[i])
                if parent:
                    temp = parent[-1].right
                    parent[-1].right = new
                    new.left = temp
                else:
                    new.left = root[0]
                    root[0] = new

                parent.append(new)
                new.right = node('')
                cur = new.right
            else:
                cur.val = expr[i]
                cur.right = node('')
                parent.append(cur)
                cur = cur.right
        else:
            if expr[i] == '!':
                new = node(expr[i] + expr[i+1])
                cur.left = new
                i += 1
            else:
                cur.left = node(expr[i])
        i += 1
# writing the post order traversal with brackets for left and right child
final_expr = ''
def post_order(root):
    if root is None:
        return ''
    if root.left is None and root.right is None:
        return '(' + root.val + ')'
    lt = post_order(root.left)
    rt = post_order(root.right)
    if root.val == '>':
        return '(!' + lt +'||' + rt +')'
    else:
        return '(' + lt + root.val + rt + ')'
        
        
# print(ex)
ex = "!Rv!G"
construc_tree(root[0],ex)
final_expr = post_order(root[0])
# final_expr = final_expr.replace('v','||')
# final_expr = final_expr.replace('^','&&')
print(final_expr)














