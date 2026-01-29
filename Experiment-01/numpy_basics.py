import numpy as np
#1D array
'''a=np.array([1,2,3,4,5])
print(a)
print(a.ndim)
print(a.shape)'''

#0D array
'''a=np.array(10)
print(a)
print(a.ndim)
print(a.shape)'''

#2D array
'''a=np.array([[1,2],[3,4]])
print(a)
print(a.ndim)
print(a.shape)'''

'''a=np.array([[1,2,1],[2,3,2]])
print(a)
print(a.ndim)
print(a.shape)'''

#3D array
'''a=np.array([[[1,2,3],[4,5,6]],
             [[7,8,9],[10,11,12]],
             [[13,14,15],[16,17,18]]])
print(a)
print(a.ndim)
print(a.shape)'''

#indexing
'''print(a[2,0])'''
#negative indexing
'''a=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(a[-2,-3])

a=np.array([[[1,2,3],[4,5,6],[7,8,9]],
            [[10,11,12],[13,14,15],[16,17,18]]])
print(a.shape)
print(a[-1,-1,-2])'''

#slicing
'''a=np.array([1,2,3,4,5])
print(a[1:4])
print(a[2:])
print(a[:3])
print(a[::2])

a=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a[:,1])
print(a[:,-2])
print(a[::2,1])
print(a[::2])

a=np.array([[[1,2,3],[4,5,6]],
             [[7,8,9],[10,11,12]],
             [[13,14,15],[16,17,18]]])
print(a[:,0,1:])'''

#numpy datatypes
'''a=np.array([1,2,3,4,5])
print(type(a))
print(a.dtype)'''
''' i int ,b boolean,u unsignd,f float,c complex, m time ,M datetime, O object, S String, U unicodestring, V void'''
#creating an array with defined data type
'''a=np.array([1,2,3,4],dtype='S')
print(a)
print(a.dtype)'''

#changing the datatype
'''a=np.array([1.1,2.2,3.3])
b=a.astype('i')
print(b)'''

'''a=np.array([1,0,3])
b=a.astype(bool)
print(b)'''

#copy and view
'''a=np.array([1,2,3,4,5])
b=a.copy()
print(a)
print(b)
a[0]=10
print(a)
print(b)
b[1]=20
print(a)
print(b)'''

'''a=np.array([1,2,3,4,5])
b=a.view()
print(a)
print(b)
a[0]=10
print(a)
print(b)
b[1]=20
print(a)
print(b)'''

#Higher dimensional arrays
'''a=np.array([1,2,3,4],ndmin=5)
print(a)
print(a.ndim)
print(a.shape)
print(a[0,0,0,0,3])'''

#Reshaping an array from 1D to 2D
'''a=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
b=a.reshape(2,3,2)
print(b)'''

#Unknown dimension
'''d=a.reshape(2,2,-1)
print(d)
print(d.shape)'''

#Flattening the array
'''a=np.array([[1,2,3],[4,5,6]])
b=a.reshape(-1)
print(b)'''

#numpy array iterating
'''a=np.array([1,2,3])
for i in a:
    print(i)'''
'''a=np.array([[1,2,3],
            [4,5,6]])
for i in a:
    for j in i:
        print(j)'''
'''a=np.array([[[1,2,3],[4,5,6]],
            [[7,8,9],[10,11,12]]])
for i in a:
    for j in i:
        for k in j:
            print(k)'''

#Iterating numpy array using nditer
'''a=np.array([[1,2,3],
            [4,5,6]])
for i in np.nditer(a):
    print(i)'''

#Iterating wih different step size i.e.,2
'''a=np.array([[1,2,3],
            [4,5,6]])
for i in np.nditer(a[:,::2]):
    print(i)'''

#enumerated iteration using ndenumerate
'''a=np.array([[1,2,3],
            [4,5,6]])
for idx,i in np.ndenumerate(a):
    print(idx,i)'''

#joining arrays(putting 2 or more arrays in single array) function - concatenate
'''a1=np.array([1,2,3])
a2=np.array([4,5,6])
a3=np.concatenate((a1,a2))
print(a3)'''

#joining 2D arrays
'''a1=np.array([[1,2],[3,4]])
a2=np.array([[5,6],[7,8]])
a3=np.concatenate((a1,a2))
print(a3)
d=np.concatenate((a1,a2),axis=1)
print(d)'''

#joining 3D arrays
'''a=np.array([[[1,2],[3,4]],
            [[5,6],[7,8]]])
b=np.array([[[9,10],[11,12]],
            [[13,14],[15,16]]])
c=np.concatenate((a,b),axis=0)
print(c)
d=np.concatenate((a,b),axis=1)
print(d)'''

#joining arrays using stack function
'''a=np.array([1,2,3])
b=np.array([4,5,6])
c=np.stack((a,b))
print(c)
print(c.shape)
d=np.stack((a,b),axis=1)
print(d)
print(d.shape)'''

#joining 2D arrays
'''a1=np.array([[1,2],[3,4]])
a2=np.array([[5,6],[7,8]])
a3=np.stack((a1,a2))
print(a3)
print(a3.shape)
a4=np.stack((a1,a2),axis=1)
print(a4)
print(a4.shape)'''

'''a=np.zeros((8,8),dtype='i')
a[::2,::2]=1
print(a)'''



