from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from funcs import *
import numpy as np

def line_dir_pt(m,A):
  len = 10
  x_AB = np.zeros((3,len))
  lam_1 = np.linspace(0,10,len)
  for i in range(len):
    temp1 = A + lam_1[i]*m
    x_AB[:,i]= temp1.T
  return x_AB


#creating x,y for 3D plotting
len = 10
xx, yy = np.meshgrid(range(len), range(len))
#setting up plot
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d',aspect='equal')


#defining line : x(k) = A + k*l
B = np.array([0,3,4]).reshape((3,1))
B2 = np.array([-3/2,3/2,4]).reshape((3,1))

#generating points in Line 
l1_p = line_dir_pt(B2-B,B)

#plotting line
plt.plot(l1_p[0,:],l1_p[1,:],l1_p[2,:],label="Line $L_1$")

#defining line : x(k) = A + k*l
A = np.array([1,1,0]).reshape((3,1))
O = np.array([0,0,0]).reshape((3,1))

#generating points in Line 
l2_p = line_dir_pt(O-A,A)

#plotting line
plt.plot(l2_p[0,:],l2_p[1,:],l2_p[2,:],label="Line $L_2$")

ax.scatter(O[0],O[1],O[2],'o',label="Point O")
ax.scatter(A[0],A[1],A[2],'o',label="Point A")
ax.scatter(B[0],B[1],B[2],'o',label="Point B")
ax.scatter(B2[0],B2[1],B2[2],'o',label="Point B2")


plt.xlabel('$x$');plt.ylabel('$y$')
plt.legend(loc='best');plt.grid()
#if using termux
#plt.savefig('../figs/1.1.pdf')
#plt.savefig('../figs/1.1.eps')
#subprocess.run(shlex.split("termux-open ../figs/1.1.pdf"))
#else
plt.show()

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from funcs import *
import numpy as np

#if using termux
import subprocess
import shlex
#end if

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
plt.plot([0,l1[0]],[0,l1[1]],[0,l1[2]],label="Direction Vector of B-B2")
plt.plot([0,l2[0]],[0,l2[1]],[0,l2[2]],label="Direction Vector of B2")
plt.plot([0,cp[0]],[0,cp[1]],[0,cp[2]],label="Cross Product Vector")

#printing cross product
print("Cross Product= \n",cp)

#show plot
plt.xlabel('$x$');plt.ylabel('$y$')
plt.legend(loc='best');plt.grid()
#if using termux
#plt.savefig('../figs/2.1.pdf')
#plt.savefig('../figs/2.1.eps')
#subprocess.run(shlex.split("termux-open ../figs/2.1.pdf"))
#else
plt.show()

