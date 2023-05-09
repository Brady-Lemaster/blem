import os
import requests
import types
name = None
uri = 'https://raw.githubusercontent.com/Brady-Lemaster/blem/main/package.py'
types.ModuleType('name')
if not name:
  name = os.path.basename(uri).lower().rstrip('.py')
r = requests.get(uri)
r.raise_for_status()
codeobj = compile(r.content, uri, 'exec')
module = types.ModuleType(name)
exec (codeobj, module.__dict__)
