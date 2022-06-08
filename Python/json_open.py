import json


with open('json_solotexto.py', 'r') as f:
    x = f.read()


mi_derulo = json.loads(x)


print(mi_derulo["nombre"], mi_derulo["apellido"], mi_derulo["aka"])
