import os
import imp
import requests
class importModule:
  def x(uri, name=None):
    if not name:
      name = os.path.basename(uri).lower().rstrip('.py')
    r = requests.get(uri)
    r.raise_for_status()
    codeobj = compile(r.content, uri, 'exec')
    module = imp.new_module(name)
    exec (codeobj, module.__dict__)
    return module
importModule.x('https://raw.githubusercontent.com/Brady-Lemaster/brady-Lemaster.github.io/main/py/miniroll.py')

