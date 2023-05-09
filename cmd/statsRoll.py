import random
def rollHandler(dice):
  inputList=[]
  outputList=[]
  for i in dice.split('d'): 
    inputList.append(i)
  for i in range(int(inputList[0])):
    outputList.append(random.randint(1,int(inputList[1])))
  return outputList
def x():
  stats = []
  for i in range(6):
    dice = rollHandler('4d6')
    dice.sort()
    dice.pop(0)
    stats.append(dice[0] + dice[1] + dice[2])
  return stats
