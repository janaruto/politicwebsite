import streamlit as st
import pandas as pd
import altair as alt
from urllib.error import URLError

st.set_page_config(page_title="Kapitalismus", page_icon="💰")

st.markdown("# Kapitalismus Pro & Contra")
st.sidebar.header("Kapitalismus")

st.write("## Pro")
from PIL import Image
image = Image.open('apps/images/stonks.png')
st.image(image)
st.write(
    """
    Ich verstehe Kapitalismus als eine Form der Wirtschaft und Gesellschaft auf der Grundlage des freien Wettbewerbs und des Strebens nach Kapitalbesitz des Einzelnen. Dabei sind ***Nachfrage, Angebot und Wettbewerb*** sind drei Schlüsselelemente, die für das Funktionieren einer kapitalistischen Wirtschaft unerlässlich sind. Daraus resultieren unteranderem folgende Vorteile:
    - ***Effizienz***: Die Kräfte der Nachfrage und des Angebots sind wichtig, um sicherzustellen, dass Waren und Dienstleistungen effizient produziert und verteilt werden. Die Interaktion zwischen Käufern und Verkäufern bestimmt die Preise von Waren und Dienstleistungen, was wiederum den Produzenten ein Signal über die Höhe der Nachfrage nach ihren Produkten gibt. Dies trägt dazu bei, die Ressourcen so effizient wie möglich zu verteilen und sicherzustellen, dass die richtigen Waren und Dienstleistungen zur richtigen Zeit und in der richtigen Menge produziert werden.
    - ***Innovation***: In einem wettbewerbsorientierten Markt suchen die Hersteller ständig nach Möglichkeiten, ihre Produkte von denen der Konkurrenz abzuheben. Dies schafft ein Umfeld, in dem die Unternehmen einen Anreiz haben, in Forschung und Entwicklung zu investieren, was zu neuen und verbesserten Produkten führen kann. Dies wiederum kommt den Verbrauchern zugute, die Zugang zu einer größeren Auswahl und besseren Produkten haben.
    - ***Souveränität der Verbraucher***: In einer kapitalistischen Wirtschaft haben die Verbraucher die Macht zu bestimmen, welche Produkte hergestellt und auf dem Markt verkauft werden. Die Unternehmen müssen auf die Bedürfnisse und Wünsche der Verbraucher eingehen, um wettbewerbsfähig zu bleiben. Dies bedeutet, dass die Verbraucher eine breite Palette von Optionen zur Auswahl haben und Produkte auswählen können, die ihren Bedürfnissen am besten entsprechen.
    - ***Preisstabilität***: Die Kräfte von Angebot und Nachfrage können dazu beitragen, dass die Preise auf dem Markt stabil bleiben. Wenn die Nachfrage nach einem bestimmten Produkt steigt, wird auch sein Preis steigen. Dies wiederum bietet den Herstellern einen Anreiz, das Angebot dieses Produkts zu erhöhen, wodurch der Preis wieder sinken kann. Dieser selbstkorrigierende Mechanismus trägt dazu bei, extreme Preisschwankungen zu verhindern.
    - ***Wirtschaftswachstum***: Der Wettbewerb zwischen Unternehmen und die ständige Suche nach neuen und besseren Produkten kann zu Wirtschaftswachstum führen. Dies wiederum schafft Arbeitsplätze und kann dazu beitragen, den Lebensstandard zu erhöhen.

    Grundsätzlich sehe ich mich als Verfechter des Kapitalismus, einerseits aus den zuvor erwähnten Gründen aber vor allem auch weil:
    - ***Mangelnde Alternativen*** In Theorie mögen mehrere Wirtschafts- bzw. Gesellschaftsformen einen besseren Eindruck hinterlassen. Ich warte bis heute auf einen entwickelten Staat welcher ein solche Form längerfristig erfolgreich umsetzt(e).
    - ***Innovation*** Kapitalismus ist unumstritten der grösste Treiber für menschliche Innovation. Theoretisch (dazu später mehr) macht es unsere Leben einfacher, gibt uns mehr Freizeit, mehr Optionen unser Leben zu gestalten, eine höhere Lebenserwartung etc.
    - ***Alle profitieren*** Ja die Vermögensschere geht weiter auf. Nein das ist nicht gut. Aber wenn wir unser Leben mit denjenigen unserer Grosseltern vergleichen (mit Praktikumslohn Ferien in Südamerika, 4-Tage vs 6-Tage Arbeit etc.) dann geht es uns definitiv besser.
    """)

st.write("## Contra")
image = Image.open('apps/images/equality.png')

