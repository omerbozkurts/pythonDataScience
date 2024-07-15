kume1 = set(['data','python'])
kume2 = set(['data','function','qcut','lambda','python','miuul'])

if kume1.isdisjoint(kume2):
    print(kume1.intersection(kume2))
else:
    print(kume2.difference(kume1))