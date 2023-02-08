import random

# True  -> 1
# Maybe -> 0
# Fasle -> -1

#UNTIL operator = p Until [t1,t2] q
t1 = 2
t2 = 5

def until_test(x,y,z):
    for i in range(len(x)):
        if p[i] == -1:
            temp = i-t2+1
            while temp <= i:
                if(temp >= 0):
                    z[temp] = -1
                temp = temp + 1 
        if q[i] == -1 and p[i] == -1:
            temp = i-t2
            while temp <= (i-t1):
                if(temp >= 0 and z[temp] == 0):
                    z[temp] = -1
                temp = temp + 1 
        elif q[i] == -1 and z[i-t2] == 0 and i-t2 > 0:
            z[i-t2] = -1
        elif q[i] == 1 and z[i-t2] == 0:
            temp = i-t2
            while temp <= (i-t1):
                if(temp >= 0 and z[temp] == 0):
                    z[temp] = 1
                temp = temp + 1 
        
p = random.choices([-1,1], k=10)
q = random.choices([-1,1], k=10)
r= [0 for i in range(len(p))]

until_test(p,q,r)

f_inp = open("until_inp.txt", "w")
f_op = open("until_op.txt", "w")

p = [str(i) for i in p]
q = [str(i) for i in q]
r = [str(i) for i in r]

for i in range(len(p)):
   f_inp.write(p[i]+","+q[i]+'\n')
   f_op.write(r[i]+'\n')

f_inp.close()
f_op.close()


