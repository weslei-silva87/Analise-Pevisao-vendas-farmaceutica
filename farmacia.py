import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

# Carregar os dados
tabela_nova = pd.read_csv(r'C:\Users\Weslei\Desktop\Projeto DS\tabela_farmacia.csv')

# Remover a coluna 'datum' se ela estiver presente
if 'datum' in tabela_nova.columns:
    tabela_nova.drop(columns=['datum'], inplace=True)

# Converter as colunas de medicamentos para tipo numérico
medicamentos = ['M01AB', 'M01AE', 'N02BA', 'N02BE', 'N05B', 'N05C', 'R03', 'R06']
tabela_nova[medicamentos] = tabela_nova[medicamentos].apply(pd.to_numeric, errors='coerce')

#=======================================================================================================
# STREAMLIT
st.header('Dashboard Farmácia')
# Definindo a barra lateral para filtros
st.sidebar.title('Filtros')

# Opções para os medicamentos
medicamentos = ['Todos'] + medicamentos
medicamento_selecionado = st.sidebar.selectbox('Selecione o medicamento', medicamentos)

# Opções para os anos
anos = ['Todos'] + list(tabela_nova['ano'].unique())
ano_selecionado = st.sidebar.selectbox('Selecione o ano', anos)

# Opções para os meses
meses = ['Todos'] + list(range(1, 13))
mes_selecionado = st.sidebar.selectbox('Selecione o mês', meses)

# Aplicando a lógica de filtro
data_filtrado = tabela_nova
if medicamento_selecionado != 'Todos':
    data_filtrado = data_filtrado[[medicamento_selecionado, 'ano', 'mes']]
if ano_selecionado != 'Todos':
    data_filtrado = data_filtrado[data_filtrado['ano'] == ano_selecionado]
if mes_selecionado != 'Todos':
    data_filtrado = data_filtrado[data_filtrado['mes'] == mes_selecionado]

# Mostrando os dados filtrados
st.write('### Dados filtrados:')
st.write(data_filtrado)

# Se nenhum medicamento específico for selecionado, plote todos os gráficos
if medicamento_selecionado == 'Todos':
    # Calculando a média de demanda para cada medicamento por ano
    media_por_ano = data_filtrado.groupby('ano').mean().reset_index()

    # Plotando gráfico interativo
    fig = px.line(media_por_ano, x='ano', y=medicamentos[1:], title='Média de demanda por medicamento ao longo dos anos')
    st.write('### Gráfico de média de demanda por medicamento e ano:')
    st.plotly_chart(fig)

else:
    # Calculando a média de demanda para o medicamento selecionado por ano
    media_por_medicamento_ano = data_filtrado.groupby(['ano']).mean().reset_index()

    # Plotando gráfico interativo
    fig = px.line(media_por_medicamento_ano, x='ano', y=medicamento_selecionado, title=f'Média de demanda para o medicamento {medicamento_selecionado} por ano')
    st.write('### Gráfico de média de demanda por ano:')
    st.plotly_chart(fig)

    # Inicializando a lista de resultados
    resultados = []

    # Verificando se cada medicamento aumentou ou diminuiu sua demanda
    for medicamento in medicamentos[1:]:
        demanda_inicial = data_filtrado.iloc[0][medicamento]  # Demanda no primeiro ano
        demanda_final = data_filtrado.iloc[-1][medicamento]  # Demanda no último ano

        if demanda_final > demanda_inicial:
            aumento_percentual = ((demanda_final - demanda_inicial) / demanda_inicial) * 100
            resultados.append((medicamento, aumento_percentual))
        elif demanda_final < demanda_inicial:
            diminuicao_percentual = ((demanda_inicial - demanda_final) / demanda_inicial) * 100
            resultados.append((medicamento, -diminuicao_percentual))
        else:
            resultados.append((medicamento, 0))

    # Plotando o gráfico de barras
    fig, ax = plt.subplots(figsize=(10, 6))
    barras = ax.bar([x[0] for x in resultados], [x[1] for x in resultados], color=['red' if x[1] < 0 else 'blue' for x in resultados])

    # Adicionando os valores nas barras
    for i, barra in enumerate(barras):
        altura = barra.get_height()
        ax.annotate('{:.2f}%'.format(altura),
                    xy=(barra.get_x() + barra.get_width() / 2, altura),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom')

    # Definindo rótulos e título
    ax.set_ylabel('Variação Percentual')
    ax.set_title('Variação Percentual da Demanda de Medicamentos')
    plt.xticks(rotation=45, ha='right')

    st.write('### Gráfico de variação percentual da demanda de medicamentos:')
    st.pyplot(fig)

