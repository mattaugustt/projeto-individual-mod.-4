#Projeto individual - Módulo 4 (SENAC/Resilia)
#Matheus Augusto -Botafogo

#importando o pandas
import pandas as pd

#Dicionário para armazenar os dados da planilha entregue pela loja.
data = {'Dia': ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo'], 
        'Limpeza' : [100, 0, 100, 0, 100, 100, 0], 'Comida' : [221.60, 375.31, 412.00, 495.20, 411.53, 245.00, 164.00], 
        'Transporte' : [150, 100, 125, 300, 275, 525, 75], 'Outros' : [0, 0, 2310, 500, 0, 0, 820]}


#criando o data_frame
df = pd.DataFrame(data)

#df #-> para visualização

df['Ganhos'] = [2200, 2420.50, 3391, 5322, 4898.50, 4200, 3893]
#adicionando a coluna ganhos no dataframe com a lista dada
#df #-> para visualização


#QUERIES:
df.query('Ganhos < 4000')  #dias da semana com ganhos inferiores a 4 mil

df.query('Ganhos > 4000')  #dias da semana com ganhos superiores à 4 mil


#QUERIES PEDIDAS NO PROJETO:
#--------------------------------------------------------------------------------
#1: A subtração de impostos dos ganhos diários, que nesta semana foi de 7%;
x = df['Ganhos'] * 0.07 #valor de impostos
r = df['Ganhos'] - x #subtração dos impostos
df['Reajustado (0,7%)'] = r   #criação de uma coluna com os valores reajustados 
#dos ganhos, denominada 'Reajustado (0,7%)'
#df #-> para visualização

#---------------------------------
#2: A soma total dos ganhos;

df['Ganhos'].sum() #-> sem o reajuste

#df['Reajustado (0,7%)'].sum() #com o reajuste

#Resultados obtidos:
#Sem reajuste: 26325.0
#Com reajuste: 24482.25


#------------------------------------
#3: A média semanal dos ganhos;
df['Ganhos'].mean()
#df['Reajustado (0,7%)'].mean()

#Resultados obtidos:
#Sem reajuste: 3760.714285714286
#Com reajuste: 3497.464285714286


#-------------------------------------------------
#4: A soma total das despesas por categoria;
#Limpeza:
l = df['Limpeza'].sum()

#Comida:
c = df['Comida'].sum()

#Transporte:
t = df['Transporte'].sum()

#Outros:
o = df['Outros'].sum()

w = l + c + t + o #soma de todas as despesas
w #total das despesas

#Resultado obtido: 7904.639999999999


#----------------------------------------------
#5: A média semanal de todas as despesas;
#Limpeza:
l = df['Limpeza'].mean()

#Comida:
c = df['Comida'].mean()

#Transporte:
t = df['Transporte'].mean()

#Outros:
o = df['Outros'].mean()

w = l+c+t+o #soma das médias
w #média semanal total

#Resultado obtido:  1129.2342857142858


#--------------------------------------------------------------------------------------------
#6: O lucro diário para informar qual dia foi mais lucrativo e o lucro total da semana;
#Gastos:
#Limpeza:
l = df['Limpeza']

#Comida:
c = df['Comida']

#Transporte:
t = df['Transporte']

#Outros:
o = df['Outros']

r = l+c+t+o #gasto diario

df['Gasto diário'] = r

g = df['Reajustado (0,7%)']

df['Lucro diário'] = g-r
df

#para achar o maior lucro diário e o dia da semana 
#(irá apresentar a linha onde está localizado o maior lucro diário)
x = df['Lucro diário'].max()
df.loc[df['Lucro diário'] == x]
