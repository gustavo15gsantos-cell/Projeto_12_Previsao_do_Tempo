import streamlit as st
from dados_api import previsao_temperatura

#cidades
cidades = {
    "Nürburg" : [50.3356, 6.9475],
    "Spa-Francorchamps" : [50.4372, 5.9714],
    "Le Mans" : [47.9567, 0.2070],
    "Interlagos": [-23.70186271337284, -46.70567307729004],
    "santana de parnaiba": [-23.446197823623113, -46.91864678740084]
}

#---------------------------------------------------------------------------

st.sidebar.title("Previsão do tempo")
st.sidebar.image("Matuê_ Temperatura em Cidades.png")

cidade = st.sidebar.selectbox("escolha a cidade : ", cidades.keys())
latitude = longitude = cidades [cidade]

#-------------------------------------------------------------------------------
st.title(f"Previsâo do tempo em {cidade} Para os próximos 7 dias ")

st.markdown("-----")

# Previsao da temperatura
dados, temperatura_media = previsao_temperatura(latitude, longitude)

# Previsão de temperatura
dados, temperatura_media = previsao_temperatura(latitude, longitude)

for i, d in temperatura_media.iterrows():

    with st.container(border=True):
        st.subheader(d['dia_semana'])

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Data", f'{int(d["dia"])}/{int(d["mes"])}')

        with col2:
            st.metric("Temperatura média", f"{d['temperatura_media']:.2f}°")

            
# Previsão de temperatura
dados, temperatura_media = previsao_temperatura(latitude, longitude)

for i, d in temperatura_media.iterrows():

    with st.container(border=True):

        st.subheader(d['dia_semana'])

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Data",
                f"{int(d['dia'])}/{int(d['mes'])}"
            )

        with col2:
            st.metric(
                "Temperatura média",
                f"{d['temperatura_media']:.2f}°"
            )

        with col3:

            if d['temperatura_media'] < 10:
                temp = "cold.png"

            elif d['temperatura_media'] < 18:
                temp = "cool.png"

            elif d['temperatura_media'] < 25:
                temp = "comfort.png"

            else:
                temp = "warm.png"

            st.image(temp, width=40)
