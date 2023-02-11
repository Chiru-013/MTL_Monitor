import random

# True  -> 1
# Maybe -> 0
# Fasle -> -1

#not operator = not p
#or operator = p or q


def or_test(x,y,z):
    for i in range(len(x)):
        if x[i] == -1 and y[i] == -1 :
            z.append(-1)
        else:
            z.append(1)

def not_test(x,z):
    for i in range(len(x)):
        if x[i] == -1:
            z.append(1)
        else:
            z.append(-1)

p = random.choices([-1,1], k=10)
q = random.choices([-1,1], k=10)
r_not= []
r_or = []

not_test(p,r_not)
or_test(p,q,r_or)


f_inp_not = open("not_inp.txt", "w")
f_op_not = open("not_op.txt", "w")

f_inp_or = open("or_inp.txt", "w")
f_op_or = open("or_op.txt", "w")

p = [str(i) for i in p]
q = [str(i) for i in q]

r_not = [str(i) for i in r_not]
r_or = [str(i) for i in r_or]

for i in range(len(p)):
   f_inp_not.write(p[i]+","+q[i]+'\n')
   f_op_not.write(r_not[i]+'\n')
   f_inp_or.write(p[i]+","+q[i]+'\n')
   f_op_or.write(r_or[i]+'\n')

f_inp_not.close()
f_op_not.close()
f_inp_or.close()
f_op_or.close()


