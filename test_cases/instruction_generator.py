#tree_problem:  Should add n-1 extra brackets at the end if continuously using n unary operators
#if op1 and op2 are unary ops then instead of (op1 (op2 A)) Enter ( (op1 ( op2 ) ) )
# for three unary operators ( ( ( op1 ( op2 (op3 A ) ) ) ) )

from pythonds.basic import Stack
from pythonds.trees import BinaryTree

inst = []
QID = ['#']

def buildParseTree(fexp):
    flst = [char for char in fexp]
    flst = [char for char in flst if char != ' ']

    print(flst)
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree
    j = -1
    for i in flst:
        j = j + 1
        # print(i)
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
            print("brac" + str(j))
        elif i in ['!', '@', '$', 'O']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i in ['^', 'v', 'U']:
            currentTree.setRootVal(i)
            print(currentTree.getRootVal())
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
            print("s" + str(j))

        elif i == ')':
            currentTree = pStack.pop()
            print("close" + str(j))

        elif i not in ['!', '^', 'v', '@', '$', 'U', 'O', ')']:
            try:
                currentTree.setRootVal(i)
                parent = pStack.pop()
                currentTree = parent
                print(i + str(j))

            except ValueError:
                raise ValueError("token '{}' is not a valid integer".format(i))            
    print("printed:" + currentTree.getRootVal())
    return eTree


import operator
def evaluate(parseTree):
    opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}

    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()

    if leftC and rightC:
        fn = opers[parseTree.getRootVal()]
        return fn(evaluate(leftC),evaluate(rightC))
    else:
        return parseTree.getRootVal()

def postorder(tree):
    if tree != None:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())
        inst.append(tree.getRootVal())


def not_gen(a):
    global QID
    temp = -1
    if len(QID) > 1:
        for i in range(len(QID)):
            if QID[i] == a:
                not_list = ["not"+a,0, i+1, -1, str(len(QID)+1),[31,31,0,0,31,31,31,31,31,31],[0,0,31,31,31,31,31,31,31,31]]
                QID.append("not_gen("+a+")")
                temp = 1

    if(temp == -1):   
        not_list = ["not"+a,0, str(len(QID)+1), -1, str(len(QID)+2),[31,31,0,0,31,31,31,31,31,31],[0,0,31,31,31,31,31,31,31,31]]
        QID.append(a)
        QID.append("not_gen("+a+")")
    
    with open('instructions.txt', 'a') as f:
        f.write("\n")
        for item in not_list:
            f.write("%s  " % item)
        f.write("\n")
    
    return("not_gen("+a+")")
    

def next_gen(a):
    global QID
    temp = -1
    if len(QID) > 1:
        for i in range(len(QID)):
            if QID[i] == a:
                next_list = ["next"+a,0, i+1, -1, str(len(QID)+1),[1,1,31,31,0,0,31,31,31,31],[31,31,1,1,0,0,31,31,31,31]]
                temp = 1
                QID.append("next_gen("+a+")")

    if temp == -1:
        next_list = ["next"+a,0, str(len(QID)+1), -1, str(len(QID)+2),[1,1,31,31,0,0,31,31,31,31],[31,31,1,1,0,0,31,31,31,31]]
        QID.append(a)
        QID.append("next_gen("+a+")")

    with open('instructions.txt', 'a') as f:
        f.write("\n")
        for item in next_list:
            f.write("%s  " % item)
        f.write("\n")
    
    return("next_gen("+a+")")

