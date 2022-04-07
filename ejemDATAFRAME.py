import pandas as pd

data = {"calorias": [420,380,390], "duracion":[50,40,45]}

myvar = pd.DataFrame(data)

# crear un indice personalizado

df = pd.DataFrame(data, index = ['dia1', 'dia2', 'dia3'])

if __name__ == '__main__':
    print(myvar)
    print(pd.__version__)

    # referencian un valor del dataframe (un unico valor)
    print(myvar.loc[0])

    # si quiero localizar mas de un registro
    print(myvar.loc[[0,1]])

    print(df)