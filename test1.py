with open("b_little_bit_of_everything.in", "r") as f:
    lines = f.readline(); 

    q = lines.split(' ')    
    #q.pop(4)
#print(q)
new=[]
for item in q:
    item = int(item)
    new.append(item)
#print(new)

M = new[0] ; T2 = new[1] ; T3 = new[2] ; T4 = new[3] ; 

X = T2*2 + T3*3 + T4*4
loss = X - M
#print(loss)

t3l = 0
if loss%2 == 1:
    t3l += 1
    loss -=3

#print(loss)

t4l = 0
t2l = 0
while loss>0:
    if loss%4 == 0:
        loss -= 4
        t4l += 1

    else:
        loss -= 2
        t2l += 1
print(T2-t2l+T3-t3l+T4-t4l) # number of deliveries
print(T2-t2l,T3-t3l,T4-t4l) # team wise count

