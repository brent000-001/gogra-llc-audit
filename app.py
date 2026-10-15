import streamlit as stimport pandas as pd
st.set_page_config(page_title="GoGra LLC Audit - Douala", layout="wide")st.title("GoGra LLC Audit - Market Study Douala")st.subheader("Cabinet Comptable & Audit - Bonanjo HQ")
# Data from Bonanjo/Akwa researchdata = {    "Quartier": ["Bonanjo","Akwa","Bonapriso","Deido","Bali"],    "PME_Contactees": [18,15,12,8,7],    "Interet_Audit": [14,11,7,3,2],    "Budget_Moyen_FCFA": [2200000,1800000,1500000,900000,800000]}df = pd.DataFrame(data)df["Taux_Interet"] = df["Interet_Audit"] / df["PME_Contactees"] * 100
with st.container():    col1, col2, col3 = st.columns(3)    col1.metric("Echantillon", f"{len(df)} Quartiers")    col2.metric("Taux Interet", f"{df['Taux_Interet'].mean():.1f}%")    col3.metric("Zone Cible", "Bonanjo")
st.divider()st.subheader("1. Demande par Quartier")st.bar_chart(df.set_index("Quartier")["Interet_Audit"])
st.subheader("2. Budget Moyen")st.bar_chart(df.set_index("Quartier")["Budget_Moyen_FCFA"])
st.subheader("3. Donnees Brutes")st.dataframe(df)
st.success("Recommandation: Lancer GoGra LLC Audit a Bonanjo - 76% demande validee. CoGRA HQ: Bonanjo P.O Box 1122")
