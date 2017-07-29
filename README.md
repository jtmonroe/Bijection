# Bijection Calculator
### Joel Monroe

### The College of William and Mary

File created because of desire to find products of larger cycles. Please use for any projects!

* ## Initiation
* Takes 3 basic arguments of group, a list of cycles or a single bijection, and the input type ("cycle" or "biject")
	* Self.__Biject
		* Bijection objects are initialized as a list. The user input may be either disjoint cycles or a single bijection with references based on the positions in the list (0,1,2,...,n-1 with reference to the 1,2,3,...,n list in a cayley notation bijection).
	* Self.__group
		* Recorded as a private object based on input from user. Used as a test to check if code can find the product of two cycles.
	* Self.identity
		* Identity object for the use of the user. Just in case.

* ## Verify Function
    * Takes the self.__biject object and tests for duplicates and number of elements to prevent poor input.

* ## Printing Options
* By default, printing a bijection object (print(sigma)) will output the disjoint cycles which describe it. 
	* Default: Cycle format
	* Option for bijection, print(format(sigma, "biject"))

* ## Allowed operations
	* Multiplication
		* Operations are non-commutative for non-disjoint cycles. Basic form is _sigma * sigma_. Two bijections in different groups will return _None_ objects. 

		* Operations are non-commutative for non-disjoint cycles. Basic form is _sigma * sigma_. Two bijections in different groups will return _None_ objects. Products of cycles follow the _right to left_ form for notation.
	* Exponentiation
		* Respects positive and negative powers for the bijection. 

* ## Returnable Attributes
	* Cycles
		* Probably some the the most nuanced and interesting code in the module. Takes the list and transfers it into multiple tuples which describes the cycles.
	* Bijection
		* Returns the self.__biject object.
	* Group
		* Retuens the self.__group object.
	* Order
		* Finds the least common multiple of the lengths of the cycles of the bijection. Then returns that as an integer.

* ## General Functions
	* Not yet finished 
