import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="GoGra LLC Audit", layout="wide")

st.title("GoGra LLC Audit - Douala PRO")
st.caption("Cabinet Comptable & Audit | Bonanjo P.O Box 1122 Douala | By Lawong Brent B.B (2026)")
st.divider()

data = {
    "Quartier": ["Bonanjo", "Akwa", "Bonapriso", "Deido", "Bali"],
    "PME_Identifiees": [18, 15, 12, 8, 7],
    "PME_Interessees": [14, 11, 7, 3, 2],
    "Budget_Moyen": [2200000, 1800000, 1500000, 900000, 800000]
}
df = pd.DataFrame(data)
df["Taux"] = (df["PME_Interessees"] / df["PME_Identifiees"] * 100).round(1)
df["Budget_M"] = (df["Budget_Moyen"] / 1000000).round(1)

c1, c2, c3, c4 = st.columns(4)
c1.metric("Taux Moyen", "55.1%")
c2.metric("Budget Moyen", "1.48M FCFA")
c3.metric("Best", "Bonanjo 77.8%")
c4.metric("Potentiel", "22M FCFA")

fig = px.bar(df, x="Quartier", y="Budget_Moyen", text="Budget_M", color="Quartier")
fig.update_traces(texttemplate='%{text}M', textposition='outside')
fig.update_layout(showlegend=False, height=380, xaxis_tickangle=0)
st.plotly_chart(fig, use_container_width=True)

st.dataframe(df, use_container_width=True)
st.success("RECOMMANDATION: Lancer GoGra LLC a Bonanjo - 77.8% valide (14/18) - 2.2M FCFA")
st.info("Pack 2.78M/client = 27.8M/an pour 10 clients")
st.caption("Source: Etude terrain 60 PME Douala Oct 2026")
