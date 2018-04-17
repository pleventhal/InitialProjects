array = [['','I','II','III','IV','V','VI','VII','VIII','IX'],
		 ['','X','XX','XXX','XL','L','LX','LXX','LXXX','LC'],
		 ['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM'],
		 ['','M','MM','MMM']]
		 
while True:

	number = input('What is the Arabic Number: ')
	numlength = len(number)
	if int(number) == 0:
		break;

	while numlength < 4:
		number = '0' + number 
		numlength = numlength + 1

	lst = [int(i) for i in str(number)]

	romannumeral = array[3][lst[0]] + array[2][lst[1]] + array[1][lst[2]] + array[0][lst[3]]

	print(romannumeral)
