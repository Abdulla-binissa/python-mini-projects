import random, string

def generate(passLength, reqUppercase, reqNumber, reqSpecial):
    reqs = [reqUppercase, reqNumber, reqSpecial]
    counter = 0
    password = ''
    
    while(True):
        rand = random.randint(0, 3)
        counter += 1
        if( rand == 0 and reqs[0] != 0):
            password += random.choice(string.ascii_uppercase) 
            reqs[0] -= 1
        elif( rand == 1 and reqs[1] != 0):
            password += random.choice(string.digits) 
            reqs[1] -= 1
        elif( rand == 2 and reqs[2] != 0):
            password += random.choice(string.punctuation) 
            reqs[2] -= 1
        else:
            password += random.choice(string.ascii_lowercase) 

        if( counter > 8 and sum(reqs) == 0 ): break
    
    return password
        
while(True):

## Step 1: Ask user for requirements
# Idea 1: Ask user to input Y/N for common requirements:
    print('\nChoose your requirements: ')
    # req 1: One uppercase letterr?
    while(True):    
        try: reqUppercase = int(input('How many uppercase letters?: '))
        except: reqUppercase = 0 
        if(not reqUppercase in range(0, 32)): print('\nEnter a number between 0 and 32')
        else: break
    # req 2: One numeric character?
    while(True):
        try: reqNumber = int(input('How many numbers?: '))
        except: reqNumber = 0 
        if(not reqNumber in range(0, 32)): print('\nEnter a number between 0 and 32')
        else: break
    # req 2: One special character{!, @, #, $, %, ^, &, *}?
    while(True): 
        try: reqSpecial = int(input('How many special characters?: '))
        except: reqSpecial = 0 
        if(not reqSpecial in range(0, 32)): print('\nEnter a number between 0 and 32')
        else: break
    # req 3: Length (between two ints?) ? [numeric input not Y/N]
    # req 4: ...

    # Idea 2: Ask user for a word to base on
        # Example: random => R@nd0m 

    ## Step 2: Generate password
    while(True):
        #length 8 - 12
        reqLength = reqUppercase + reqNumber + reqSpecial

        passLength = reqLength if (reqLength > 8) else 8
        passLength += random.randint(1,5)

        print('\nThis is your password: ', generate(passLength, reqUppercase, reqNumber, reqSpecial))

        ## Step 3: Allow user to generate different paswords with same requirements
        while(True):
            try: answer = input("Would you like another one? (Y/N): ")
            except: answer = ''
            if (answer.lower() == 'y' or answer.lower() == 'n'): break
            else: print("\nEnter 'Y' for yes or 'N' for no.")
        if( answer.lower() == 'n' ): break

    ## Step 4: Allow user to generate different paswords with different requirements
    while(True):
        try: answer = input("\nOkay. Would you like to choose different requirements? (Y/N): ")
        except: answer = ''
        if (answer.lower() == 'y' or answer.lower() == 'n'): break
        else: print("\nEnter 'Y' for yes or 'N' for no.")
    if( answer.lower() == 'n' ): break

print('\nThank you!')