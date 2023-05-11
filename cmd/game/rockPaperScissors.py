import random
def x(elements, user):
  elementsFigure = elements+elements
  if elements.count(user) > 0:
    botChosen = round(random.randint(1, len(elements)))
    botChosenIndex = botChosen - 1
    if elementsFigure[botChosenIndex - 1] == user:
      print("bot: " + elements[botChosenIndex])
      print("WIN")
      print(botChosenIndex)
    elif elementsFigure[botChosenIndex + 1] == user: 
      print("bot: " + elements[botChosenIndex])
      print("LOSE")
      print(botChosenIndex)
    else:
      print("bot: " + elements[botChosenIndex])
      print("TIE")
      print(botChosenIndex)
  else:
    print("ERROR: " + user + " ELEMENT DOES NOT EXIST")
    print("LOSE")
    print("botChosenIndex")
