import streamlit as st
import pandas as pd
import requests

url ='https://dadosabertos.camara.leg.br/api/v2/deputados?siglaSexo=F&ordem=ASC&ordenarPor=nome'

resposta = requests.get(url)

dfmulheres = pd.DataFrame(resposta.json()['dados'])

url ='https://dadosabertos.camara.leg.br/api/v2/deputados?siglaSexo=M&ordem=ASC&ordenarPor=nome'

respostaM = requests.get(url)

dfhomens = pd.DataFrame(respostaM.json()['dados'])

df = pd.concat([dfmulheres, dfhomens])

opcao = st.selectbox(
    'Qual gênero vc quer selecionar?',
     ['Feminino','Masculino'])

st.write('Você selecionou: ', opcao)

if opcao == 'Feminino':
  st.write(dfmulheres)

else:
  st.write(dfhomens)

if opcao == 'Feminino':
  st.header('Número de deputadas por UF')
  st.bar_chart(dfmulheres['siglaUf'].value_counts())

else:
  st.header('Número de deputados por UF')
  st.bar_chart(dfhomens['siglaUf'].value_counts())
