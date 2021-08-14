print("employee management using dictionary")

#emp=[]
empdict={}
while True:

	print("Enter 1 for add employee ")
	print("Enter 2 for delete employee")
	print("enter 3 for search employee")
	print("enter 4 for change employee data")
	print("enter 5 for display employees")
	print("enter 6 for quite")
	choice=int(input())
	if (choice == 1):
		addid=int(input("Enter Id\t"))
		if addid not in empdict.keys():
			addname=input("Enter name\t")
			addage=int(input("Enter age\t"))
			addgender=input("Gender\t\t")
			addplace=input("Enter place\t")
			addsalary=input("Enter salary\t")
			addpcompany=input("Enter previous company\t")
			addjdate=input("Enter joining data dd/mm/yyyy\t")
			temp={
				"name":addname,
				"age":addage,
				"gender":addgender,
				"place":addplace,
				"salary":addsalary,
				"pcompany":addpcompany
				}
			empdict[addid] = temp
		else:
			print("ID is already in data")
		
#		emp.append(addname)
	elif (choice == 2):
		print(empdict)
		did=int(input("Enter Id\t"))
		del empdict[did]
		print("deleted",empdict)
	elif (choice == 3):
		sname=input("Enter employee name\t")
		for i in empdict.values():
			if i["name"] == sname:
				print(sname,"is found")
		else:
			print(sname, "not in data")
	elif (choice == 4):
		cid=int(input("enter id of employee"))
		if cid in empdict.keys():
			ch=int(input("1 for change name \n 2 for age \n 3 for gender \n 4 for salary"))
			if (ch == 1):
				cname=input("enter new name")
				empdict[cid]['name']=cname
				print(empdict)

			elif (ch == 2):
				cage=input("Enter new age")
				empdict[cid]['age']=cage
				print(empdict)
			elif (ch == 3):
				cgender=input("Enter gender")
				empdict[cid]['gender']=cgender
				print(empdict)
			elif (ch == 4):
				csalary=input("Enter salary")
				empdict[cid]['salary']=csalary
				print(empdict)
			else:
				print("invalid entry")
		else:
			print("wrong employee id")
		#cname=input()
		#i=emp.index(cname)
		#print("enter new name")
		#nname=input()
		#emp[i]=nname
		#print(emp)
	elif (choice == 5):
		print(empdict)
		#a=1
		#for j in emp:
					
	#		print(str(a) + "." + j)
	#		a+=1
		#	aaa=j
			#ind=emp.index[aaa]
		

	elif (choice == 6):
		break;

	else:
		print("invalid entry")

#emp.append("suf")

#print(emp[0])

