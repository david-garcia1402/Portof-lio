#!/usr/bin/env python
# coding: utf-8

# In[66]:


#importando o selenium e o webdriver para servir de ferramentas no processo de 
#automatização
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import jupyter
import openpyxl

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)


# In[67]:


import time
navegador.get('https://web.whatsapp.com/') #entrar no site do whats web
while len(navegador.find_elements(By.XPATH, '//*[@id="pane-side"]/button/div/div[1]/div/div/span')) < 1: #se a lista de elementos do wpp web carregado for vazia, a tela ainda n carregou
    time.sleep(1)
time.sleep(2)


# In[68]:


#Whatsapp carregado
import pandas as pd #leitura do arquivo excl
tabela = pd.read_excel('Pasta2.xlsx')
print(tabela[['nome', 'mensagem', 'telefone', 'arquivo']])


# In[69]:


import urllib #ele formata os textos para o formato do link 
import pyautogui as pa

for linha in tabela.index: #.index seria os índices (que enumeram as linhas)
    #enviar a mensagem para a pessoa
    nome = tabela.loc[linha, 'nome']
    mensagem = tabela.loc[linha, 'mensagem']
    arquivo = tabela.loc[linha, 'arquivo']
    telefone = tabela.loc[linha, 'telefone']
    #texto = mensagem.replace('fulano', nome) trocar o 'fulano' pelo nome certo da pessoa
    
    
    #enviando a mensagem
    mensagem = urllib.parse.quote(mensagem) #texto formatado em link
    link = f'https://web.whatsapp.com/send?phone={telefone}&text={mensagem}'
    navegador.get(link)
    
    
    while len(navegador.find_elements(By.XPATH, '//*[@id="pane-side"]/button/div/div[1]/div/div/span')) < 1: #se a lista de elementos do wpp web carregado for vazia, a tela ainda n carregou
        time.sleep(1)
    time.sleep(2)
        
    
    
    navegador.find_element(By. XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span').click()
    time.sleep(2)


# In[ ]:




