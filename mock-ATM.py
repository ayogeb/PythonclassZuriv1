name = input("What is your name? \n")
allowedUsers = ['Ayoge','UGB','SUB']
allowedPassword = ['password1','password2','password3']


if(name in allowedUsers):
    password = input("Your password? \n")
    userId = allowedUsers.index(name)

    if(password == allowedPassword[userId]):
        print('Welcome %s' %name)
        print('These are the available options')
        print('1. Withdrawal')
        print('2. Cash Deposit')
        print('3. Complaint')

        selectedOption = int(input('Please select an option: \n'))
        if(selectedOption == 1):
            print('You have slected option %s' %selectedOption)
            withdrawAmount = int(input('How much would you like to withdraw? \n'))
            print('You have chosen to withdraw %d' %withdrawAmount)
            print('Take your cash')
            
        elif(selectedOption == 2):
            print('You have slected option %d' %selectedOption)
            depositAmount = int(input('How much would you like to deposit? \n'))
            print('You have chosen to deposit %d' %depositAmount)
            print('Place the notes in the receiver tray')
            previousBalance = 2000
            currentBalance = previousBalance + depositAmount
            print('Your current balance is %d' %currentBalance)
           
        elif(selectedOption == 3):
            print('You have selected option %s' %selectedOption)
            complaint = input('What issue would you like to report? \n')
            print('Thank you for contacting us.')

        else:
            print('Invalid option selected, please try again')
            
    else:
        print('Password Incorrect, please try again')

else:
    print('Name not found, please try again')


