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
altStatsRoll = importModule.x('https://raw.githubusercontent.com/Brady-Lemaster/blem/main/cmd/altStatsRoll.py')
altStatsBuild = importModule.x('https://raw.githubusercontent.com/Brady-Lemaster/blem/main/cmd/altStatsBuild.py')
statsRoll = importModule.x('https://raw.githubusercontent.com/Brady-Lemaster/blem/main/cmd/statsRoll.py')
rockPaperScissors = importModule.x('https://raw.githubusercontent.com/Brady-Lemaster/blem/main/cmd/rockPaperScissors.py')
dieRoll = importModule.x('https://raw.githubusercontent.com/Brady-Lemaster/blem/main/cmd/dieRoll.py')
dieSampler = importModule.x('https://raw.githubusercontent.com/Brady-Lemaster/blem/main/cmd/dieSampler.py')
twentySideSample = importModule.x('https://raw.githubusercontent.com/Brady-Lemaster/blem/main/cmd/twentySideData.py')

