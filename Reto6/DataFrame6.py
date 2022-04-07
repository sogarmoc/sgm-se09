import pandas as pd

diccionario = {'mes': ['Enero','Febrero','Marzo','Abril'], 'Ventas': [30500,35600,28300,33900], 'Gastos': [22000,23400,18100,20700] }

frame = pd.DataFrame(diccionario)
print(frame)

def balance(cont, meses):
    # se crea una columna nueva para saber la resta de Ventas - gastos
    cont['Balance'] = cont.Ventas - cont.Gastos
    print(frame)
    # isin -> dentro del intervalo de la lista de los meses
    return cont[cont.mes.isin(meses)].Balance.sum()


if __name__ == '__main__':
    print(balance(frame, ['Enero', 'Marzo']))

# Guardar en un csv los datos
    frame.to_csv('contabilidad.csv')

# Guardar en un csv los datos
    frame.to_csv('../csv/contabilidad.csv')

    # No queremos guardar nilas cabeceras ni los indices
    frame.to_csv('contabilidad.csv', header=False , index=False)