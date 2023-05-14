import os
import requests
import types
import random 
class dieRoll:
  def x(dice):  inputList=[] 
    outputList=[] 
    for i in dice.split('d'): 
      inputList.append(i) 
    for i in range(int(inputList[0])):
      outputList.append(random.randint(1,int(inputList[1]))) 
    return outputList 
class importModule:
  def x(uri, name=None):
    if not name:
      name = os.path.basename(uri).lower().rstrip('.py')
    r = requests.get(uri)
    r.raise_for_status()
    codeobj = compile(r.content, uri, 'exec')
    module = types.ModuleType(name)
    exec (codeobj, module.__dict__)
    return module
class altStatsBuild:
  def x(rolledDice, die1, die2, die3): 
    if rolledDice[die1-1] > 0 and rolledDice[die2-1] > 0 and rolledDice[die3-1] > 0:
      rolledDice[die1-1] = rolledDice[die1-1]-1
      rolledDice[die2-1] = rolledDice[die2-1]-1 
      rolledDice[die3-1] = rolledDice[die3-1]-1
      stat = die1 + die2 + die3 
      return(rolledDice, stat) 
    else:
      return(rolledDice, "error") 
class altStatsRoll:
  def x():
    dice = rollHandler('20d6')
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
class chatManager:
  def x(profile, element, content): 
    if profile == None: 
      profile = ["ada", 1, 1000, "placeholderKey"]
    if element == "model":
      profile[0] = content 
    elif element == "random": 
      profile[1] = content 
    elif element == "limit":
      profile[2] = content
    elif element == "key": 
      profile[3] = content 
    else:
      print("ERROR: ELEMENT NOT FOUND")
    return(profile)
class chatProfile:
  x = ["text-davinci-003", 0, 5, "placeholderKey"]
