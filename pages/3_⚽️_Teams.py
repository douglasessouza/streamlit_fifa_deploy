import streamlit as st 

#configurando a página
st.set_page_config(
    page_title="Players",
    page_icon="⚽️",
    layout="wide"
)

df_data = st.session_state['data']

clubes = df_data['Club'].value_counts().index #pegando os valores únicos
club = st.sidebar.selectbox('Clube', clubes)

#filtrando o dataframe
df_filtered = df_data[(df_data["Club"] == club)].set_index("Name")

st.image(df_filtered.iloc[0]["Club Logo"])
st.markdown(f"## {club}")

#criando uma lista com as colunas que quero ver no dataset
columns = ["Age", "Photo", "Flag", "Overall", "Value(£)", "Wage(£)", "Joined",
           "Height(cm.)", "Weight(lbs.)", "Contract Valid Until", "Release Clause(£)"]

st.dataframe(df_filtered[columns],
             column_config = {
                 "Overall": st.column_config.ProgressColumn(
                     "Overall", format = "%d", min_value = 0, max_value = 100
                 ),
                 "Wage(£)": st.column_config.ProgressColumn("Weekly Wage", format = "£%f", 
                                                            min_value = 0, max_value = df_filtered["Wage(£)"].max() #essa parte organiza pelo maior salário
                 ),
                 "Photo": st.column_config.ImageColumn(),
                 "Flag": st.column_config.ImageColumn("Country"), #passando Country renomeia a coluna


             }
             )