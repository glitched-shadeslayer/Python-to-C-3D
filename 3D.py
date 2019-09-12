import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

def line_dir_pt(m,A):
  len = 10
  x_AB = np.zeros((3,len))
  lam_1 = np.linspace(0,10,len)
  for i in range(len):
    temp1 = A + lam_1[i]*m
    x_AB[:,i]= temp1.T
  return x_AB

O = np.array([0,0,0]).reshape((3,1))
A = np.array([1,1,0]).reshape((3,1))
B = np.array([0,3,4]).reshape((3,1))
l= A

xx, yy = np.meshgrid(range(10), range(10))
#setting up plot
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d',aspect='equal')

k = -(B.T@A)/(A.T@A)
P = B + k*A
m = B - P 
print("Point P = ", P.T)

#generating points in line 
l1_p = line_dir_pt(l,O)
l2_p = line_dir_pt(m,P)

plt.plot(l1_p[0,:],l1_p[1,:],l1_p[2,:],label="Line $OA$")
plt.plot(l2_p[0,:],l2_p[1,:],l2_p[2,:],label="Line $BP$")

ax.scatter(A[0],A[1],A[2],'o',label="Point A")
ax.scatter(B[0],B[1],B[2],'o',label="Point B")
ax.scatter(O[0],O[1],O[2],'o',label="Point O")
ax.scatter(P[0],P[1],P[2],'o',label="Point P")

plt.xlabel('$x$');plt.ylabel('$y$')

plt.legend(loc='best');plt.grid()
plt.axis([-2,1.5,0,3.5])
plt.show()

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

#creating x,y for 3D plotting
xx, yy = np.meshgrid(range(10), range(10))
#setting up plot
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d',aspect='equal')

#defining direction vectors of planes
l1 = np.array([3/2,3/2,0])
l2 = np.array([-3/2,3/2,4])

#finding cross product
cp = np.cross(l1,l2)

#plotting lines
plt.plot([0,l1[0]],[0,l1[1]],[0,l1[2]],label="Direction Vector of B-P")
plt.plot([0,l2[0]],[0,l2[1]],[0,l2[2]],label="Direction Vector of P")
plt.plot([0,cp[0]],[0,cp[1]],[0,cp[2]],label="Cross Product Vector")

#printing cross product
print("Cross Product = ",cp)

#show plot
plt.xlabel('$x$');plt.ylabel('$y$')
plt.legend(loc='best');plt.grid()
plt.axis('equal')

plt.show()
