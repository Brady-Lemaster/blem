import os
import imp
import requests
class importModule:
  def __init__(self, value):
      self.value = value
  def x(uri, name=None):
    if not name:
      name = os.path.basename(uri).lower().rstrip('.py')
    r = requests.get(uri)
    r.raise_for_status()
    codeobj = compile(r.content, uri, 'exec')
    module = imp.new_module(name)
    exec (codeobj, module.__dict__)
    return module
importModule.x('')



num = s(20)

print(num.myfunc())
