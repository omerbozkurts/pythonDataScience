a = 5

b = 4

multiple = lambda c,d : c*d


print(multiple(a,b))


salaries = [34000,23492,52391,39191,59318]


def newSalary(x):
    return round(x * 1.2,2)

print(newSalary(500))


for salary in salaries:
    print(newSalary(salary))


print(list(map(newSalary, salaries)))


salaries = [34000,23492,52391,39191,59318]

print(list(map(lambda x : round(x*1.2,2), salaries)))


listA = [1,5,12,51,3,745,32,15,16,83,92]

print(list(filter(lambda x : x % 2 == 0 , listA)))



from functools import reduce

listB = [1,2,3,4,5]

print(reduce( lambda a,b : a+b,listB))