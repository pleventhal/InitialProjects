binary = ''
number = input('What is the Arabic Number: ')

number = int(number)

while number > 0:
	if number % 2 == 0:
		binary = '0' + binary
	else:
		binary = '1' + binary
		number = number - 1

	number = number / 2

print(binary)
