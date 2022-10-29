class Rectangle:
	def __init__(self,width,height):
		self.width=width
		self.height=height
    
	def get_area(self):
		return self.width*self.height
  
	def get_perimeter(self):
		return 2*(self.width+self.height)
  
	def set_height(self,height):
		self.height=height
  
	def set_width(self,width):
		self.width=width
	
	def get_diagonal(self):
		return (self.width**2+self.height**2)**.5
	
	def get_amount_inside(self,objectx):
		return  self.get_area()/objectx.get_area()
  
	def get_picture(self):
		y="";
		x="";
		for i in range(0,self.width):
			x=x+"*"
		for j in range(0,self.height):
			y=y+x
			y=y+"\n"
		return y

	def __str__(self):
		return "Rectangle(width="+str(self.width)+", height="+str(self.height)+")"

class Square(Rectangle):
	def __init__(self,side):
		Rectangle.__init__(self,side,side)
		self.side=side
	
	def set_side(self,side):
		self.width=side
		self.height=side
		self.side=side
	

	
	def __str__(self):
		return "Squre(side="+str(self.side)+")"

