import random

# True  -> 1
# Maybe -> 0
# Fasle -> -1

#and operator = not ((not p[i]) or (not q[i]))

def and_test(x,y,z):
    for i in range(len(x)):
        if x[i] == 1 and y[i] == 1 :
            z.append(1)
        else:
            z.append(-1)

p = random.choices([-1,1], k=10)
q = random.choices([-1,1], k=10)
r= []
and_test(p,q,r)


f_inp = open("and_inp.txt", "w")
f_op = open("and_op.txt", "w")
p = [str(i) for i in p]
q = [str(i) for i in q]
r = [str(i) for i in r]
for i in range(len(p)):
   f_inp.write(p[i]+","+q[i]+'\n')
   f_op.write(r[i]+'\n')
f_inp.close()
f_op.close()


