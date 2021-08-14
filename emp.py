print("employee management")

emp=[]

while True:

	print("Enter 1 for add employee ")
	print("Enter 2 for delete employee")
	print("enter 3 for search employee")
	print("enter 4 for change employee data")
	print("enter 5 for display employees")
	print("enter 6 for quite")
	choice=int(input())
	if (choice == 1):
		print("enter employee name :")
		addname=input()
		emp.append(addname)
	elif (choice == 2):
		print(emp)
		print("enter name for delete :")
		dname=input()
		emp.remove(dname)
		print("deleted",emp)
	elif (choice == 3):
		print("enter name to search")
		sname=input()
		if sname in emp:
			print(sname,"is found")
		else:
			print(sname, "not in data")
	elif (choice == 4):
		print("enter name for change")
		cname=input()
		i=emp.index(cname)
		print("enter new name")
		nname=input()
		emp[i]=nname
		print(emp)
	elif (choice == 5):
		a=1
		for j in emp:
					
			print(str(a) + "." + j)
			a+=1
		#	aaa=j
			#ind=emp.index[aaa]
		

	elif (choice == 6):
		break;
	else:
		print("invalid entry")

#emp.append("suf")

#print(emp[0])

