import streamlit as st

st.set_page_config(page_title="CV", page_icon="📄")

st.markdown("# CV kei Angst nid wie uf LinkedIn")
st.subheader("Auf SoMe kaum aktiv aber wird sich evtl. mal ändern")
st.sidebar.header("CV")

from pathlib import Path
from PIL import Image


# --- PATH SETTINGS ---

EMAIL = "guddal.jan@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "hhttps://www.linkedin.com/in/jan-guddal-a48671167/",
    "FaceBook": "https://www.facebook.com/jan.guddal",
    "Insta": "https://www.instagram.com/jguddal/",
    "Twitter": "https://twitter.com/GuddalJan"
}




# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- Kindheit ---
st.write('### **Kindheit**')

st.write(
    """
🇨🇭🇳🇴 Mutterseits aus Glarus, Vaterseits aus Norwegen, zogen nach Winterthur um bei Sulzer zu arbeiten. Da meine Eltern bedingt kreativ bei meinem Vornamen waren und wir die einzigen Guddals in der Schweiz sind war es nur logisch, dass mich alle Guddi nannten/nennen. Nicht zu verwechseln mit diesem [Gudi](https://www.youtube.com/watch?v=mnWtXf6A2TI).

⚽ 6 Jahre Primarschule im Schulhaus Altstadt. Alles ausser Fussball war unwichtig, leider war ich ein Holzfuss und musste daher wie alle anderen auch weiterhin zur Schule.
"""
)

# --- Jugend ---
st.write('### **Jugend**')

