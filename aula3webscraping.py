#!/usr/bin/env python
# coding: utf-8

# Automação Web e busca de informações com Python 3
# 
# Buscar preço do Euro, Dólar e Ouro
# 

# In[5]:


#Passo 1: Pegar cotação do ouro
#Passo 2: Pegar cotação do dólar
#Passo 3:Pegar cotação do euro
#Passo 4: Atualizar a base de dados
#Passo 5: Recalcular os preços
#Passo 6: Exportar a base atualizada


# In[6]:


from selenium import webdriver
navegador = webdriver.Chrome()

#Pegando a cotação do dólar
navegador.get('https://www.google.com/search?q=cota%C3%A7%C3%A3o+dolar&oq=cota&aqs=chrome.0.0i131i433i512j69i57j0i433i512j0i131i433i512j0i433i512j0i512j0i131i433i512j0i433i512l3.1726j1j7&sourceid=chrome&ie=UTF-8')#abrindo o link para ver o dólar
cotacao_dolar = navegador.find_element('xpath', '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')#Pegando o preço do dólar
print(cotacao_dolar)

#Pegando a cotação do euro
navegador.get('https://www.google.com/search?q=cota%C3%A7%C3%A3o+euro&oq=cota%C3%A7%C3%A3o+euro&aqs=chrome.0.0i131i433i512l3j0i433i512j0i512l6.1822j1j7&sourceid=chrome&ie=UTF-8')#abrindo o link da cotação do euro
cotacao_euro = navegador.find_element('xpath', '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')#Pegando o preço do euro
print(cotacao_euro)

#Pegando cotação do ouro
navegador.get('https://www.melhorcambio.com/ouro-hoje')#Site da cotação do ouro
cotacao_ouro = navegador.find_element('xpath', '//*[@id="comercial"]').get_attribute('value')#Pegando o preço do ouro
cotacao_ouro = cotacao_ouro.replace(',', '.')
print(cotacao_ouro)


# In[7]:


#Importando a base de dados e atualizar a base
import pandas as pd

dados = pd.read_excel('Produtos.xlsx')

dados.loc[dados['Moeda'] == 'Dólar', 'Cotação'] = float(cotacao_dolar)#Ajustando a tabela para a cotação dólar
dados.loc[dados['Moeda'] == 'Euro', 'Cotação'] = float(cotacao_euro)#Ajustando a tabela para a cotação euro
dados.loc[dados['Moeda'] == 'Ouro', 'Cotação'] = float(cotacao_ouro)#Ajustando a tabela para a cotação ouro

#Recalculando os preços
dados['Preço de Compra'] = dados['Preço Original'] * dados['Cotação']
dados['Preço de Venda'] = dados['Preço de Compra'] * dados['Margem']
print(dados)

#Exportando uma base de dados NOVA 
dados.to_excel('Produtos NOVO.xlsx', index=False)
navegador.quit()

