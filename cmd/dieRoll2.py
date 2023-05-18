import random, math
def x(dice):
  inputList=[]
  outputList=[]
  for i in dice.split('d'):    inputList.append(i) 
  for i in range(int(inputList[0])):
    outputList.append(random.randint(1,int(inputList[1])))
  total = 0
  for i in range(len(outputList)):
    total = total + outputList[i]
  rQG = total / len(outputList)
  rQG = rQG / int(dice.split('d')[1])
  rQG = math.floor(rQG * 50)
  return rQG, outputList
