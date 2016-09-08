print "Hello, What do you  want to  bay?"
print "Tshirt  is costs 100"
print "Jeans  is  costs 200"
print "Jacket  is costs 300"
print "But you can have 20% discount if you type more than 500 "
Tshirt = 100
Jeans = 200
Jacket = 300
gTshirt = int(raw_input("How many T-shirt?> "))
gJeans = int(raw_input("How many Jeans?> "))
gJacket = int(raw_input("How many Jacket?> "))
summ1 = (Tshirt*gTshirt) + (Jeans*gJeans) + (Jacket*gJacket)
if summ1 < 500:
	print "Total"
	print summ1 
	money = int(raw_input("How much money do you give?> "))
	if money == summ1:
		print "Everything is paid. Tanks for buying!!!"
	elif money > summ1:
		print "delivery-"
		print money - summ1
		print "Everything is paid. Tanks for buying!!!"
	elif money < summ1:
		print "it is not enough!"
elif summ1 >= 500:
	print "Total"
	print summ1
	print "discount 20%-"
	print summ1 * 9 / 100 
	money = int(raw_input("How money do you give?> "))
	if money == (summ1*0,9):
		print "Everything is paid. Tanks for buying!!!"
	elif money > (summ1*0,9):
		print "delivery-"
		print money - (summ1*0,9)
		print "Everything is paid. Tanks for buying!!!"
	elif money < (summ1*0,9):
		print "it is not enough!"



    

