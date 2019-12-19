import numpy as np
m=np.array([[2,4,5],[4,6,8],[8,9,20]])
n=np.array([[2,3,1],[2,2,2],[3,7,9]])
print "matrices are \n:","m=\n",m,"\n","n=\n",n
print"size of matrices m,n :","m=\n",m.shape,"\n","n=\n",n.shape
print"inverses of matrices m,n \n:","m=\n",np.linalg.inv(m),"\n","n=\n",np.linalg.inv(n)
print"determinent of matrices m,n \n:","m=\n",np.linalg.det(m),"\n","n=\n",np.linalg.det(n)
print"eigenvalues of matrices m,n \n:","m=\n",np.linalg.eig(m),"\n","n=\n",np.linalg.eig(n)
a=m+n
b=m-n
c=m*n
d=m/n
print"addition of two matrices\n :",a
print"subtraction of two matrices\n:",b
print"multiplication of two matrices\n:",c
print"division of two matrices\n:",d
print"dot product of m,n\n:",m.dot(n)
print"cross product of m,n\n:",np.cross(m,n)


