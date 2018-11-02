#https://stackoverflow.com/questions/18412179/reading-a-file-and-storing-values-into-variables-in-python
file = open('elements.csv')
for line in file:
	element=line.readline()
	part = line.split(',')
	print (part[0],part[1])
'''first = f.readline()
second = f.readline()
print(first,second)'''