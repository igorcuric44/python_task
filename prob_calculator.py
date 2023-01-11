from random import randint


class Hat:
	sum=0
	result=list()
	def __init__(self, **kwargs):
		self.dict=kwargs
	
		for key, value in kwargs.items():
			print("%s == %s" % (key, value))
			self.result.append(key)
	
	def number(self):
		print(self.dict)
	
	def number(self):
		for key in self.dict:
			print(key, '->',self.dict[key])
			self.sum=self.sum+self.dict[key]
	
	def total(self):
		return self.sum
	
	def totallist(self):
		return self.result
	
	def draw(self,num_balls_drawn):
		listxx=[]
		listtt=self.result.copy()
		for i in range(num_balls_drawn):
			sum=len(listtt)
			print("///",sum)
			value = randint(0,sum-1)
			
			print(value)
			print("-----",listtt[value])
			listxx.append(listtt[value])
		
		return listxx
			

def experiment(hat,expected_balls,num_balls_drawn,num_experiment):
	print(hat)
	print(hat.draw(num_balls_drawn))
	print(expected_balls)
	print(num_balls_drawn)
	print(num_experiment)
	
	count=0
	
	for _ in range(num_experiment):
		listxx=hat.draw(num_balls_drawn)
		
		counts={}
		for listy in listxx:
			counts[listy]=counts.get(listy,0)+1

		print(counts)
		print(expected_balls)
		
		p=True
		for key,value in expected_balls.items(): 
			if key in counts.keys():
				if	counts[key]>=value:
					print(value," ",key," ",counts[key])
				else:
					print("None")
					p=False
			else:
				print("None")
				p=False
					
		if p:
			print(expected_balls,counts)
			count=count+1
	
	probability=count/num_experiment
	
	return probability

