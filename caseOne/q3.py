listA = ['D','A','T','A','S','C','I','E','N','C','E']

print(len(listA))

print(listA[0], listA[10])

newList = []
newList.append(listA[0])
newList.append(listA[1])
newList.append(listA[2])
newList.append(listA[3])
print(newList)


listA.pop(8)
print(listA)

listA.append('X')

listA.insert(8,'N')
print(listA)