st.write(
    """
🤪 Die Einführung des neuen Eintragsystems an der St. Georgener Schule sollte die Disziplin verbessern. Doch die Folgen waren verheerend. Aus meiner Sicht, trieb das Eintragsystems viele Schüler in die Verzweiflung und sogar in die Sucht.

Das neue Eintragsystem erlaubte Lehrkräften die minutiöse Dokumentation kleinster Vergehen (Hausaufgaben vergessen, Mütze im Unterricht usw.) in verschiedenen Kategorien. Je nach Kategorie drohten Konsequenzen wie schlechte Noten im Verhalten oder Verweise bei wiederholten Verstößen.

Ich will nichts beschönigen, ja, ich war als Schüler in dieser Zeit verdammt lästig und habe ständig den Unterricht gestört. Aber ich habe nie jemanden verprügelt (klar, es gab hin und wieder Nackenschläge), oder eine Lehrperson direkt beleidigt und war immer pünktlich. Mein damaliges Verhalten äußerte sich vor allem darin, als Klassenclown für Unruhe zu sorgen.

Mit einigen meiner damaligen Kollegen stehe ich noch in Kontakt. Es waren etwa 120 Schüler oder 60 männliche Schüler im Schulhaus. Ich weiß allein von vier Personen (eine davon mit Suizidversuch), die später einen Klinikaufenthalt hatten, und ich bin überzeugt, dass mindestens 10 weitere ein massives Drogenproblem haben und früher oder später auch in der Klinik landen werden, also über 1/6 der Männer. Und ja, ich denke, dass das Eintragssystem dabei eine große Rolle gespielt hat. Jungs sind in der Pubertät anders als Mädchen, die meisten brauchen mehr Bewegung, und so ist es nicht verwunderlich, dass der Prozentsatz der weiblichen Maturanden 60 % und derjenige der Jungs 40 % beträgt. 

Das Hauptproblem mit dem Eintragsystem war vor allem, dass sobald das Kreuz im Zeugnis an der falschen Stelle stand, keine Verbesserungen mehr vorgenommen werden konnten. Scheisse bauen war also angesagt, sobald dies der Fall war, weil es sowieso keine Rolle mehr spielte. Auch wenn wir damals untereinander mit unseren Einträgen geprahlt haben, bin ich mir sicher, dass sie uns psychisch fertig gemacht haben. Die Schule gab uns das Gefühl, dass die Gesellschaft uns nicht gebrauchen konnte, dass alles was wir taten, falsch war. Viele meiner Kollegen begannen in dieser Zeit exzessiv zu kiffen, ich glaube, das war ihre Art, sich ruhig zu stellen, in die Klasse zu passen, nicht aufzufallen. Cannabis ist per se weniger gefährlich als Alkohol. Aber das Problem mit Cannabis ist, man kann regelmäßig bekifft zur Schule gehen und die Lehrkräfte störrt es nicht, während man betrunken sofort auffallen würde. Ich glaube dass die Kombination, von einem System welches Schüler welche grosse Probleme haben sich ruhig zu verhalten hart bestraft und die beruhigende Wirkung des THCs, für viele meiner Kollegen der Einstieg in die Sucht waren.

Ich selbst hatte das Glück, dass Cannabis für mich nie wirklich attraktiv war. Der Flash war einfach zu langweilig. Andererseits konnte ich mich auch nicht ruhig stellen und flog schliesslich von der Schule ins Timeoutprojekt "Trampolin".


Zusammengefasst trieb das Eintragsystem viele meiner Mitschüler in die Verzweiflung. Es führte zu einem Gefühl der Wertlosigkeit und trug meiner Meinung nach maßgeblich zu psychischen Problemen und Drogenabhängigkeit bei. Diese Erlebnisse haben mich tief geprägt und sind der wohl größte Motivationsfaktor für mein politisches Wirken. Ich bin fest davon überzeugt, dass die Schule für junge Männer, aber auch für alle Schüler generell, besser angepasst werden muss. Besonders wichtig ist mir dabei die Förderung von Bewegung. Junge Menschen, insbesondere Jungs in der Pubertät, brauchen mehr Möglichkeiten, sich auszutoben und Energie abzubauen. Ein starres Sitzen im Unterricht über Stunden hinweg kann zu Frustration und Konzentrationsschwierigkeiten führen. Stattdessen sollten Schulen Bewegungskonzepte integrieren, die den natürlichen Bewegungsdrang der Schüler aufgreifen und in den Lernprozess einbeziehen. Darüber hinaus muss das Schulsystem individuellen Interessen und Stärken mehr Raum geben. Französisch ist immer noch pflicht, während die Welt immer digitaler wird. Weshalb sollte man Französisch zugunsten Informatik nicht abwählen dürfen?

⌛ Das Trampolin war ein Timeoutprojekt. Es bedeutete: Weg von der Schule, hin zu handwerklichem Arbeiten. Dieses Projekt half mir enorm. Hier bekam ich endlich das Gefühl, doch noch etwas wert zu sein, während die Lehrkräfte sich von mir erholen konnten. Parallel dazu begann ich im Club Basketball zu spielen, nahm Ritalin ein und hatte bald meine erste Freundin. All diese Faktoren zusammen gaben mir schließlich die richtige Richtung.

🤓 Eigentlich wollte ich eine Lehre absolvieren. Die Schule hatte mich mehr als satt. Mein Zeugnis war aufgrund der Zeit, die ich auf dem Trampolin verbracht hatte, allerdings keine Augenweide für das HR-Personal. Daher dachte ich mir, ich versuche es noch einmal mit der Gymiprüfung. Denn vom Gymnasium aus hatte ich bessere Chancen auf eine Lehrstelle als mit einem Abschluss der 10. Schulstufe. Ich bestand die Gymiprüfung und merkte schnell, dass das Gymnasium eine ganz andere Welt war. Provokationen wurden von den Lehrern gerne in den Unterricht aufgenommen, statt bestraft zu werden. Der Inhalt und das Tempo des Unterrichts sagten mir deutlich mehr zu. So entschied ich mich, das Gymnasium zu absolvieren.
"""
)

# --- Zwischenjahr ---
st.write('### **Zwischenjahr**')

st.write(
    """
🛎️ Um Geld für mein Zwischenjahr zu verdienen, arbeitete ich im Tres Amigos. Das Team war super, die Arbeitsbedingungen allerdings eher bescheiden. Fehler wie falsche Bestellungen tippen oder heruntergefallenes Essen wurden vom eigenen Gehalt abgezogen und auch sonst waren Verstöße gegen das Arbeitsgesetz an der Tagesordnung. Schliesslich gaben mir diese negativen Erfahrungen den Antrieb, ein Studium anzustreben, obwohl ich nie genau wusste, was ich studieren sollte...

🚅 Mit dem verdienten Geld gönnte ich mir einen dreimonatigen Sprachaufenthalt in Kalifornien und reiste anschließend noch ein bisschen mit Interrail durch Europa. Schnell stellte ich fest, dass ich eigentlich doch gerne beschäftigt bin, sei es durch Arbeit oder Schule. Ich bin einfach nicht der Typ, der monatelang planlos herumreisen kann. Irgendwann fühlt sich das Reisen wie Arbeit an. Im Hostel hat man immer dieselben Konversationen, und Sehenswürdigkeiten  werden nur noch abgehakt, um sagen zu können, man habe sie gesehen. Zumindest ging es mir so. Versteht mich nicht falsch, ich reise immer noch sehr gerne, aber nach drei Wochen am Stück ist dann auch wieder gut für ein paar Monate."""
)

