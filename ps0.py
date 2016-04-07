def is_even(number):
	if number / 2 == 0:
		return "Even"
	else:
		return "Odd"
	
def number_digits(number):
	counter = 0
	while number > 0:
		number /= 10
		counter+=1
	return counter

def sum_digits(number):
	sum = 0
	while number > 0:
		sum += (number % 10)
		number /= 10
	return sum

def sum_less_ints(x):
	y = 1
	z = 0
	while x > 0:
		x -= y			
		z += x
	return z

def factorial(x):
	y = 0
	z = 1
	while y < x:
		y += 1			
		z *= y
	return z

def divisibility(x, y):
	if y % x == 0:
		return True
	else:
		return False

def prime(x):
	y = 2
	while x > y:
		if x % y == 0:
			return False
		else:
			y += 1
	if y == x:
		return True

def perfect(x):
	index = 1
	count = 0
	while x > index:
		if x % index == 0:
			count += index
			index += 1
		else:
			index += 1
	if count == x:
		return True
	else:
		return False


def sum_digits_divisible(x):
	if x % sum_digits(x) == 0:
		return True
	else:
		return False

def reverse_digits(x):
	length = 10 ** ((num_digits(x)) - 1)
	y = 1
	sum = 0
	while length != 0:
		z = 0
		while x > length or x == 1:
			x -= length
			z += 1
		if length == 1 and z == 10:
			z -= 1
		sum += z * y
		y *= 10
		length /= 10
	return sum