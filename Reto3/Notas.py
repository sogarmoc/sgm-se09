import pandas as pd

alumnos = ['Sonia', 'Juan', 'Pedro','Sergio']
notas = [8, 4, 8.9,7.3]

# Reto 3
notas = pd.Series(notas, index = (alumnos))
estado = pd.Series([notas.min(),notas.max(),notas.mean(),notas.std()], index=['Minimo', 'Maximo','Media','Desviacion tipica'])

# Reto 4
aprobados = notas[notas >= 5]

# filtro por indice para saber la notas
filtro = notas['Pedro']


if __name__ == '__main__':
    print(notas)
    print('Nota minima\n', notas.min())
    print('Nota maxima\n', notas.max())
    print('Nota media\n', notas.mean())
    print('Desviacion tipica\n', notas.std())
    print(estado)
    # Reto 4, mostrar en orden ascendente las notas de los aprobados
    print(aprobados.sort_values(ascending=False))
    print(filtro)

