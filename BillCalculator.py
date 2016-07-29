
def tip(bill_amount, tip_percentage):
	return bill_amount * tip_percentage

def total_bill(bill_amount, tip):
	return bill_amount + tip

def split_bill(total_bill_dollars, number_of_people):
	return total_bill_dollars / number_of_people

# print tip(50.00, .10)

def main():
	
	tip_percentage = 0.10

	bill_amount = float(raw_input("What is your bill amount?"))

	print bill_amount

	choice = int(raw_input("Enter 1 to Calculate the Tip or Enter 2 to Split the bill"))
	if (choice == 1):
		print tip(bill_amount,tip_percentage)
	else:
		number_of_people = int(raw_input("How many people are in your party?"))
		total_bill_amount = tip(bill_amount, tip_percentage) + bill_amount
		print split_bill(total_bill_amount, number_of_people)



if __name__ == '__main__':
   main()