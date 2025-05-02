def xor_problem(x1,x2):
    w1 = [1,-1]
    w2 = [1,-1]
    if x1*w1[0]+x2*w2[1]==x1*w1[1]+x2*w2[0]==0:
        y = 0
    else:
        y1 = 1