print("Welcome to the Python Airlines Prototype Membership System\n ")
 
# Asking the user to input information about their annual and lifetime metrics,information about their next/upcoming flight
firstName = input("What is your first name? ")
annualMiles = int(input("How many miles have you flown this year? "))
annualSegments = int(input("How many segments have you flown this year? "))
annualDollars = float(input("How much money have you spent this year (USD)? "))
lifetimeMiles = int(input("How many lifetime miles have you flown? "))
loungeCheck = input("Is your next flight to (or through) the Chicago airport? ").lower()
ticketPrice = float(input("How much will a Coach Class ticket for your next flight cost (USD)? "))

#printing blank line
print()

#Initializing variables
membership = ""  
lifetimeMembership = ""
lounge = 0

#Checking membership tier
if annualMiles >= 100000 or (annualSegments >= 120 and annualDollars >= 24000):
    membership = "Diamond"
    bags = 3
    upgrades = "First Class"
    discount = 0.3
    lounge = 1

elif annualMiles >= 75000 or (annualSegments >= 90 and annualDollars >= 15000):
    membership = "Ruby"
    bags = 2
    upgrades = "First Class"
    discount = 0.25

elif annualMiles >= 50000 or (annualSegments >= 60 and annualDollars >= 7000):
    membership ="Emerald"
    bags = 1
    upgrades = "Business Class"
    discount = 0.20
        
elif annualMiles >= 25000 or (annualSegments >= 30 and annualDollars >= 3000):
    membership = "Sapphire"
    bags = 0
    upgrades = "Business Class"
    discount = 0.15

#Checking lifetime membership tier
if lifetimeMiles >= 3000000:
    lifetimeMembership = "Diamond"
    # Managing Rewards
    bags = 3
    upgrades = "First Class"
    discount = 0.3
    lounge = 1

elif (lifetimeMiles >= 2000000):
    lifetimeMembership = "Ruby"
    # Managing Rewards to make changes if a person is eligible for a higher yearly membership reward
    if (annualMiles < 75000):
        bags = 2
        upgrades = "First Class"
        discount = 0.25
        
elif (lifetimeMiles >= 1000000):
    lifetimeMembership = "Emerald"
    # Managing Rewards to make changes if a person is eligible for a higher yearly membership reward
    if (annualMiles < 50000):
        bags = 1
        upgrades = "Business Class"
        discount = 0.20

#Displaying an input summary of the input values.    
print('{}, this year, you have flown {} flights for {:,} miles and spent ${:.2f} USD with Python Airlines. Lifetime, you have flown {:,} miles.\n'.format(firstName,annualSegments,annualMiles,annualDollars,lifetimeMiles))

#If the user has achieved a lifetime membership tier, display
if lifetimeMembership!="":
    print("You have achieved lifetime frequent-flier status at the {} level!".format(lifetimeMembership))
#If a lifetime membership user also achieves a higher-level, annual membership tier, display:
    if ((lifetimeMembership=='Ruby'or lifetimeMembership=='Emerald')and membership=='Diamond') or (lifetimeMembership=='Emerald'and membership=='Ruby'):
        print('This year, you have also achieved annual frequent-flier status at the {} level!'.format(membership))
                         
#If the user only achieves an annual membership tier (not lifetime), display:
if (membership!="") & (lifetimeMembership==""):
    print('This year, you have achieved annual frequent-flier status at the {} level!'.format(membership))

#If the user has failed to achieve both an annual and lifetime membership tiers, display:
if(lifetimeMembership=="")&(membership==""):
    print("You are on your way to achieving annual frequent-flier status with Python Airlines!")


print()


#Membership elidgibility
if lifetimeMembership or membership:
    print("You have unlocked the following rewards:")
#Check if there any any add on bags allowed
    if bags:
        print("- {} free checked bags per flight".format(bags))
# Upgrade seats
    print("- Free seat upgrades to First Class".format(upgrades))
# Is there lounge access?
    if lounge:
        if loungeCheck=="yes" or loungeCheck=="y":
            print('- Enjoy free access to the club lounge in Chicago on your next/upcoming flight!')
        else:
            print('- Free access to the club lounge next time flying to/through in Chicago')
# price after discount
    print('- Your upcoming flight ticket price of ${:.2f} USD was reduced by {}% to ${:.2f} USD.'.format(ticketPrice,int(discount*100),(1-discount)*ticketPrice))









