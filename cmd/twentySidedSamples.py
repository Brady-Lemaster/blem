import random
def rollHandler(dice):
  inputList=[]
  outputList=[]
  for i in dice.split('d'): 
    inputList.append(i)
  for i in range(int(inputList[0])):
    outputList.append(random.randint(1,int(inputList[1])))
  return outputList
def x(number):
  dice = rollHandler(number+"d20")
  diceAmount = []
  diceAmount.append(dice.count(1))
  diceAmount.append(dice.count(2))
  diceAmount.append(dice.count(3))
  diceAmount.append(dice.count(4))
  diceAmount.append(dice.count(5))
  diceAmount.append(dice.count(6))
  diceAmount.append(dice.count(7))
  diceAmount.append(dice.count(8))
  diceAmount.append(dice.count(9))
  diceAmount.append(dice.count(10))
  diceAmount.append(dice.count(11))
  diceAmount.append(dice.count(12))
  diceAmount.append(dice.count(13))
  diceAmount.append(dice.count(14))
  diceAmount.append(dice.count(15))
  diceAmount.append(dice.count(16))
  diceAmount.append(dice.count(17))
  diceAmount.append(dice.count(18))
  diceAmount.append(dice.count(19))
  diceAmount.append(dice.count(20))
  return(diceAmount)
