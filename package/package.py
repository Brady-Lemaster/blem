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
dieRoll = importModule.x('https://raw.githubusercontent.com/Brady-Lemaster/blem/main/cmd/dice/dieRoll.py')
dieSampler = importModule.x('https://raw.githubusercontent.com/Brady-Lemaster/blem/main/cmd/dice/dieSampler.py')
twentySideSample = importModule.x('https://raw.githubusercontent.com/Brady-Lemaster/blem/main/cmd/dice/twentySideData.py')
altStatsRoll = importModule.x('https://raw.githubusercontent.com/Brady-Lemaster/blem/main/cmd/dnd/altStatsRoll.py')
altStatsBuild = importModule.x('https://raw.githubusercontent.com/Brady-Lemaster/blem/main/cmd/dnd/altStatsBuild.py')
statsRoll = importModule.x('https://raw.githubusercontent.com/Brady-Lemaster/blem/main/cmd/dnd/statsRoll.py')
rockPaperScissors = importModule.x('https://raw.githubusercontent.com/Brady-Lemaster/blem/main/cmd/game/rockPaperScissors.py')
chatbot = importModule.x('https://raw.githubusercontent.com/Brady-Lemaster/blem/main/cmd/gpt/chatbot.py')


