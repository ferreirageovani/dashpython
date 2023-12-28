import streamlit as st
import pandas as pd
import webbrowser
from datetime import datetime

if "data" not in st.session_state:
    df_data = pd.read_csv("datasets/male_players.csv", index_col=0)
    df_data = df_data[
        df_data["club_contract_valid_until_year"] >= datetime.today().year
    ]
    df_data = df_data[df_data["value_eur"] > 0]
    df_data = df_data.sort_values(by="overall", ascending=False)
    st.session_state["data"] = df_data

st.write("# DADOS OFICIAIS EA FC 24 🇧🇷")
st.sidebar.markdown("© 2023-2024 [GFdeveloper](https://github.com/ferreirageovani)")

btn = st.button("Acesse os dados no Kaggle")
if btn:
    webbrowser.open_new_tab(
        "https://www.kaggle.com/datasets/stefanoleone992/ea-sports-fc-24-complete-player-dataset"
    )

st.markdown(
    """
    O conjunto de dados
    de jogadores de futebol de 2023/24 contem informações
    abramgentes sobre jogadores profissionais.
    O conjunto contém uma ampla gama de atributos, incluindo:
    caracteristicas fisicas, de jogo, detalhes de contrato
    e afiliações a clubes.
    """
)
