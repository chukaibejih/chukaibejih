import time
import datetime

print('********************************************************** \n EAZY BANKING \n**********************************************************')
time.sleep(2)
username = str(input("\nPlease enter your username: "))
account_names = ['Danny', 'Kate', 'Prince','Happy', 'Rita', 'Chukwuka']
account_passwords = ['danxyz', 'katiexyz', 'princixyz', 'happiexyz', 'ritxyz', 'chukaxyz']
current_balance = 800

if (username in account_names):
	password = input("\nPassword: ")
	userid = account_names.index(username)

	if (password == account_passwords[userid]):
		print("\nGood Day {}".format(username))
		login_time = datetime.datetime.now()
		print ("\nLogged in : ")
		print (login_time.strftime("%Y-%m-%d %H:%M:%S"))

		time.sleep(2)
		print("\n What action would you like to perform?")
		time.sleep(1)
		print("1. Withdraw")
		time.sleep(1)
		print("2. Deposit")
		time.sleep(1)
		print("3. Complaint")	

		selected_option = int(input("Please select an option: "))

		if (selected_option == 1):

			print("Your current balance is ${}".format(current_balance))
			time.sleep(2)
			withdraw = int(input("How much would you like to withdraw "))
			if withdraw > current_balance:
				print("Insufficient Fund")
			else:	
				print("Take your cash")
				time.sleep(2)
				new_balance = current_balance - withdraw
				print("Your new balance is ${}".format(new_balance))

		elif (selected_option == 2):

			print("Your current balance is ${}".format(current_balance))
			time.sleep(2)
			deposit = int(input("How much would you like to deposit? "))
			print("Transaction successful")
			time.sleep(2)
			new_balance = current_balance + deposit
			print("Your new balance is ${}".format(new_balance))


		elif (selected_option == 3):
			input("What issue will you like to report?")
			print("Thank you for contacting us")

		else:
			print("Action can not be performed")
		
	else:
		print("Password incorrect, please try again")

else:
	print("Username not found")
	

	
	

	