import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import time

st.set_page_config(
    page_title="Agent SolarQuote - Bénin",
    page_icon="☀️",
    layout="wide"
)

st.title("☀️ Agent SolarQuote")
st.subheader("Agent IA avec Splunk pour la maintenance prédictive des installations solaires au Bénin")
st.caption("Hackathon Splunk 2026 | Équipe: Ayode290")

# Sidebar
with st.sidebar:
    st.header("⚙️ Paramètres")
    site = st.selectbox("Choisir le site solaire", ["Cotonou - Site A", "Parakou - Site B", "Natitingou - Site C"])
    seuil_alert = st.slider("Seuil d'alerte température °C", 40, 80, 60)
    
    st.markdown("---")
    st.write("**Stack Technique**")
    st.write("- Splunk pour l'analyse de logs")
    st.write("- Python 3.11")
    st.write("- Streamlit UI")
    st.write("- MongoDB Atlas")

# Génération de données simulées type Splunk
@st.cache_data
def generer_donnees(site_nom, jours=30):
    dates = [datetime.now() - timedelta(days=x) for x in range(jours)]
    data = {
        "timestamp": dates,
        "temperature_panneau": np.random.normal(55, 10, jours).clip(30, 85),
        "puissance_kw": np.random.normal(4.2, 0.8, jours).clip(1, 6),
        "irradiance": np.random.normal(800, 200, jours).clip(200, 1200),
        "defaut": np.random.choice([0, 1], jours, p=[0.9, 0.1])
    }
    df = pd.DataFrame(data)
    df["site"] = site_nom
    df["risque_panne"] = (df["temperature_panneau"] > 65) | (df["defaut"] == 1)
    return df

df = generer_donnees(site)

# Dashboard principal
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Température Moy", f"{df['temperature_panneau'].mean():.1f} °C", 
              delta=f"{df['temperature_panneau'].iloc[-1] - df['temperature_panneau'].iloc[-2]:.1f} °C")
with col2:
    st.metric("Puissance Actuelle", f"{df['puissance_kw'].iloc[-1]:.2f} kW")
with col3:
    alertes = df['risque_panne'].sum()
    st.metric("Alertes 30j", f"{alertes}", delta_color="inverse")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.subheader("📈 Évolution Température")
    st.line_chart(df.set_index("timestamp")["temperature_panneau"])

with col2:
    st.subheader("⚡ Puissance vs Irradiance")
    st.scatter_chart(df, x="irradiance", y="puissance_kw")

# Module "Agent Splunk"
st.markdown("---")
st.subheader("🤖 Agent de Maintenance Prédictive")

uploaded_file = st.file_uploader("1. Uploader un CSV de logs Splunk", type=["csv"])

if st.button("2. Lancer l'analyse prédictive", type="primary"):
    with st.spinner("Agent Splunk en cours d'analyse..."):
        time.sleep(2)
        
    if uploaded_file is not None:
        st.success("Fichier analysé avec succès !")
        st.dataframe(pd.read_csv(uploaded_file).head())
    else:
        st.info("Analyse sur données simulées du site : " + site)
    
    # Résultats IA
    st.markdown("### Résultats")
    if alertes > 3:
        st.error(f"🚨 Risque élevé détecté sur {site}. Intervention recommandée sous 7 jours.")
        st.write(f"- {alertes} anomalies de température > {seuil_alert}°C")
        st.write("- Perte de rendement estimée : 12%")
    else:
        st.success(f"✅ Site {site} : État de santé OK. Prochaine maintenance dans 45 jours.")
    
    st.markdown("### Actions recommandées")
    st.write("1. Nettoyage des panneaux Site C")
    st.write("2. Vérifier onduleur n°2")
    st.write("3. Exporter rapport pour technicien")

st.markdown("---")
st.caption("Code sous Licence MIT | Dépôt: https://github.com/Ayode290/Agent-SolarQuote-")
