import pandas as pd
import matplotlib.pylab as plot
import seaborn as sns

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
    

df['Categoria de atraso'] = df['Atraso (min)'].apply(categorizar_atraso)

frequenca_atraso = df['Categoria de atraso'].value_counts().sort_index()

sns.set(style='whitegrid')

plot.figure(figsize= (8,6))
sns.barplot(x=frequenca_atraso.index, y=frequenca_atraso.values, palette="viridis")
plot.title("Distribuição das Categorias por atraso")
plot.xlabel("Categoria por atraso")
plot.xlabel("Numero de voos")
plot.tight_layout

plot.show