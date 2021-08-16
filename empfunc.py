print("employee management")

emp=[]
empdict={}
groups={}
def manage_all_group_menu():
	print("\t 1 for create group")
	print("\t 2 for display group")
	print("\t 3 for manage group")
	print("\t 4 for delete group")
	print("\t 5 for Exit")
def create_group():
	gname=input("Enter group name")
	groups[gname] = []
	
def delete_group():
	group_name = input("\tEnter group name ")
	if group_name in groups.keys():
		del groups[group_name]
		print("\tDeleted the group")
	else:
		print("\tWrong group name")
def display_group():
	for key,value in groups.items():
		name_string = ""
		for i in value:
			name_string = name_string + "|" + empdict[i]["name"]
		print(f"{key} => {name_string}")

def manage_group_menu():
	print("\t\t1.Add Member")
	print("\t\t2.Delete Member")
	print("\t\t3.List Members")
#	print("\t\t4.Exit")
	

def manage_group():
	group_name = input("\t\tEnter group name ")
	manage_group_menu()
	ch = int(input("\t\t Enter your Choice "))
	if ch == 1:
		#Add member
		add_member(group_name)
	elif ch == 2:
		#Delete member
		delete_member(group_name)
	elif ch == 3:
		#List member
		list_member(group_name)
	else:
		print("\tInvalid choice")	
	
def add_member(group_name):
#	display_student()
	print(empdict)
	serial_no = int(input("\t\tEnter the serial no of employee "))
	if serial_no in empdict.keys():
		groups[group_name].append(serial_no)
	else:
		print("\t\tWrong serial No.")

def list_member(group_name):
	name_string=""
	for i in groups[group_name]:
		name_string = name_string +"|"+i+"."+empdict[i]["name"]
	print(f"{name_string}")

def delete_member(group_name):
	list_member(group_name)
	serial_no = input("\t\tEnter serial no from list")
	if serial_no in groups[group_name]:
		groups[group_name].remove(serial_no)
	else:
		print("\t\tWrong serial No.")

def manage_all_groups():
	while True:
		manage_all_group_menu()
		c= int(input("\t Enter choice"))
		if c == 1:
			create_group()
		elif c == 2:
			display_group()
		elif c == 3:
			manage_group()
		elif c == 4:
			delete_group()
		elif c == 5:
			break;
		else:
			print("invalid entry")

while True:

	print("Enter 1 for add employee ")
	print("Enter 2 for delete employee")
	print("Enter 3 for search employee")
	print("Enter 4 for channge employee data")
	print("Enter 5 for display employees")
	print("Enter 6 for Manage Teams")
	print("Enter 7 for quite")
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
			empdict[addid]={
				"name":addname,
				"age":addage,
				"gender":addgender,
				"place":addplace,
				"salary":addsalary,
				"pcompany":addpcompany
				}
			#empdict[addid] = temp
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
				cgender("Enter gender")
				empdict[cid]['gender']=cgender
				print(empdict)
			elif (ch == 4):
				csalary("Enter salary")
				empdict[cid]['salary']=csalary
				print(empdict)
			else:
				print("invalid entry")
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
		manage_all_groups()
	elif (choice == 7):
		break;
	else:
		print("invalid entry")

#emp.append("suf")

#print(emp[0])

