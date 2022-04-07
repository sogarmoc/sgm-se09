import pandas as pd

# Todas las filas que quiero que me muestre
pd.options.display.max_rows = 101
# Las columnas que quiero que me muestre
pd.options.display.max_columns = 50
# la longitud de columna
pd.options.display.max_colwidth = 20

# delimitador |
df = pd.read_csv('../sgm-se09/data/file3.csv', sep='|')


df = pd.read_csv('../sgm-se09/data/file3.csv')

# leer 2 csv
df2 = pd.read_csv('../sgm-se09/data/file3.csv')

s = pd.concat([df,df2])

if __name__ == '__main__':
    print(df)
    print(s)

    # filtrar por Male
    result = df[df['gender']=='Male']
    print(result)

    # transformarlo a una lista para tener las funciones de python de la lista
    lista = result.values.tolist()
    print(lista)

    # aqui filtra por email
    lista2 = df['email'].tolist()
    print(lista2)

    # aqui filtra por 3 campos de la lista y aquellos que solo sean Female
    lista3 = df[['email','ip_address','gender']].query("gender=='Female'")
    lista3 = lista3.values.tolist()
    print(lista3)

    # se añade una query de los que sean Male y esa ip
    lista4 = df.query("gender=='Male' and ip_address =='252.82.166.20'")
    lista4 = lista4[['email','ip_address']].values.tolist()
    print(lista4)

    # Nuevo df de la lista 3 con solo esas columnas guardarlo en un csv nuevo

    df3 = pd.DataFrame(lista3, columns = ['email','ip_address','gender'])
    print(df3)
    df3.to_csv('../sgm-se09/csv/file4.csv', header=True, index=False)

    # implememntar graficos
    