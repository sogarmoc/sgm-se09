import pandas as pd

diccionario = {'mes' : ['Enero','Febrero','Marzo','Abril'], 'Ventas' : [30500,35600,28300,33900], 'Gastos' : [22000,23400,18100,20700] }
frame = pd.DataFrame(diccionario)


if __name__ == '__main__':
    print(frame)
