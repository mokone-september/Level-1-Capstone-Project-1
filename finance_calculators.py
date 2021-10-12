import math


# Code to input() user selection, provided also is the user instruction.

user_selection = str(input("Choose either 'investment' or 'bond':\n \n investment \t - to calculate the amount of interest you'll earn on interest \n bond \t\t - to calculate the amount you'll have to pay on a home loan: \n\n")).lower()

# Code to determine user selection if "investment" was selected, a series of input() questions is asked with each variable stored as an interger. After the correct input() from the user a "Correct" Emoji is printed()
# Please note that math.floor() functions have been used for final sum and output to user, for result accuracy purposes. 

if user_selection == "investment" :
	invest_depo = int(input('Enter the amount of money that you will be depositing: \n\n'))
	print(u'\t\u2713\n', f'\n You have selected to Deposit R{float(invest_depo)}\n')
	
	invest_inter = int(input('Enter your interest rate, numerical value only: \n\n'))
	print(u'\t\u2713\n', f'\n You have selected the Interest Rate of {invest_inter}%\n')
	
	invest_years = int(input('Enter the numbers of years that you plan on investing for: \n\n'))
	print(u'\t\u2713\n', f'\n You have selected {invest_years} years to invest for\n')

# Code to determine simple or compound interest from the user and performing all necessary calculations based on user selection.
	
	interest = str(input("Choose either 'simple' or 'compound' interest for you investment:\n\n\n simple interest \t\t - is continually calculated on the initial amount invested and is only calculated once per year. \n compound interest \t - is different in that the interest is calculated on the current total known as the accumulated amount: \n\n")).lower()
	
	if interest == "simple" :
		interest_cal = invest_inter / 100
		invest_type = invest_depo * (1 + interest_cal * invest_years)
		print(f'\t\tFinal Investment At Maturity: \n\t\t\tR{float(math.floor(invest_type))}')
	
	elif interest == "compound" :
		interest_cal = invest_inter / 100
		invest_type = invest_depo * math.pow((1 + interest_cal),invest_years)
		print(f'\t\tFinal Investment At Maturity: \n\t\t\tR{float(math.floor(invest_type))}')
		
# Code to notify user of an invalid entry
		
	else:
		print("Invalid Entry, Type and Choose either 'simple' or 'compound'") 

# Code to determine user selection if "bond" was selected, a series of input() questions is asked with each variable stored as an interger. After the correct input() from the user a "Correct" Emoji is printed()

elif user_selection == "bond" :
	bond_value = int(input('Enter the present value of the house: \n\n'))
	print(u'\t\u2713\n', f'\n The Value of the house is R{float(bond_value)}\n')
	
	bond_inter = int(input('Enter the interest rate, numerical value only: \n\n'))
	print(u'\t\u2713\n', f'\n The Interest Rate selected is {bond_inter}%\n')
	
	bond_months = int(input('Enter the number of months that you plan on repaying the bond: \n\n'))
	print(u'\t\u2713\n', f'\n You have selected {bond_months} months to repay the bond\n')

# Code performing all necessary calculations based on user selection for bond repayment.
# Please note that math.ceil() functions have been used for final sum and output to user, for result accuracy purposes. 

	total_months = 12
	interest_formula_bond = bond_inter / 100
	monthly_interest_rate = (interest_formula_bond) / total_months
	bond_cal = bond_value * ((monthly_interest_rate * ((monthly_interest_rate + 1) ** bond_months)) / (((monthly_interest_rate + 1) ** bond_months)-1))
	print(f'\t\tYour monthly repayment will be: \n\t\t\tR{float(math.ceil(bond_cal))}')
	
	

# Code to notify user of an invalid entry

else:
        print("Invalid Entry, Type and Choose either 'investment' or 'bond'")
        
        
	