def box_gen(a):
    global QID
    temp = -1
    print("\n\nEnter the interval for box("+a+"):")
    t1 = int(input("t1:"))
    t2 = int(input("t2:"))

    if len(QID) > 1:
        for i in range(len(QID)):
            if QID[i] == a:
                box_list = ["box"+a,0, i+1, -1, str(len(QID)+1),[31,31,31,31,0,0,t2,t2,31,31],[31,31,t2,t1,0,0,31,31,31,31]]
                temp = 1
                QID.append("box_gen("+a+")")
    
    if temp == -1:
        box_list = ["box"+a,0, str(len(QID)+1), -1, str(len(QID)+2),[31,31,31,31,0,0,t2,t2,31,31],[31,31,t2,t1,0,0,31,31,31,31]]
        QID.append(a)
        QID.append("box_gen("+a+")")
    
    with open('instructions.txt', 'a') as f:
        f.write("\n")
        for item in box_list:
            f.write("%s  " % item)
        f.write("\n")

    return("box_gen("+a+")")

def dia_gen(a):
    global QID
    temp = -1
    print("\n\nEnter the interval for diamond("+a+"):")
    t1 = int(input("t1:"))
    t2 = int(input("t2:"))

    if len(QID) > 1:
        for i in range(len(QID)):
            if QID[i] == a:
                dia_list = ["diamond"+a,0, i+1, -1, str(len(QID)+1),[t2,t1,31,31,0,0,31,31,31,31],[31,31,31,31,0,0,31,31,t2,t2]]
                temp = 1
                QID.append("dia_gen("+a+")")

    if temp == -1:
        dia_list = ["diamond"+a,0, str(len(QID)+1), -1, str(len(QID)+2),[t2,t1,31,31,0,0,31,31,31,31],[31,31,31,31,0,0,31,31,t2,t2]]
        QID.append(a)
        QID.append("dia_gen("+a+")")

    with open('instructions.txt', 'a') as f:
        f.write("\n")
        for item in dia_list:
            f.write("%s  " % item)
        f.write("\n")

    return("dia_gen("+a+")")
   

def or_gen(a):
    global QID
   
    if a[0] and a[1] in QID:
        or_list = ["or"+a[0]+","+a[1],0, QID.index(a[0])+1, QID.index(a[1])+1, str(len(QID)+1),[0,0,31,31,31,31,31,31,31,31],[0,0,31,31,31,31,31,31,31,31]]
        QID.append("or_gen("+a[0]+a[1]+")")
    elif a[0] in QID:
        or_list = ["or"+a[0]+","+a[1],0, QID.index(a[0])+1, str(len(QID)+1), str(len(QID)+2),[0,0,31,31,31,31,31,31,31,31],[0,0,31,31,31,31,31,31,31,31]]
        QID.append(a[1])
        QID.append("or_gen("+a[0]+a[1]+")")
    elif a[1] in QID:
        or_list = ["or"+a[0]+","+a[1],0, str(len(QID)+1), QID.index(a[1])+1, str(len(QID)+2),[0,0,31,31,31,31,31,31,31,31],[0,0,31,31,31,31,31,31,31,31]]
        QID.append(a[0])
        QID.append("or_gen("+a[0]+a[1]+")")
    elif a[0] and a[1] not in QID:
        or_list = ["or"+a[0]+","+a[1],0, str(len(QID)+1), str(len(QID)+2), str(len(QID)+3),[0,0,31,31,31,31,31,31,31,31],[0,0,31,31,31,31,31,31,31,31]]
        QID.append(a[0])
        QID.append(a[1])
        QID.append("or_gen("+a[0]+a[1]+")")
    
    with open('instructions.txt', 'a') as f:
        f.write("\n")
        for item in or_list:
            f.write("%s  " % item)
        f.write("\n")

    return("or_gen("+a[0]+a[1]+")")


