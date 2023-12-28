import streamlit as st

st.set_page_config(page_title="Teams", page_icon="⚽", layout="wide")

df_data = st.session_state["data"]

clubes = df_data["club_name"].value_counts().index
club = st.sidebar.selectbox("Clube", clubes)

df_filtered = (
    df_data[df_data["club_name"] == club]
    .drop_duplicates(subset=["short_name"])
    .set_index("club_name")
)

st.markdown(f"## {club}")

columns = [
    "short_name",
    "club_position",
    "overall",
    "potential",
    "international_reputation",
    "shooting",
    "passing",
    "dribbling",
]

st.dataframe(
    df_filtered[columns],
    column_config={
        "potential": st.column_config.ProgressColumn(
            "Pontencial",
            format="%d",
            min_value=0,
            max_value=100,
        ),
        "international_reputation": st.column_config.NumberColumn(),
        "overall": st.column_config.ProgressColumn(
            "Overall",
            format="%d",
            min_value=0,
            max_value=100,
        ),
    },
)
