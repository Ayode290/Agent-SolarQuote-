# Agent-SolarQuote

**Agent IA avec Splunk pour la maintenance prédictive et les devis photovoltaïques des installations solaires au Bénin - Hackathon Splunk**

## 1. Description

**Agent-SolarQuote** est un agent intelligent développé pour le contexte béninois. 
L'objectif : Réduire de 5 jours à 2 minutes le temps de création d'un devis photovoltaïque et anticiper les pannes sur les installations solaires au Bénin.

Au Bénin, 60% de la population n'a pas encore un accès fiable à l'électricité. Les installateurs solaires passent en moyenne 5 jours à se déplacer, mesurer les toits et calculer un devis à la main. Pendant ce temps, les clients perdent de l'argent et les petites entreprises solaires ne peuvent pas scaler.

**Agent-SolarQuote** utilise l'IA de vision par ordinateur + Gemini pour :
1.  **Devis Express** : Analyser une photo satellite d'un toit et générer un devis solaire complet en 2 min.
2.  **Maintenance Prédictive** : Détecter les signes de panne, ombrage, poussière ou dégradation des panneaux à partir de données Splunk/IoT.
3.  **Optimisation** : Proposer le meilleur dimensionnement et emplacement des panneaux selon l'ensoleillement au Bénin.

Le projet est 100% fonctionnel et déployé pour le marché béninois.

## 2. Problème au Bénin

1.  **Délai** : Un devis solaire prend 5 jours en moyenne entre déplacement, mesure, calcul.
2.  **Coût** : Les frais de déplacement renchérissent l'installation pour les ménages.
3.  **Pannes** : 30% des installations perdent en rendement après 2 ans faute de maintenance préventive. 
4.  **Manque de données** : Peu d'installateurs ont des outils pour analyser l'état des panneaux à distance.

## 3. Solution

Agent-SolarQuote est une web-app Streamlit qui agit comme un "commercial IA".

**Fonctionnalités clés :**
1.  **Analyse de Toit par IA** : Upload d'une photo satellite/adressage. L'IA Gemini + Vision calcule la surface, l'orientation, l'ombrage.
2.  **Génération de Devis** : Devis PDF en 2 min avec coût matériel, main d'oeuvre, ROI sur 5 ans, adapté aux prix du marché au Bénin.
3.  **Monitoring Splunk** : Connexion aux données IoT de l'installation. L'agent Splunk détecte les anomalies de production kWh et alerte avant la panne.
4.  **Maintenance Prédictive** : Modèle Scikit-learn qui prédit la probabilité de panne dans les 30 prochains jours selon température, poussière Harmattan, production.

## 4. Technologies Utilisées

-   **Langage** : Python
-   **Frontend** : Streamlit
-   **IA Générative** : Google Gemini API
-   **Vision par Ordinateur** : OpenCV, Gemini Vision
-   **Machine Learning** : Scikit-learn, Pandas, NumPy
-   **Observabilité** : Splunk SDK for Python
-   **Visualisation** : Matplotlib
-   **Déploiement** : Streamlit Cloud
-   **Base de données** : SQLite

## 5. Impact au Bénin

1.  **Économique** : Divise par 1000 le temps de devis. Une PME solaire peut traiter 50 clients/jour au lieu de 1.
2.  **Social** : Accélère l'accès à l'énergie solaire pour les ménages et PME hors réseau à Cotonou, Parakou, Natitingou.
3.  **Environnemental** : Optimise le dimensionnement = moins de gaspillage de panneaux. La maintenance prédictive augmente la durée de
