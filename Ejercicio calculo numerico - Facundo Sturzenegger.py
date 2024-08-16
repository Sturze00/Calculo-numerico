students = [
    {"nombre": "Jose", "notas": [85, 90, 78, -10]},
    {"nombre": "Carlos", "notas": [88, 72, 94, 102]},
    {"nombre": "Maria", "notas": [95, 85, 87, "A++"]}
]

for i in students:
    acum = 0
    error = 0
    for j in i["notas"]:
        if type(j) != int or j<0 or j>100:
            print(i["nombre"] ," tiene un valor erroneo: ", j)
            error = error + 1
        else:
            acum = acum + j
    if error == len(i["notas"]):
        print("NO hay calificaciones validas para ", i["nombre"], "\n")
    else:
        print(i["nombre"], ": Calificacion final: ", acum/(len(i["notas"]) - error), "\n")                
