#!/usr/bin/env python
# coding: utf-8

# PASSO A PASSO - PROJETO DE CIÊNCIA DE DADOS - PREVISÃO DE VENDAS
# 
# Passo 1: Entendimento do Desafio 
# Passo 2: Entendimento da Área/Empresa
# Passo 3: Extração/Obtenção de Dados
# Passo 4: Ajuste de Dados (Tratamento/Limpeza)
# Passo 5: Análise Exploratória
# Passo 6: Modelagem + Algoritmos (Aqui entra a inteligência artificial, se necessário)
# Passo 7: Interpretação dos resultado

# Desafio: Conseguir prever as vendas que vamos ter em determinado período com base nos gastos em anúncios nas 3 grandes redes que a empresa investe: TV, Jornal e Rádio

# In[3]:


#Importar a base de dados
import pandas as pd

dados = pd.read_csv('advertising.csv')
print(dados)


# In[7]:


import matplotlib.pyplot as plt #Bibliotecas para criar gráficos
import seaborn as sns

 
print(dados.corr()) #Mostrando a correlação dos itens

#Criando um gráfico
sns.heatmap(dados.corr(), cmap = 'Blues', annot= True) #Gráfico das correlações

#Exibir o gráfico
plt.show()


# In[9]:


#Inteligência Artificial

y = dados['Vendas']
x = dados[['TV', 'Radio', 'Jornal']]

from sklearn.model_selection import train_test_split

x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size= 0.3, random_state= 1)

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

modelo_regressaolinear = LinearRegression()
modelo_arvoredecisao = RandomForestRegressor()

modelo_regressaolinear.fit(x_treino, y_treino)
modelo_arvoredecisao.fit(x_treino, y_treino)

previsao_regressaolinear = modelo_regressaolinear.predict(x_teste)
previsao_arvoredecisao = modelo_arvoredecisao.predict(x_teste)

from sklearn.metrics import r2_score

print(r2_score(y_teste, previsao_regressaolinear))
print(r2_score(y_teste, previsao_arvoredecisao))


# In[11]:


dados_auxiliar = pd.DataFrame()
dados_auxiliar['y_teste'] = y_teste
dados_auxiliar['Previsao Arvore Decisao'] = previsao_arvoredecisao
dados_auxiliar['Previsao Regressao'] = previsao_regressaolinear

print(dados_auxiliar)


# In[14]:


#Fazendo a previsão
nova_tabela = pd.read_csv('novos.csv')
print(nova_tabela)

previsao = modelo_arvoredecisao.predict(nova_tabela)
print(previsao)

