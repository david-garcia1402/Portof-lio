#!/usr/bin/env python
# coding: utf-8

# Você trabalha em uma empresa de telecom e tem clientes de vários serviços diferentes, entre os principais: internet e telefone.
# 
# O problema é que, analisando o histórico dos clientes dos últimos anos, você percebeu que a empresa está com Churn de mais de 26% dos clientes.
# 
# Isso representa uma perda de milhões para a empresa.
# 
# O que a empresa precisa fazer para resolver isso?
# 
# ANÁLISE DE DADOS COM PYTHON

# In[1]:


#PASSO A PASSO
#Passo 1: Importar a base dados 
#Passo 2: Visualizar e analisar as informações da base de dados
#Passo 3: Tratar os dados // Resolver valores que estão sendo reconhecidos de forma errada
#Passo 3: Descobrir as causas do cancelamento dos clientes

import pandas as pd #biblioteca para ler a base de dados
tabela = pd.read_csv('telecom_users.csv')

tabela = tabela.drop('Unnamed: 0', axis = 1) #excluindo a coluna unnamed 0
                                             #axis = 1 significa que é uma coluna
                                             #axis = 0 significa que é uma linha
display(tabela)
tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors = 'coerce') #aqui vai transformar a coluna 19 (TotalGasto) de object para float
tabela = tabela.dropna(how ='all' , axis = 1 ) #aqui excluiu colunas inteiras que tivesse TODOS os valores vazio
tabela = tabela.dropna(how = 'any', axis = 0) #aqui excluiu linhas inteiras que tivesse AO MENOS um valor vazio
print(tabela.info())  #mostra informações da tabela


# In[2]:


# Fazendo a análise inicial
# Coluna Churn mostra quem cancelou ou não
print(tabela['Churn'].value_counts()) #1587 de 5974 cancelaram, isso significa que realmente 26% cancelaram
print(tabela['Churn'].value_counts(normalize= True) * 100) #aqui mostra a porcentagem


# In[3]:


# Comparar cada coluna da base de dados com a coluna Churn
import plotly.express as px #Essa biblioteca mostra gráficos dinâmicos

#CRIANDO GRÁFICO
for coluna in tabela.columns:
    grafico = px.histogram(tabela, x = coluna, color = 'Churn', text_auto = True) #aqui mostra o gráfico com os dados de 'TipoContrato' e quantos cancelaram (Churn)
#EXIBIR O GRÁFICO
    grafico.show()


# ANÁLISES E CONCLUSÕES:
# - Clientes solteiros tendem a cancelarem mais (1011)
#     => Hipótese: clientes casados tendem a não cancelar porque podem dividir o plano, já solteiros provavelmente optam por serviços mais baratos
# - Clientes não dependentes tendem a cancelarem mais (1306)
#     => Hipótese: clientes dependentes tendem a ter ajuda no pagamento por parentes ou amigos, já os que não são dependentes provavelmente optam por serviços mais baratos
# - Clientes tendem a cancelarem já nos primeiros dois meses (504)
#     => Hipótese: planos mensais tendem a ser um pouco mais caro, podemos fazer planos trimestrais, 6 meses ou anual com um preço acessível e admirador
# - Clientes com serviço de internet FIBRA cancela quase com 50% de certeza (1091 CHURN / 1536 NAO CHURN)
# - Clientes sem serviço de segurança online tende a cancelar (1242 de 2982)
#     => Hipótese: clientes com vários serviços tendem a cancelar mais pelo alto valor de serviços separados, podemos fazer pacotes com esses serviços inclusos com um preço acessível e admirador
# 
