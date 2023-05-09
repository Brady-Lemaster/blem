import os
import requests
import types
class default.importModule:
  def x(uri, name=None):
    if not name:
      name = os.path.basename(uri).lower().rstrip('.py')
    r = requests.get(uri)
    r.raise_for_status()
    codeobj = compile(r.content, uri, 'exec')
    module = types.ModuleType(name)
    exec (codeobj, module.__dict__)
    return module
diceUtil = importModule.x('https://raw.githubusercontent.com/Brady-Lemaster/blem/main/package/dicePkg.py')
