import streamlit as st
import pandas as pd
import altair as alt
from urllib.error import URLError

st.set_page_config(page_title="Winterthur & Kultur", page_icon="🎭")

st.markdown("# Winterthur & Kultur")
st.sidebar.header("Winterthur & Kultur")

st.write("## Meine Meinung zur Winterthurer Kultur")
from PIL import Image
image = Image.open('apps/images/kultur.png')
st.image(image)

st.write(
    """Winterthurs Kulturszene besticht durch ihre facettenreiche und lebendige Natur, geprägt von einem alternativen, bescheidenen und zugleich kreativen Charakter, der durch Angebote wie OnThur, die Musikfestwochen und dem FCW verkörpert wird.

Obwohl der Wunsch nach einer stärkeren finanziellen Unterstützung der Kultur weit verbreitet ist, darf die prekäre Finanzsituation der Stadt Winterthur nicht ausser Acht gelassen werden. Was ist einem wichtiger? Ein zweites Hallenbad?, Die Schützenwiese UEFA-konform umbauen? Die Kultursubventionen erhöhen?

Auch wenn man klar dafür ist, dass die Subvention für Kulturschaffende in Winterthur erhöht werden sollten, wirft für mich die derzeitige Verteilung der Kulturgelder nach wie vor Fragen auf. Während Angebote wie OnThur einen breiten Bevölkerungsteil ansprechen, scheint die Vergabe der Gelder anders gelagert zu sein. Daher setze ich mich für eine direktere Mitbestimmung der Bevölkerung bei der Verteilung der Kulturgelder ein.

Die Zeiten, in denen Künstler aufgrund von "nicht erkanntem Talent" oder "verbotenem Gedankengut" gefördert oder geschützt werden mussten, sind vorbei. In unserer offenen Gesellschaft wird Kunst respektiert, und Talente finden Möglichkeiten zu florieren.

Daher plädiere ich für eine Kulturpolitik, die den Fokus auf die Bereitstellung von zusätzlichen Räumen für Kulturschaffende legt. Kunstschaffenden soll es erleichtert werden, ihre Projekte auf Winterthurer Boden zu verwirklichen. Dies erscheint mir langfristig sinnvoller, als unterdurchschnittliche Kunst mit Steuergeldern am Leben zu erhalten.

Darüber hinaus dominiert einseitig linke Rhetorik die Winterthurer Kulturszene. Es ist fraglich, ob die Finanzierung von vorwiegend linksgerichteten Kunstschaffenden durch Steuergelder die gewünschte Vielfalt tatsächlich fördert. Vielmehr sollte man sich an den Idealen der Linken orientieren und Diversität anstreben, wobei dies nicht nur im physischen, sondern vor allem im psychischen Sinne zu verstehen ist. SP-Wähler*innen würden es wohl kaum begrüssen, wenn ihre Steuergelder vor allem für die Subventionierung politisch rechtsgerichteter Kultur verwendet würden.

Die zentrale Frage bleibt: Benötigt die Winterthurer Kultur mehr Geld? Ehrlich gesagt, ich weiss es nicht. Ich bin mir aber sicher, dass sich die Winterthurer Kultur gerade durch ihren "Low-Budget-Vibe" auszeichnet. Das Zürcher Kunsthaus ist für mich schlichtweg weniger ansprechend, als der Salon Erika. Ich wage die steile Hypothese: Wenn Winterthur die Kultursubventionen signifikant steigern würde, könnte sie langfristig ihre eigene Identität verlieren.""")