def and_gen(a):
    global QID
   
    if a[0] and a[1] in QID:
        and_list = ["and"+a[0]+","+a[1],1, QID.index(a[0])+1, QID.index(a[1])+1, str(len(QID)+1),[0,0,31,31,31,31,31,31,31,31],[0,0,31,31,31,31,31,31,31,31]]
        QID.append("and_gen("+a[0]+a[1]+")")
    elif a[0] in QID:
        and_list = ["and"+a[0]+","+a[1],1, QID.index(a[0])+1, str(len(QID)+1), str(len(QID)+2),[0,0,31,31,31,31,31,31,31,31],[0,0,31,31,31,31,31,31,31,31]]
        QID.append(a[1])
        QID.append("and_gen("+a[0]+a[1]+")")
    elif a[1] in QID:
        and_list = ["and"+a[0]+","+a[1],1, str(len(QID)+1), QID.index(a[1])+1, str(len(QID)+2),[0,0,31,31,31,31,31,31,31,31],[0,0,31,31,31,31,31,31,31,31]]
        QID.append(a[0])
        QID.append("and_gen("+a[0]+a[1]+")")
    elif a[0] and a[1] not in QID:
        and_list = ["and"+a[0]+","+a[1],1, str(len(QID)+1), str(len(QID)+2), str(len(QID)+3),[0,0,31,31,31,31,31,31,31,31],[0,0,31,31,31,31,31,31,31,31]]
        QID.append(a[0])
        QID.append(a[1])
        QID.append("and_gen("+a[0]+a[1]+")")
    
    with open('instructions.txt', 'a') as f:
        f.write("\n")
        for item in and_list:
            f.write("%s  " % item)
        f.write("\n")

    return("and_gen("+a[0]+a[1]+")")

def until_gen(a):
    global QID
   
    print("\n\nEnter the interval for until("+a[0]+","+a[1]+"):")
    t1 = int(input("t1:"))
    t2 = int(input("t2:"))

    if a[0] and a[1] in QID:
        until_list1 = ["until1"+a[0]+","+a[1],0, QID.index(a[0])+1, QID.index(a[1])+1, str(len(QID)+1),[31,31,31,31,0,0,31,31,31,31],[31,31,t1-1,0,31,31,31,31,31,31]]
        until_list2 = ["until2"+a[0]+","+a[1],0, QID.index(a[0])+1, QID.index(a[1])+1, str(len(QID)+1),[31,31,31,31,31,31,31,31,t2,t1],[31,31,31,31,31,31,31,31,t2,t2]]
        until_list3 = ["until3"+a[0]+","+a[1],0, QID.index(a[0])+1, QID.index(a[1])+1, str(len(QID)+1),[31,31,31,31,31,31,31,31,31,31],[31,31,31,31,31,31,31,31,t2,t1]]
        QID.append("until_gen("+a[0]+a[1]+")")
    elif a[0] in QID:
        until_list1 = ["until1"+a[0]+","+a[1],0, QID.index(a[0])+1, str(len(QID)+1), str(len(QID)+2),[31,31,31,31,31,31,31,31,t2,t1],[31,31,31,31,31,31,31,31,t2,t2]]
        until_list2 = ["until2"+a[0]+","+a[1],0, QID.index(a[0])+1, str(len(QID)+1), str(len(QID)+2),[31,31,31,31,0,0,31,31,31,31],[31,31,t1-1,0,31,31,31,31,31,31]]
        until_list3 = ["until3"+a[0]+","+a[1],0, QID.index(a[0])+1, str(len(QID)+1), str(len(QID)+2),[31,31,31,31,31,31,31,31,31,31],[31,31,31,31,31,31,31,31,t2,t1]]
        QID.append(a[1])
        QID.append("until_gen("+a[0]+a[1]+")")
    elif a[1] in QID:
        until_list1 = ["until1"+a[0]+","+a[1],0, str(len(QID)+1),QID.index(a[1])+1, str(len(QID)+2),[31,31,31,31,31,31,31,31,t2,t1],[31,31,31,31,31,31,31,31,t2,t2]]
        until_list2 = ["until2"+a[0]+","+a[1],0, str(len(QID)+1),QID.index(a[1])+1, str(len(QID)+2),[31,31,31,31,0,0,31,31,31,31],[31,31,t1-1,0,31,31,31,31,31,31]]
        until_list3 = ["until3"+a[0]+","+a[1],0, str(len(QID)+1),QID.index(a[1])+1, str(len(QID)+2),[31,31,31,31,31,31,31,31,31,31],[31,31,31,31,31,31,31,31,t2,t1]]
        QID.append(a[0])
        QID.append("until_gen("+a[0]+a[1]+")")
    elif a[0] and a[1] not in QID:
        until_list1 = ["until1"+a[0]+","+a[1],0, str(len(QID)+1),str(len(QID)+2), str(len(QID)+3),[31,31,31,31,31,31,31,31,t2,t1],[31,31,31,31,31,31,31,31,t2,t2]]
        until_list2 = ["until2"+a[0]+","+a[1],0, str(len(QID)+1),str(len(QID)+2), str(len(QID)+3),[31,31,31,31,0,0,31,31,31,31],[31,31,t1-1,0,31,31,31,31,31,31]]
        until_list3 = ["until3"+a[0]+","+a[1],0, str(len(QID)+1),str(len(QID)+2), str(len(QID)+3),[31,31,31,31,31,31,31,31,31,31],[31,31,31,31,31,31,31,31,t2,t1]]
        QID.append(a[0])
        QID.append(a[1])
        QID.append("until_gen("+a[0]+a[1]+")")
    
    with open('instructions.txt', 'a') as f:
        f.write("\n")
        for item in until_list1:
            f.write("%s  " % item)
        f.write("\n")
    with open('instructions.txt', 'a') as f:
        f.write("\n")
        for item in until_list2:
            f.write("%s  " % item)
        f.write("\n")
    with open('instructions.txt', 'a') as f:
        f.write("\n")
        for item in until_list3:
            f.write("%s  " % item)
        f.write("\n")

    return("until_gen("+a[0]+a[1]+")")

