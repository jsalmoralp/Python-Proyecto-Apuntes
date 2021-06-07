"""
AND: Eqivalente a "Y si además..."
OR: "O sino..."
not -> negación
"""

distancia = 1200
numeroHermanos = 2
salarioPadres = 1500

tieneBeneficio = False

if (distancia > 1000 and numeroHermanos > 2) or salarioPadres < 2000:
    tiensBeneficio = True

print(not tieneBeneficio)

if (5 > 3) or (8 <6):
    print("Verdad")
else:
    print("Es mentira...")
