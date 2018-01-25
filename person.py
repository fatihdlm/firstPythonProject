# Contains Each Person's Information
class Person(object):
	#Constructor yenilendi fatih
	#denene
	def __init__(self,name,age,mail):
		self.name=name
		self.age=age
		self.mail=mail
	
	#Accesser Methods (Getters)
	def getName(self):
		return self.name

	def getAge(self):
		return self.age

	def getMail(self):
		return self.mail

	#Mutator Methods (Setters)
	def setName(self,name):
		 self.name=name
	def setName(self,age):
		 self.age=age
	def setName(self):
		 self.mail=mail
	def __str__(self):
		return "Person[Name :"+self.getName() + \
			",Age :"+self.getAge() + \
			",Email :"+self.getMail() + \
			"]"


def insert_person():
	print("Please Input Person Information")
	name=input("Input Name : ")
	age=input("Input Age : ")	
	mail=input("Input Email : ")
	return Person(name,age,mail)
def show_all_person(person):
	print("Showing All Person")
	for per in person:
		print(per)
def look_up_person(person):
	found=False
	key=input("Please Enter Key: ")
	for per in person:
		if key in per.getName():
			print(per)
			found=True
	if not found:
		print("No Person Match That Term")
def main():
	person=[]
	runing=True
	while runing:
		print("\n Menu")
		print("1-> Insert Person")
		print("2-> Look Up Person")
		print("3-> Show All Person")
		print("4-> Exit")
		option=input(">")
		if option=="1":
			person.append(insert_person())
		elif option=="2":
			show_all_person(person)
		elif option=="3":
			look_up_person(person)
		elif option=="4":
			runing=False
		else:
			print("Unrecognized input, Please Try Again")
	print("Program Ending")
main()

