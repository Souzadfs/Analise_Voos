import pandas as pd

df = pd.read_csv("voos_comerciais_ficticios.csv")
print(df.shape)

#mostrando as 5 primeiras linhas do dataset
print('Primeiras linhas do dataset')
print(df.head())

#Verificando os tipo de dados de cada coluna
print(df.dtypes)

#verificando se existe valores nulos
print(df.isnull().sum())

#Transformando a coluna 'Cancelado' em booleano
df['Cancelado'] = df['Cancelado'].map({'Sim':True, 'Não': False})

def categorizar_atraso(minutos):
    if minutos == 0:
        return 'Sem atraso'
    elif 1 <= minutos <= 30:
        return 'Leve'
    
    elif 30 <= minutos <= 90:
        return 'Moderado'
    
    else:
        return 'Grave'