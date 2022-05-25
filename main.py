from random import *
dragon = 0
tiger = 1
counterD = 0
counterT = 0

totalWins = 0
totalLoses = 0

money = 100 #starting balance
bet = 1 #betting 
userBet = 0 #dragon vs tiger comparison, not money
userStatus = bool()
winner = True
loser = False

for counter in range(100000):
    
    randNum = randrange(2)
    
    if userBet == randNum:
        money = money + bet
        userStatus = winner
        
    else:
        money = money - bet
        userStatus = loser
    
    if userStatus == loser and userBet == 0:
        userBet = 1
        
    elif userStatus == loser and userBet == 1:
        userBet = 0
        
    else:
        userBet = userBet

    
    if randNum == 0:
        counterD = counterD + 1
        
    else:
        counterT = counterT + 1
    
if money >= 1000:
    totalWins = totalWins + 1
    
else:
    totalLoses = totalLoses + 1
        
print("Total Dragon Wins: ", counterD,"     Total Tiger Wins: ", counterT)
print("Current balance: $", money)




