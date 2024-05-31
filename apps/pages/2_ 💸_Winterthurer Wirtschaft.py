import streamlit as st
import time
import numpy as np
import pandas as pd
import plotly
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="Winterthurer Wirtschaft", page_icon="💸")

st.markdown("# Winterthurer Wirtschaft")
st.sidebar.header("Winterthurer Wirtschaft")
st.markdown(
    """
    ### Wie hat sich die Winterthurer Wirtschaft in den letzten Jahren so entwickelt? 🤓
    Wie im Sport, nehmen wir auch hier zum vergleichen die Stadt Zürich
    - Datenquelle [ Statistisches Amt Kt. ZH](https://www.zh.ch/de/direktion-der-justiz-und-des-innern/statistisches-amt.html)
    """
)


status_text = st.sidebar.empty()

def plot():

    df = pd.read_csv('apps/data/processed/stats_wirtschaft_processed.csv')

    #zeitraum_list = ['Ganzer Zeitraum', 'Departement Finanzen Winterthur NICHT von SP besetzt', 'Departement Finanzen Winterthur von SP besetzt']
    #zeitraum = st.selectbox("Wähle einen Zeitraum", zeitraum_list)
    
    indikator_list = ['Nettoschuld [Fr.]',  'Steuerfuss (beschlossen) [%]', 'Relative Steuerkraft [Fr./Einw.]','Nettoschuld [Fr./Einw.]' ,'Differenz Relative Steuerkraft [Fr./Einw.] - Nettoschuld [Fr./Einw.]']
    indikator = st.selectbox("Wähle einen Indikator", indikator_list)
    
    cities = ["Zürich, Stadt", "Winterthur, Stadt"]
    
    #if (zeitraum == 'Departement Finanzen Winterthur NICHT von SP besetzt'):
    #    dfs = {city: df[(df["Jahr"] <= 2012) & (df.Indikator == indikator) & (df.Stadt == city)] for city in cities}
    #elif zeitraum == 'Departement Finanzen Winterthur von SP besetzt':
    #    dfs = {city: df[(df["Jahr"] > 2012) & (df.Indikator == indikator) & (df.Stadt == city)] for city in cities}
    #else:
    dfs = {city: df[(df.Indikator == indikator) & (df.Stadt == city)] for city in cities}
        
    #st.write("Du hast den Zeitraum: ***{}*** und den Indikator: ***{}*** gewählt".format(zeitraum, indikator))

    fig = go.Figure()
    for city, df in dfs.items():
        fig = fig.add_trace(go.Scatter(x=df["Jahr"], y=df["Wert"], name=city))

    st.plotly_chart(fig)

plot()

st.markdown(
    """
    ### Was sich zu bestimmten Faktoren sagen lässt:
    
    - ***Relative Steuerkraft [Fr./Einw.]*** Ist in der Stadt Zürich beinahe doppelt so hoch wie in der Stadt Winterthur
    - ***Nettoschuld [Fr./Einw.]*** Ist in beiden Städten ähnlich. Für die Stadt Zürich ist sie aber eine geringere Gefahr, da die relative Steuerkraft viel stärker ist
    - ***Nettoschuld [Fr.]*** Diese verdoppelte sich in Winterhur im Zeitraum von 2012-2016, pikant ist dabei, dass seit 2012 das Finanz Departement von der SP besetzt ist (zuvor FDP)
    - ***Steuerfuss (beschlossen) [%]*** Aufgrund des um 6% höheren Steuerfusses bekommt Winterthur überhaupt die eigene Verschuldung langsam in den Griff
    
    ### Auch in Zürich verschlechtert sich die Lage zunehmend, aber weshalb?
    
    Sicherlich ein Grund ist der schweizweit zweithöchste Gewinnsteuersatz für Unternehmen. Die Anzahl [abgewanderter Firmen war im Kanton Zürich im Jahr 2022](https://www.tagesanzeiger.ch/kein-kanton-verliert-so-viele-firmen-wie-zuerich-257457694679) mit Abstand am höchsten.
    """
)

