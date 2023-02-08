import random

# True  -> 1
# Maybe -> 0
# Fasle -> -1

#Box/Global/Always operator = Box [t1,t2] p

t1 = 2
t2 = 5

def box_test(x,y):
    for i in range(len(x)):
        if i-t2 >= 0:
            if x[i] == 1 and y[i-t2] == 0:
                y[i-t2] = 1
            if x[i] == -1:
                y[i-t2:i-t1+1] = [-1] * (t2-t1+1)
        elif i-t1 >= 0:
            if x[i] == -1:
                temp = 0
                while temp <= i-t1:
                    y[temp] = -1
                    temp = temp + 1
         

p = random.choices([-1,1], k=10)
r= [0 for i in range(len(p))]

box_test(p,r)

f_inp = open("box_inp.txt", "w")
f_op = open("box_op.txt", "w")

p = [str(i) for i in p]
r = [str(i) for i in r]

for i in range(len(p)):
   f_inp.write(p[i]+'\n')
   f_op.write(r[i]+'\n')
f_inp.close()
f_op.close()



