#class to find products of and carry out functions upon bijections
#Created by Joel Monroe

#Print versions
	#Cycles are default
	#print(format(object, "biject")) will return in classic notation

#Operations Allowed
	#Multiplication
	#Exponents

#Returnable attributes
	#List of Cycles
	#Classic Bijection
	#Group
	#Order

class Bijection():
	#Initialization
	def __init__(self, group, *elements, type = "cycle"): #Takes disjoint cycles
		#initialize identity element
		self.__group = group
		identity = []
		for i in range(1,group+1):
			identity.append(i)
		self.identity = identity
		
		if type == "cycle":
			#initialize a base list to reference through
			sigma = []
			for i in range(1,group+1):
				sigma.append(i)
	
			#initialize second list where input is a list
			for element in elements:
				for entry in range(len(element)):
					sigma[element[entry] - 1] = element[(entry + 1)%len(element)]
			self.__biject = sigma
		elif type == "biject":
			self.__biject = elements[0]
	
	#Printing 
	def __str__(self): #THIS CODE IS VITAL TO UNDERSTAND -- APPEARS THROUGHOUT
		total = []			                    #Make array to place cycles within
		unvisited = set() 			            #set to indicate unvisited terms
		for i in range(1,self.__group+1):       #fill the set with needed terms
			unvisited.add(i)
		while len(unvisited) > 0:			    #build the cycles by removing visited terms from unvisited
			k = min(unvisited)
			cycle = ()
			while k in unvisited:
				cycle = cycle + (k,)            #Add term into cycle
				unvisited.remove(k)             #Remove visited term from unvisited
				k = self.__biject[k-1]          #Move to the next term using bijection
			total.append(cycle)	                #Add cycle to the array of cycles
		return str(total) + "\n" 
	
	def __print_biject(self):
		#Output in Bijection form
		return str(self.identity) + "\n" + str(self.__biject) + "\n"
	
	def __format__(self, spec):
		if spec == "biject":                    #Allow for bijections to be printed
			return self.__print_biject()
		return str(self).__format__(spec)
	
	#Operations 
	def __mul__(self, other):
		if self.__group != other.__group:       #In case of stupid
			pass
		sigma = Bijection(self.__group)         #New bijection
		for i in range(len(self.__biject)):     #Look through both objects to create new one -- Arrays are amazing
			sigma.__biject[i] = other.__biject[(self.__biject[i] - 1 + self.__group)%self.__group]
		return sigma			
	
	def __pow__(self, n):
		sigma = Bijection(self.__group)
		if n >= 0:                              #Restrict to positive powers
			for i in range(n):                  #Multiply a bunch of times
				sigma = sigma * self            #Does not matter which side you multiply on
			return sigma
		elif n < 0:
			for i in range(self.order() + n):
				sigma = sigma * self
			return sigma
	
	#Attribute returns
	def cycles(self):
		total = []                              #REFERENCE TO __str__ for explanation
		unvisited = set()
		for i in range(1,self.__group+1):
			unvisited.add(i)
		while len(unvisited) > 0:
			k = min(unvisited)
			cycle = ()
			while k in unvisited:
				cycle = cycle + (k,)
				unvisited.remove(k)
				k = self.__biject[k-1]
			total.append(cycle)	
		return total
	
	def biject(self):
		return self.__biject
	
	def group(self):
		return self.__group
	
	def order(self):
		total = []                          #REFERENCE TO __str__ for explanation
		unvisited = set()
		for i in range(1,self.__group+1):
			unvisited.add(i)
		while len(unvisited) > 0:
			k = min(unvisited)
			cycle = ()
			while k in unvisited:
				cycle = cycle + (k,)
				unvisited.remove(k)
				k = self.__biject[k-1]
			total.append(cycle)	
		orders = set()
		for cycle in total:               #Gather the orders of all cycles
			orders.add(len(cycle))        #Utilize the set to only have 1 of every entry
		k = 1
		for i in orders: 
			k = k*i                       #Find the lcm of all of the orders of the cycles 
		return k                          #Return the overall order

	
	#General Functions
	def __verify(self):
		block = set()
		for i in self.__biject:
			if i > 0 and i <= self.__group:
				block.add(i)
		if len(block) == len(self.__biject):
			return True
		else:
			return False