from PIL import Image
image = Image.open('apps/images/firmenabwanderung.png')
st.image(image)

st.markdown(
    """
    ### Weshalb ist der zweithöchste Gewinnsteuersatz gerade für Winterthur verheerend?
    
    Laut [Umfrage des House of Winterthur ist der Gewinnersteuersatz für Winterthurer Unternehmen kein Problem](https://www.landbote.ch/jedes-zweite-unternehmen-findet-zu-wenig-gutes-personal-362693317602). Das juckte mich so sehr, dass ich ein Leserbrief verfasste, meine Meinung hat sich nicht geändert:
    
    Laut Untertitel des Artikels und indirekt der Umfrage vom House of Winterthur ist der Steuerfuss kein Thema für die lokalen Unternehmen. Dann will ich aber in Erinnerung rufen, dass Wärtsilä seit 2020 im Kanton Thurgau (Gewinnsteuersatz 13.21%) und Zimmer Biomet ebenfalls seit 2020 im Kanton Zug (Gewinnsteuersatz 11.85%) versteuern. Ich denke nicht, dass in diesen Unternehmen der Gewinnsteuersatz des Kantons Zürich (19.65%) keine Rolle spielt. Weiter hat der Kanton Zürich im Jahr 2021 satte 347 Firmen verloren, am zweitwenigsten mit 83 Verlusten steht der Kanton Bern (Gewinnsteuersatz 21.04%). Am zweitmeisten Zuzüge hat der Kanton Thurgau (87 Firmen). Nur der Kanton Wallis hat mit 120 Zuzügen (Gewinnsteuersatz 17.12%) mehr. Der Kanton Wallis zeigt, dass der Gewinnsteuersatz sicher nicht das einzige Kriterium für Zuzüge von Unternehmen ist, da der eigene Gewinnsteuersatz über dem schweizerischen Durchschnitt von 14.7% liegt. Clustereffekte, vorangetrieben durch Grossfirmen wie Lonza und einer meisterhaften Standortförderung sind unbestritten weitere Faktoren. Aber dennoch: Die Umfrage des House of Winterthur weist - sofern man die deskriptiven Zahlen stur interpretiert - eine klassische Auswahlverzerrung auf. Die Umfrage wäre aussagekräftiger, wenn man auch Unternehmen in die Umfrage miteinbezieht, welche nicht mehr in Winterthur versteuern oder sich bei einer Niederlassung in der Schweiz nicht für Winterthur entscheiden.
    Ich bin mir sicher. Der kantonale Gewinnsteuersatz ist für die Zukunft Winterthurs zentral. Im Westen ist Zürich das globale IT- und Finanzzentrum mit Top-Universitäten im Osten, der Kanton Thurgau mit einem 6% tieferem Gewinnsteuersatz. Stellen Sie sich vor, Sie hätten eine Unternehmung und würden sich im Grossraum Zürich - Ostschweiz niederlassen wollen. Würden Sie Winterthur wählen?
    """
)

st.markdown(
    """
    ### Wie lösen wir das Problem?
    
    Ganz einfach: Die kantonale Unternehmenssteuer muss auf den globalen Mindestsatz von 15% gesenkt werden. Winterthur hat das Potential wirtschafltich stark zu wachsen. Es gibt günstige Büroräume, eine lebendige Startups-Szene, Fachhochschulen und eine Bevölkerung die wohle lieber in der eigenen Stadt arbeiten würden als sich täglich in die überfüllten Züge in Richtung Zürich zu quetschen."""
)

#firmenabgäng https://www.tagesanzeiger.ch/kein-kanton-verliert-so-viele-firmen-wie-zuerich-257457694679
#steuerstatz https://home.kpmg/ch/de/home/medien/medienmitteilungen/2022/05/swiss-tax-report-2022.html