import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')#aumentar o tamanho da página

st.title('Localização das comunidades quilombolas (2022)')
df = pd.read_csv('https://raw.githubusercontent.com/adrianalite/datasets/main/BR_LQs_CD2022.csv')

df.drop(columns=['Unnamed: 0'], inplace=True)
list = ['Lat_d', 'Long_d']
# convertendo para numeros
df[list] = df[list].apply(pd.to_numeric, errors='coerce')
estados = df.sort_values(by='NM_UF', ascending=True)['NM_UF'].unique()
estadoFiltro = st.selectbox(
    'Qual estado selecionar?',
    estados)
dadosFiltrados = df[df['NM_UF'] == estadoFiltro]
if st.checkbox('Mostrar tabela'):
  st.write(dadosFiltrados)
st.map(dadosFiltrados, latitude="Lat_d", longitude="Long_d")

qtdeMunicipios = len(df['NM_MUNIC'].unique())
st.write("A quantidade de municípios com localização quilombola é " + str(qtdeMunicipios))

qtdeComunidades = len(df['NM_AGLOM'].unique())
st.write(f"A quantidade de comunidades quilombolas é {str(qtdeComunidades)}.")

st.header('Número de comunidades por UF')
st.bar_chart(df['NM_UF'].value_counts())

#tentando mostrar de mais a menos
top_municipios = df['NM_MUNIC'].value_counts().nlargest(10)

# Exibindo o gráfico em ordem decrescente
st.bar_chart(top_municipios)

numero = st.slider('Selecione um número de linhas a serem exibidas', min_value = 0, max_value = 100)
st.write(df.head(numero))

st.metric('# Municípios', len(df['NM_MUNIC'].unique()))
st.metric('# Comunidades', len(df['NM_AGLOM'].unique()))
