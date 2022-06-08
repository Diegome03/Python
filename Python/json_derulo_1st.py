import json


x = '''{

"nombre" : "Jason",
"apellido" : "Derulo",
"aka" : "tip toe"


}'''

derulo = json.loads(x)

print(derulo["aka"],derulo["apellido"])
