import random
def rollHandler(dice):
  inputList=[]
  outputList=[]
  for i in dice.split('d'): 
    inputList.append(i)
  for i in range(int(inputList[0])):
    outputList.append(random.randint(2,int(inputList[1])))
  return outputList
def x():
  dice = rollHandler('4d6')
  dice.sort()
  dice.pop(0)
  dice.pop(0)
  rolledDice = []
  rolledDice.append(dice.count(1))
  rolledDice.append(dice.count(2))
  rolledDice.append(dice.count(3))
  rolledDice.append(dice.count(4))
  rolledDice.append(dice.count(5))
  rolledDice.append(dice.count(6))
  return rolledDice