st.write(
    """
    Die oben genannten Vorteile kommen nur dann zur Geltung, wenn folgende Prinzipien garantiert sind:
    - ***Chancengleichheit*** Chancengleichheit - nicht zu verwechseln mit Ergebnisgleichheit - ist unabdingbar für den Kapitalismus. Chancengleichheit bedeutet, dass jeder die gleiche Chance auf Erfolg haben sollte, unabhängig von seinem Hintergrund oder seinen Umständen. In einer kapitalistischen Wirtschaft ist dies wichtig, weil es dazu beiträgt, dass die talentiertesten und motiviertesten Menschen unabhängig von ihrem sozialen oder wirtschaftlichen Status erfolgreich sein können. Dies wiederum trägt dazu bei, dass die Wirtschaft ihr höchstes Potenzial ausschöpft und die talentiertesten Personen Unternehmen leiten und Innovationen vorantreiben. Ergebnisgleichheit hingegen bedeutet, dass alle Menschen unabhängig von ihren Fähigkeiten oder Anstrengungen den gleichen Erfolg oder die gleiche Belohnung erhalten sollten. Dies ist nicht dasselbe wie Chancengleichheit, denn es berücksichtigt nicht die Unterschiede in den Fähigkeiten, der Motivation oder den Anstrengungen der Einzelnen. In einer kapitalistischen Wirtschaft kann dieser Ansatz sogar kontraproduktiv sein, denn er kann die Anreize für den Einzelnen verringern, hart zu arbeiten, innovativ zu sein oder Risiken einzugehen. Dies wiederum kann zu einer weniger dynamischen und weniger wohlhabenden Wirtschaft führen. Die Chancengleichheit ist aber aus meiner Sicht nicht immer gegeben. Zum Beispiel sind Privatschulen/Nachhilfen Haushalten mit geringem Einkommen kaum zugänglich. Solche Ungerechtigkeiten müssen behoben werden.
    - ***Erben*** Hier vor allem in Bezug auf die Chancengleichheit. Klar sollte man in der Schweiz keine Erbschaftssteuer erheben, da dann vor allem reiche Familien im Ausland vererben werden. Es müsste eine globale Mindeststeuer geben (wie bei den Unternehmen) und die Schweiz sollte den Mindestsatz national festlegen.
    - ***Budget politischer Parteien*** Es darf nicht sein, dass bestimmte Parteien mehr Budget zur Werbung zur Verfügung haben als andere. Alle Parteien sollte gleich lange Spiese haben, alles andere ist ein Steilpass für Lobbyisten.
    - ***Transparenz*** Transparenz kann dazu beitragen, Betrug und Korruption im Wirtschaftssystem zu verhindern. Wenn Unternehmen und Regierungen ihre Tätigkeiten transparent machen, wird es für Einzelpersonen schwieriger, sich an illegalen oder unethischen Aktivitäten zu beteiligen. Außerdem können die Beteiligten Betrug und Korruption aufdecken und melden, wenn sie auftreten, was dazu beitragen kann, diese Verhaltensweisen in Zukunft zu verhindern.
    - ***Sucht*** süchtig machende Produkte wie Tabak oder Glücksspiel, haben das Potenzial, viel Geld zu verdienen. Diese Produkte können jedoch negative Auswirkungen auf den Einzelnen und die Gesellschaft als Ganzes haben. Nebst gesundheitlichen Risiken können Suchtmittel auch negative soziale und wirtschaftliche Folgen haben. Glücksspielsucht kann beispielsweise zum finanziellen Ruin und zum Zusammenbruch der Familie führen, während Alkoholsucht das Urteilsvermögen beeinträchtigt und das Unfallrisiko erhöht. Darüber hinaus können süchtig machende Produkte einen Kreislauf der Abhängigkeit schaffen, der nur schwer zu durchbrechen ist. Wer einmal von einem Produkt abhängig geworden ist, kann nur schwer wieder damit aufhören, was zu langfristigen gesundheitlichen Problemen und finanziellen Schwierigkeiten führen kann. Darüber hinaus kann die Vermarktung von Suchtmitteln sehr gezielt und manipulativ sein, was dazu führen kann, dass gefährdete Personen überhaupt erst süchtig werden.
    """)

st.write("## Fakten")
image = Image.open('apps/images/capitalism.png')
st.image(image, caption='bitte sei nicht der Linke')
st.write(
    """
    - In Aktien bzw. passive Indexfund anzulege lohnt sich! Die Graphik zeigt die reale, das heisst inflationsadjustierte Wertentwicklung von CHF-Obligationen und von Schweizer Aktien. Aus ihr geht hervor, dass mit Obligationen aufgrund der reinvestier- ten Verzinsung über die 72-jährige Periode seit Ende 1925 ein Vermögen resultierte, das kaufkraftmässig dem 4.5-fachen der Anfangsinvestition entsprach. Dies steht einem auf das 66.30-fache angestiegenen realen Vermögen mit Aktien gegenüber. Wer sich vertieft mit dem Thema anlegen befassen will, dem kann ich dieses [Buch](https://www.orellfuessli.ch/shop/home/artikeldetails/A1059799699) empfehlen.
    """
    )
image = Image.open('apps/images/pictet.png')
st.image(image, caption='Quelle: Historische Performance von Schweizer Aktien und Schweizerfranken-Obligationen (1926-2022) Banque Pictet & Cie SA')

st.write(
    """
    - Finde ich es fair, dass jemand ein Milliarden Vermögen hat, andere gar nichts haben und diese Ungleichheit grösser wird? Nein! Aber, global sinkt die Armut:
    """
    )
image = Image.open('apps/images/poverty.png')
st.image(image)

st.write(
    """
    - Die obersten 10% Prozente zahlen in der Schweiz mehr als die Hälfte aller Steuern.
    """
    )
image = Image.open('apps/images/steuern.png')
st.image(image)

st.write(
    """
    - Grosse Vermögen erben (gerade Imbolienportfolios) finde ich fraglich. Dennoch laut [Studien](https://www.gsb.stanford.edu/alumni/news/books/preparing-heirs) verliert eine Familie ihr Vermögen in 90 Prozent der Fällen innerhalb drei Generationen 
    """
    )