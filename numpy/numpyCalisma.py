import numpy as np

np.array([2,4,5,9,10])

type(np.array([2,4,5,9,10]))

np.zeros(10,dtype=int)

np.random.randint(0,10,size = 10)

np.random.normal(10,4,(3,4))

a = np.random.randint(10, size = 5)
a.ndim
a.shape
a.size
a.dtype

np.random.randint(1,10,size = 9).reshape(3,3)

a = np.random.randint(10,size = 10)
a[0]
a[0:5]

m = np.random.randint(10,size = (3,5))

m[0,2]

v = np.arange(0,30,3)

v[0]


catch = [1,2,3]

v[catch]


v = np.array([1,2,3,4,5])

ab = []

for i in v:
    if i<3:
        ab.append(i)


v < 3

v[v<3]


v = np.array([1,2,3,4,5])

v / 5
v ** 2

np.subtract(v,1)
np.add(v,1)
np.mean(v)
np.sum(v)
np.min(v)
np.max(v)
np.var(v)


a = np.array([[5,1],[1,3]])
b = np.array([12,10])

np.linalg.solve(a,b)


arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[-3:-1])