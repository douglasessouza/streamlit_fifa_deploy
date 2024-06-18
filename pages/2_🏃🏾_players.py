import streamlit as st 
import pandas as pd 

#configurando a página
st.set_page_config(
    page_title="Players",
    page_icon="🏃🏾",
    layout="wide"
)

df_data = st.session_state['data']

clubes = df_data['Club'].value_counts().index #pegando os valores únicos
club = st.sidebar.selectbox('Clube', clubes)

df_players = df_data[(df_data['Club'] == club)]
players = df_players['Name'].unique() #pegando os valores únicos com unique
player = st.sidebar.selectbox('Jogador', players)

#montando a table 
player_stats = df_data[df_data['Name'] == player].iloc[0]

#colocando a foto 
##st.image(player_stats["Photo"])
##st.title(player_stats["Name"])

#fazendo markdowns
st.markdown(f"**Clube:** {player_stats['Club']}")
st.markdown(f"**Posição:** {player_stats['Position']}")

#criando colunas 
col1, col2, col3, col4 = st.columns(4)
col1.markdown(f"**Idade:** {player_stats['Age']}")
col2.markdown(f"**Altura:** {player_stats['Height(cm.)'] / 100}")
col3.markdown(f"**Peso:** {round(player_stats['Weight(lbs.)'] * 0.453, 2)}") 
# ou col3.markdown(f"**Peso:** {player_stats['Weight(lbs.)'] * 0.453:.2f)}") -> :.2f usado no final é para arredondar 

#colocando uma linha
st.divider()

st.subheader(f"Overall {player_stats['Overall']}")
st.progress(int(player_stats['Overall']))

st.divider()
col1, col2, col3, col4 = st.columns(4)
#usando st.metric
col1.metric(label = 'Valor de mercado', value=f"£ {player_stats['Value(£)']:,}")
col2.metric(label = 'Remuneração semanal', value=f"£ {player_stats['Wage(£)']:,}")
col3.metric(label = 'Clásula de recisão', value=f"£ {player_stats['Release Clause(£)']:,}")