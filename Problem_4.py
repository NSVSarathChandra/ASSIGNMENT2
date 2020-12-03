import numpy as np
import math

#Define points P, Q and R

P = np.array([-3,-4])
Q = np.array([2,6])
R = np.array([-6,10])

#Calculate a, b and c - that is, the distances between P and Q, Q and R, P and R respectively

a = np.linalg.norm(P-Q)

b = np.linalg.norm(Q-R)

c = np.linalg.norm(P-R)


print(a)
print(b)
print(c)

d = math.sqrt((pow(a,2)+pow(b,2)))


print(d)


##Since d = c hence proved that P, Q, R make right angled triangle based on Bodhayana theorem


## Orthogonality principle

vec_X_PQ_BAR = Q-P
vec_Y_QR_BAR = R-Q
vec_Z_PR_BAR = R-P


## Calculate XT*Y

XT = vec_X_PQ_BAR.transpose()

XTY = np.matmul(XT, vec_Y_QR_BAR)

print(XTY)

##Since XTY =0, hence proved that P, Q, R make right angled triangle based on the orthogonality principle

