


dinero_banco = 1000
gastos_noche = 4000
soy_gilipollas = True

c1 = dinero_banco >= gastos_noche
c2 = not soy_gilipollas

if(c1 and c2):
    print("    Le gustas a Maria")

if(c1 or c2):
    print("    Le gustas a Pepe")

if((not c1 and c2) or (c1 and not c2)):
    print("    Le gustas a PACOOOLLL")