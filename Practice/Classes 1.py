

# 2. Implement a class for point in a Cartesian coordinate system. Use this point class to implement a Euclidean vector with methods
# such as addition, scalar multiplication, dot product and cross product. Finally represent the type of linear transformations in the
# Euclidean space as matrices and show the computation of rotation of vectors.

class Cartesian:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def add(self, p2):
		return ((self.x+p2.x,self.y+p2.y))

	def scalar_mult(self, k):
		return ((k*self.x, k*self.y))

	def dot_prod(self, p2):
		return ((self.x*p2.x + self.y*p2.y))

	def cross_prod(self, p2):
		return ((0,0,self.x*p2.y - self.y*p2.x))

	def show(self):
		print(self.x,"i+",self.y,"j")

	def lin_Trans(self, T):
		return ((T[1][1]*self.x + T[1][2]*self.y, T[2][2]*self.y + T[2][1]*self.x))

p=Cartesian(10, 5)
p1=Cartesian(1.1, 5)
p2=Cartesian(5.8, 7)

p.show()
p1.show()
print(p1.add(p2))
print(p1.scalar_mult(21))
print(p1.dot_prod(p2))
print(p1.cross_prod(p2))



# 1. Implement a class for Sets containing integers. Provide methods for set intersection and set union show their time complexity. 

class Sets:
	def __init__(self, lower, upper):
		if lower<=upper:
			self.lower = lower
			self.upper= upper
		else:
			raise ValueError("Invlid Set Bounds")
	def show2(self):
		print("(",self.lower,",",self.upper,")")

	def intersection(self, S2):
		sk = [max(self.lower, S2.lower),min(self.upper, S2.upper)]
		if sk[0]>sk[1]:
			return (())
		elif sk[0]==sk[1]:
			return ((sk[0]))
		else:
			return ((max(self.lower, S2.lower),min(self.upper, S2.upper)))

	def union(self, S2):
		if self.intersection(S2) ==() :
			print((min(self.lower, S2.lower),min(self.upper, S2.upper)),"U",(max(self.lower, S2.lower),max(self.upper, S2.upper)))
		else:
			print((min(self.lower, S2.lower),max(self.upper, S2.upper)))


S1= Sets(2,31)
S1.show2()
S2= Sets(31,71)
S2.show2()
print(S1.intersection(S2))
S1.union(S2)



class Set:
	def __init__(self):
		self.set=[]

	def insert(self, num):
		if num not in self.set:
			self.set.append(num)
		return self.set.sort()

	def union2(self, S2):
		for num in S2:
			if num not in self.set:
				self.set.append(num)
		return self.set.sort()

	def intersection2(self, S2):
		s=[]
		for i in S2:
			if i in self.set:
				s.append(i)
		return s.sort()

	def show3(self):
		print(self.set)


		
# print(0.1+0.2)
# print(0.2+0.4)
# print(0.3+0.6)
# print(0.4+0.8)

class Animal:
	def __init__(self, age):
		self.name = None
		self.age = age
	def get_age(self):
		return self.age
	def get_name(self):
		return self.name
	def set_age(self, new_age):
		self.age=new_age
	def set_name(self, newname=""):
		self.name=newname
	def __str__(self):
		return "Animal:"+str(self.name)+":"+str(self.age)

class cat(Animal):
	def speak(self):
		print("Meow")
	def __str__(self):
		return "cat:"+str(self.name)+":"+str(self.age)

C1=cat(3)
C1.set_name("Sparkles")
print(C1.__str__())




nums = [0,2,0,1,0,3,0,6,0,7,0,3,4,0]
print(list(filter(lambda x:x!=0, nums)))



class Coordinate(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def distance(self, other):
		x_diff_sq = (self.x-other.x)**2
		y_diff_sq = (self.y-other.y)**2
		return (x_diff_sq + y_diff_sq)**0.5
	def __str__(self):
		return "<"+str(self.x)+","+str(self.y)+">"
c = Coordinate(3,4)
print(c)
print(type(c)) #The type of object c is a class Coordinate
print(Coordinate) #A coordinate is a class
print(type(Coordinate)) #A Coordinate class is a type of object
print(isinstance(c, Coordinate)) #Is c an instance of the class Coordinate?
