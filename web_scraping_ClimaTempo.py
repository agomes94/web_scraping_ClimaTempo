# -*- coding: utf-8 -*-
"""
Created on Sat May  9 08:16:28 2020

@author: agomes
"""

from selenium import webdriver

driver = webdriver.Chrome(r'C:\chromedriver.exe')

site = 'https://www.climatempo.com.br/previsao-do-tempo/cidade/'
cidades = ['199/tresmarias-mg','130/contagem-mg','477/lencoispaulista-sp']

for i in cidades:
    driver.get(site+i)
    localidade = driver.find_element_by_xpath('//*[@id="mainContent"]/div[4]/div[4]/div[1]/div[2]/div[1]/div/h1').text
    temp_Min = driver.find_element_by_xpath('//*[@id="min-temp-1"]').text
    temp_Max = driver.find_element_by_xpath('//*[@id="max-temp-1"]').text
    chuva = driver.find_element_by_xpath('//*[@id="mainContent"]/div[4]/div[4]/div[1]/div[2]/div[2]/div[2]/div[1]/ul/li[2]/div/span').text
    vento = driver.find_element_by_xpath('//*[@id="mainContent"]/div[4]/div[4]/div[1]/div[2]/div[2]/div[2]/div[1]/ul/li[3]/div').text
    umidade = driver.find_element_by_xpath('//*[@id="mainContent"]/div[4]/div[4]/div[1]/div[2]/div[2]/div[2]/div[1]/ul/li[4]/div/p').text.replace("\n"," - ")
    sol = driver.find_element_by_xpath('//*[@id="mainContent"]/div[4]/div[4]/div[1]/div[2]/div[2]/div[2]/div[1]/ul/li[5]/span[2]').text
  
    print(localidade,'\n',
          'Temperatura Mínima:',temp_Min,'\n',
          'Temperatura Máxima:',temp_Max,'\n',
          'Chuva:',chuva,'\n','Vento:',vento,'\n',
          'Umidade',umidade,'\n',
          'Sol:',sol)
    print("-" * 60)

driver.close()

