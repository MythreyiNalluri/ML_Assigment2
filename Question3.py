lst = [23, 'Python', 23.98]
list=[]
for element in lst:
   x = type(element)
   list.append(x)
print (str(lst)[1:-1])
print(str(list)[1:-1])