# Peter Madin 03
# 5/25/20
# Retirement_Planning_V2
#
# This progam creates a table using the users input as savings
# after that a preset amount of interest and age is calcuated for them

# CSC 110

def main():
    
    ## Obtains And Validates Inputs
    
    print('Welcome User to the retirement plannting tool!')
    annual_limit = int(input('\nEnter annual savings (at least $100): $'))
    while annual_limit < 100:
        annual_limit = int(input('Try again (Annual savings must be >= $100): $'))
        
    amount_saved = annual_limit # initialize staring value
    
    ## Header
    print('Retirement Savings Table:')
    print('\nStarting     Assumed Interest Rate')
    print('  Age           4%           6%           8%          10%')

    ## Neasted Loops
    #  The first set of loops creates the age list and prints
    #  them plus it assigns the age for calc_final_balance.
    #  the seoond loop gets it interest assigned for calc_final_balance
    for age in range(20, 70, 5):
        print(format(age, '5.0f'), end ='') # initialization
        starting_age = age # assigns age through loop
        for interest in range(4, 11, 2):
            interest_rate = interest # assigns interest through loop
            print('  $' + format(calc_final_balance(starting_age, amount_saved, interest_rate),'10.2f'), end ='')
        print()

    print('\nWhen are You going to start saving for retiremeint?')

## Function calculates the final balance until target age of 70 is reached
def calc_final_balance(starting_age, amount_saved, interest_rate):
    ## Stimulates retirement changes until target age of 70

    age = starting_age # initialize counter
    balance = 0 # initialize starting balance
    interest_rate = float((interest_rate) / 100) # converts interest rate to decimal
    interest_rate += 1 # yearly increase of interest_rate 


    # loop contains buffer for logical savings
    while age < 70 and age >= 18: # loop for each year
        age = age + 1#age += 1 # iterates the age until age 70
        balance += amount_saved
        balance *= interest_rate # gets the interest rate per year and multiplies
    return balance#returns the final calulated balance

main()

## DOCUMENTATION
#
## TEST 01
# Input: $3000
# Output: Age 60 with 4% = $37459.05
#         Age 65 with 10% = $20146.83
#
## TEST 02
# Input: $420
# Output: Age 60 with 4% = $5244.27
#         Age 65 with 10% = $2820.56
#
## TEST 03
# Input: $1337
# Output: Age 60 with 4% = $16694.25
#         Age 65 with 10% = $8978.77

# Tested input were calculated and verified by hand
