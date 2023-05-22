import os
import requests
import types
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
dieRoll = importModule.x('https://raw.githubusercontent.com/Brady-Lemaster/blem/main/cmd/dieRoll.py')
dieSampler = importModule.x('https://raw.githubusercontent.com/Brady-Lemaster/blem/main/cmd/dieSampler.py')
twentySideSample = importModule.x('https://raw.githubusercontent.com/Brady-Lemaster/blem/main/cmd/twentySideData.py')
altStatsRoll = importModule.x('https://raw.githubusercontent.com/Brady-Lemaster/blem/main/cmd/altStatsRoll.py')
altStatsBuild = importModule.x('https://raw.githubusercontent.com/Brady-Lemaster/blem/main/cmd/altStatsBuild.py')
statsRoll = importModule.x('https://raw.githubusercontent.com/Brady-Lemaster/blem/main/cmd/statsRoll.py')
rockPaperScissors = importModule.x('https://raw.githubusercontent.com/Brady-Lemaster/blem/main/cmd/rockPaperScissors.py')
chatbot = importModule.x('https://raw.githubusercontent.com/Brady-Lemaster/blem/main/cmd/chatbot.py')
imageGen = importModule.x('https://raw.githubusercontent.com/Brady-Lemaster/blem/main/cmd/imageGen.py')
chatbot2 = importModule.x('https://raw.githubusercontent.com/Brady-Lemaster/blem/main/cmd/chatbot2.py')
imageGen2 = importModule.x('https://raw.githubusercontent.com/Brady-Lemaster/blem/main/cmd/imageGen2.py')
imageProfile = importModule.x('https://raw.githubusercontent.com/Brady-Lemaster/blem/main/cmd/imageProfile.py')
imageManager = importModule.x('https://raw.githubusercontent.com/Brady-Lemaster/blem/main/cmd/imageManager.py')
chatProfile = importModule.x('https://raw.githubusercontent.com/Brady-Lemaster/blem/main/cmd/chatProfile.py')
chatManager = importModule.x('https://raw.githubusercontent.com/Brady-Lemaster/blem/main/cmd/chatManager.py')
chatbot3 = importModule.x('https://raw.githubusercontent.com/Brady-Lemaster/blem/main/cmd/chatbot3.py')
chatHistory = importModule.x('https://raw.githubusercontent.com/Brady-Lemaster/blem/main/cmd/chatHistory.py')
fileToList = importModule.x('https://raw.githubusercontent.com/Brady-Lemaster/blem/main/cmd/fileToList.py')
listToFile = importModule.x('https://raw.githubusercontent.com/Brady-Lemaster/blem/main/cmd/listToFile.py')
dan = importModule.x('https://raw.githubusercontent.com/Brady-Lemaster/blem/main/cmd/dan.py')
dieRoll2 = importModule.x('https://raw.githubusercontent.com/Brady-Lemaster/blem/main/cmd/dieRoll2.py')
bitIntLimit = importModule.x('https://raw.githubusercontent.com/Brady-Lemaster/blem/main/cmd/bitIntLimit.py')
