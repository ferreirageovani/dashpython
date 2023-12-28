import streamlit as st

st.set_page_config(page_title="Players", page_icon="🏃", layout="wide")

df_data = st.session_state["data"]

clubes = df_data["club_name"].value_counts().index
club = st.sidebar.selectbox("Clube", clubes)

df_players = df_data[df_data["club_name"] == club]
players = df_players["short_name"].value_counts().index
player = st.sidebar.selectbox("Jogador", players)

player_stats = df_data[df_data["short_name"] == player].iloc[0]

# st.image(player_stats["player_url"]) ----- o codigo traria a Photo do Jogador
st.title(f"{player_stats['short_name']}")

st.markdown(f"**Clube:** {player_stats['club_name']}")
st.markdown(f"**Posição:** {player_stats['club_position']}")

col1, col2, col3, col4 = st.columns(4)
col1.markdown(f"**Idade:** {player_stats['age']}")
col2.markdown(f"**Altura:** {player_stats['height_cm'] / 100: .2f}")
col3.markdown(f"**Peso:** {player_stats['weight_kg']}")

st.divider()
st.subheader(f"Overall {player_stats['overall']}")
st.progress(int(player_stats["overall"]))

col1, col2, col3 = st.columns(3)
col1.metric(label="Valor de Mercado", value=f"€ {player_stats['value_eur']:,}")
col2.metric(label="Valor de Salario Semanal", value=f"€ {player_stats['wage_eur']:,}")
col3.metric(label="Valor da Multa", value=f"€ {player_stats['release_clause_eur']:,}")