# --- Uni ---
st.write('### **Uni**')

st.write(
    """
🎓 Ich wusste nie was ich studieren sollte, als Mutter dann sagte einschreiben oder raus, schrieb ich mich bei Geografie ein. Geografie ist gefährlich. Es ist ein einfaches Studium, man ist sehr generell, vertieft sich aber nie, man muss sich zwingend vertiefen sonst landet man auf dem RAV. Zum guten Glück kam mir via GIS die Informatik über den Weg. Definitiv das Studium welches ich im Nachhinein gewählte hätte. Geographie ist aber extrem kulant was Nebenfächer angeht. Folglich konnte ich mir während dem Studium genügend IT-Skills aneignen um anschliessend auch einen Job in der IT zu finden.

🛠️ Während dem Bachelor arbeitet ich als Promoter und Logistiker für diverse Firmen. Lohn war gut, Arbeit flexibel, bringt nichts im CV kann ich aber durchaus empfehlen. Im Master arbeitete ich 40% in einem Ingenieurbüro mit Fokus auf Lärmarmestrassenbeläge. Gut für den CV, aber noch wichtiger war für mich zu merken, dass ich doch nicht in ein Ingenieurbüro will und investierte daher viel Zeit in die Informatik.

🧳 Austauschsemester kann ich wärmstens empfehlen. Im Bachelor war ich 6 Monate in Birmingham. Bezüglich Partys etc. kann man dort in 6 Monaten so viel erleben wie in einer durchschnittlichen schweizer Jugend. War top, könnte es aber nie wieder tun. Im Master ging ich nach Genf, um Französisch zu lernen, zum Glück war alles auf English, adieau Francais ;). In Genf war ich aber hart im Strebermodus 24/7 Bibliothek, da ich ja eben nicht in ein Igenieurbüro wollte. Die Kurse waren super und fachlich war es die wohl lehrreichste Zeit für mich.
"""
)


# --- Arbeit ---
st.write('### **Arbeit**')

st.write(
    """
🏢 Ich hatte das Glück genau gleichzeitig mit COVID in den Arbeitsmarkt einzutreten, bzw. Homeoffice. Ich war insgesamt bei vier verschiedenen Corpoorates im Praktikum. Ehe ich bei Intervista landete. Dort haben wir ein Panel mit ca. 4000 Personen die permanent geolokalisiert werden. Datenschutz mässig brisant, aber um eine Doppelmoral zu vermeiden, habe ich mich auch in dieses Panel eingeschrieben. Ich mag meinen Job, da wir sehr spannende Daten haben und in verschiedenen Bereichen (Aussenwerbung, Mobilität, Tourismus) Aufträge erledigen dürfen.

"""
)

# --- Startups ---
st.write('### **Startups**')

st.write(
    """
🚀Die Startup-Szene war für mich lange Zeit ein Synonym für Hochstapelei – ein Vorurteil, das ich, wie ich gestehen muss, teilweise auch heute noch teile. Angesichts der prekären wirtschaftlichen Situation in Winterthur war ich jedoch froh um die Startup Night und meldete mich kurzerhand als Helfer an.

Meine anfänglichen Zweifel verflogen schnell. Klar, ein gewisses Maß an Selbstdarstellung gehört in dieser Branche zum Geschäft, schließlich muss man Investoren und Kunden überzeugen. Dennoch erlebte ich die meisten Akteure als bodenständige und hart arbeitende Menschen.

Aktuell bin ich sogar selbst Teil der Startup-Welt. In einem stundenlohnbezahlten Job bei einem jungen Unternehmen arbeite ich mit daran, Fußballtransfers mithilfe von Crowdfunding zu ermöglichen. Die Idee begeistert mich und ich bin vom Erfolg des Projekts überzeugt. Daher habe ich sogar einen kleinen Anteil an Aktien erworben
"""
)
