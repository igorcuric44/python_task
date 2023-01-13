class Category:

	def __init__(self,category):
		self.category=category
		self.balance=0
		self.spend=0
		self.listx=[]
		
	def deposit(self,dictx):
		self.listx.append(dictx)
		self.balance=self.balance+dictx["amount"]
	
	def withdraw(self,dicty):
		if self.check_funds(dicty["amount"]):
			self.spend=self.spend+dicty["amount"]
			dicty["amount"]=(-1)*dicty["amount"]
			self.balance=self.balance+dicty["amount"]
			self.listx.append({"amount":dicty["amount"],"description":dicty["description"]})
			
	
	def get_balance(self):
		return self.balance
		
	def get_spend(self):
		return self.spend
	
	def transfer(self,amount,cat):
		if self.check_funds(amount):
			self.balance=self.balance-amount
			cat.deposit({"amount":amount,"description":"Transfer from "+self.category})
			self.withdraw({"amount":amount,"description":"Transfer to "+cat.category})
			return True
		else:
			return False
		
	
	def check_funds(self,amount):
		if amount>self.balance:
			return False
		else:
			return True
	
	def ispis(self):
		return self.listx
	
	def ispisx(self,obj):
		print(obj.category)
		print(self.category)
		
	def print(self):
		isp=self.listx
		strx="{0:<23s}{1:>7.2f}"
		total=0
		print('{:*^30}'.format(self.category))
		for i in range(len(isp)):
			print(strx.format(isp[i]["description"][:23],isp[i]["amount"]))
			total=total+isp[i]["amount"]
		print('Total: {0:7.2f}'.format(total))

def create_spend_chart(categories):
	lis=[]
	lisp=[]
	
	stringus=""
		
	for objectx in categories:
		lisp.append(objectx.category)
		lis.append(objectx.get_spend())
		

	Sum = sum(lis)

	result=map(lambda x: int(x/Sum*100),lis)

	lis1=list(result)


	result1=list(map(lambda x:100-x,lis1))
	result2=list(map(lambda x:round(x/100,1)*10,result1))


	strxx=[]
	for i in range(0,11):
		strx=""
		for j in range(len(result2)):
			if i<result2[j]:
				strx=strx+"  "
			else:
				strx=strx+" 0"
		strxx.append(strx)


	lispmax=max(lisp,key=len)
	#print(lispmax)
	lenx=len(lispmax)

	lenxx=[]
	for i in range(len(lisp)):
		lenxx.append(lenx-len(lisp[i]))
		lisp[i]=lisp[i]+" "*lenxx[i]

	for i in range(0,11):
		#print("{0:>3d}|{1}".format((10-i)*10,strxx[i]))
		stringus=stringus+"{0:>3d}|{1}".format((10-i)*10,strxx[i])+"\n"
	#print("{0:>13}".format("---------"))
	strtt=[]
	stringus=stringus+"{0:>13}".format("---------")+"\n"
	for i in range(lenx):
		stryy=""
		for j in range(len(lisp)):
			stryy=stryy+lisp[j][i]+" "
		strtt.append(stryy)

	for i in range(lenx):
		#print("{0:>5}{1:>3}".format("",strtt[i]))
		stringus=stringus+"{0:>5}{1:>3}".format("",strtt[i])+"\n"
	
	return stringus