def inst_choose(x):
    ap=[]
    op=[]
    result = "-1"
    r = -1
    print('\n')
    for i in x:
        if i not in ['!', '^', 'v', '@', '$', 'U', 'O']:
            ap.append(i)
            print(ap)
        else:
            op.append(i)
            print(op)

        if len(ap) == 1 and len(op) != 0:
            if op[0] == '!':
                result = "not_gen(" + ap[0] + ")"
                r = not_gen(ap[0])
                ap.clear()
                op.clear()
                print(result)  
            elif op[0] == '@':
                result = "box_gen(" + ap[0] + ")"
                r = box_gen(ap[0])
                ap.clear()
                op.clear()
                print(result)  
            elif op[0] == '$':
                result = "diamond_gen(" + ap[0] + ")"
                r = dia_gen(ap[0])
                ap.clear()
                op.clear()
                print(result)  
            elif op[0] == 'O':
                result = "next_gen(" + ap[0]+ ")"
                r = next_gen(ap[0])
                ap.clear()
                op.clear()
                print(result)  
        elif len(ap) == 2 and len(op) != 0:
            if op[0] == '^':
                result = "and_gen(" + ap[0] + "," + ap[1] + ")"
                r = and_gen(ap)
                ap.clear()
                op.clear()
                print(result)  
            elif op[0] == 'v':
                result = "or_gen(" + ap[0] + "," + ap[1] + ")"
                r = or_gen(ap)
                ap.clear()
                op.clear()
                print(result)  
            elif op[0] == 'U':
                result = "until_gen(" + ap[0] + "," + ap[1] + ")"
                r = until_gen(ap)
                ap.clear()
                op.clear()
                print(result)     
        if len(ap) == 0:
            ap.append(r)
        print(ap)
        print(op)
        print('\n')


exp = "( ( O ( A v B ) ) ) U C"
pt = buildParseTree(exp)
postorder(pt)  #defined and explained in the next section
f = open("instructions.txt","a")
f.write("\n----------New Property:- " + exp +" -----------\n")
f.close()
# print(evaluate(pt))
print(inst)
inst = [char for char in inst if char != '']
print(inst)
inst_choose(inst)


