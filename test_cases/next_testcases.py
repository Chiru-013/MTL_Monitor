import random

# True  -> 1
# Maybe -> 0
# Fasle -> -1

#next operator = Op

def and_test(x,z):
    for i in range(len(x)):
        if i == len(x)-1:
            z.append(0)
        elif x[i+1] == 1:
            z.append(1)
        else:
            z.append(-1)

p = random.choices([-1,1], k=10)
r= []
and_test(p,r)


f_inp = open("next_inp.txt", "w")
f_op = open("next_op.txt", "w")

p = [str(i) for i in p]
r = [str(i) for i in r]

for i in range(len(p)):
   f_inp.write(p[i]+'\n')
   f_op.write(r[i]+'\n')

f_inp.close()
f_op.close()


