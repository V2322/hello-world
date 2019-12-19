list1=[]
list2=[]
l=input("enter length of list1:")
for i in range(l):
	lis=input("enter elements of list1:")
	list1.append(lis)
print "elements of list1 is ",list1
l2=input("enter length of list2:")
for i in range(l2):
	lis=input("enter elements of list2:")
	list2.append(lis)
print"elements of list2 is ",list2
list2.append(list1)
print"appending of lists",list2
for i in range(l2):
	if(list2[i]%2==0):
		list1.append(list2[i])
print "appending only even elements of list2 to list1 is",list1


