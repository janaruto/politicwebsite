import streamlit as st
import base64

st.set_page_config(page_title="CV", page_icon="📄")

st.markdown("# CV - kei Angst nid wie uf LinkedIn")

video_file = open('apps/data/raw/cvWeb.mp4', 'rb')
video_bytes = video_file.read()

st.video(video_bytes, loop=True)

st.subheader("Auf SoMe kaum aktiv aber wird sich evtl. mal ändern")
st.sidebar.header("CV")

from pathlib import Path
from PIL import Image


# --- PATH SETTINGS ---

EMAIL = "guddal.jan@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/jan-guddal-a48671167/",
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

❌ Aufnahmeprüfung fürs Gymnasium nicht bestanden → Sekundarschule St.Georgen
"""
)

# --- Jugend ---
st.write('### **Jugend**')

st.write(
    """
🤪 Die Einführung des neuen Eintragsystems im St.Georgen Schlhaus sollte die Disziplin verbessern. Doch die Folgen waren verheerend. Aus meiner Sicht, trieb das Eintragsystems viele Schüler in die Sucht.

Das neue Eintragsystem erlaubte Lehrkräften die minutiöse Dokumentation kleinster Vergehen (Hausaufgaben vergessen, Mütze im Unterricht usw.) in verschiedenen Kategorien. Je nach Kategorie drohten Konsequenzen wie schlechte Noten im Verhalten oder Verweise bei wiederholten Verstössen.

Ich will nichts beschönigen, ja, ich war als Schüler in dieser Zeit verdammt lästig und habe ständig den Unterricht gestört. Aber ich habe nie etwas wirklich schlimmes, wie jemanden richtig verprügelt, verbrochen. Mein damaliges Verhalten äusserte sich vor allem darin, als Klassenclown für Unruhe zu sorgen.

Mit einigen meiner damaligen Kollegen stehe ich noch in Kontakt. Es waren etwa 120 Schüler oder 60 männliche Schüler im Schulhaus. Ich weiss allein von vier Personen (eine davon mit Suizidversuch), die später einen Klinikaufenthalt hatten, und ich bin überzeugt, dass mindestens 10 weitere ein massives Drogenproblem haben und früher oder später auch in der Klinik landen werden, also über 1/6 der Männer. Und ja, ich denke, dass das Eintragssystem dabei eine grosse Rolle gespielt hat. Jungs sind in der Pubertät anders als Mädchen, die meisten brauchen mehr Bewegung, und so ist es nicht verwunderlich, dass der Prozentsatz der weiblichen Maturanden 60 % und derjenige der Jungs 40 % beträgt. 

Das Hauptproblem mit dem Eintragsystem war vor allem, dass sobald das Kreuz im Zeugnis an der falschen Stelle stand, keine Verbesserungen mehr vorgenommen werden konnten. Scheisse bauen war also angesagt, sobald dies der Fall war, weil es sowieso keine Rolle mehr spielte. Auch wenn wir damals untereinander mit unseren Einträgen geprahlt haben, bin ich mir sicher, dass sie uns psychisch fertig gemacht haben. Die Schule gab uns das Gefühl, dass die Gesellschaft uns nicht gebrauchen konnte, dass alles was wir taten, falsch war. Viele meiner Kollegen begannen in dieser Zeit exzessiv zu kiffen, ich glaube, das war ihre Art, sich ruhig zu stellen, in die Klasse zu passen, nicht aufzufallen. THC ist per se weniger gefährlich als Alkohol. Aber das Problem mit THC ist, man kann regelmässig bekifft die Schule besuchen, denn die Lehrkräfte störrt es nicht, während man betrunken sofort auffallen würde. Ich glaube dass die Kombination, von einem System welches Schüler welche grosse Probleme haben sich ruhig zu verhalten hart bestraft und die beruhigende Wirkung des THCs, für viele meiner Kollegen der Einstieg in die Sucht war. Diese Erlebnisse haben mich tief geprägt und sind der wohl grösste Motivationsfaktor für mein politisches Wirken.

Ich selbst hatte das Glück, dass THC für mich nie wirklich attraktiv war. Der Flash war einfach zu langweilig. Andererseits konnte ich mich auch nicht ruhig stellen und flog schliesslich von der Schule ins Timeoutprojekt "Trampolin".

⌛ Das Trampolin war ein Timeoutprojekt. Es bedeutete: Weg von der Schule, hin zu handwerklichem Arbeiten. Dieses Projekt half mir enorm. Hier bekam ich endlich das Gefühl, doch noch etwas wert zu sein, während die Lehrkräfte sich von mir erholen konnten. Parallel dazu begann ich im Club Basketball zu spielen, nahm Ritalin ein und hatte bald meine erste Freundin. Die Kombination dieser Faktoren gaben mir schliesslich die richtige Richtung.

🤓 Ursprünglich wollte ich eine Lehre machen, da ich die Schule mehr als satt hatte. Doch mein Zeugnis, geprägt von der Zeit vor meinem Trampolin-Timeout, war für jedes HR-Departement abschreckend, sodass mich niemand einstellen wollte. Deshalb entschloss ich mich, die Aufnahmeprüfung fürs Gymnasium zu absolvieren, da man vom Gymnasium aus bessere Chancen auf eine Lehrstelle hat als aus dem 10. Schuljahr. Ich bestand die Prüfung und stellte schnell fest, dass das Gymnasium eine ganz andere Welt war. Provokationen wurden von den Lehrern gerne in den Unterricht integriert, anstatt bestraft zu werden. Der Inhalt und das Tempo des Unterrichts sagten mir deutlich mehr zu. Daher entschied ich mich, das Gymnasium zu absolvieren.
"""
)

# --- Zwischenjahr ---
st.write('### **Zwischenjahr**')

st.write(
    """
🛎️ Um Geld für mein Zwischenjahr zu verdienen, arbeitete ich im Tres Amigos. Das Team war super, die Arbeitsbedingungen allerdings eher bescheiden. Fehler wie falsche Bestellungen tippen oder heruntergefallenes Essen wurden vom eigenen Gehalt abgezogen und auch sonst waren Verstösse gegen das Arbeitsgesetz an der Tagesordnung. Schliesslich gaben mir diese negativen Erfahrungen den Antrieb, ein Studium anzustreben, obwohl ich nie genau wusste, was ich studieren sollte...

🚅 Mit dem verdienten Geld gönnte ich mir einen dreimonatigen Sprachaufenthalt in Kalifornien und reiste anschliessend noch ein bisschen mit Interrail durch Europa. Schnell stellte ich fest, dass ich eigentlich doch gerne beschäftigt bin, sei es durch Arbeit oder Schule. Ich bin einfach nicht der Typ, der monatelang planlos herumreisen kann. Irgendwann fühlt sich das Reisen wie Arbeit an. Im Hostel hat man immer dieselben Konversationen, und Sehenswürdigkeiten  werden nur noch abgehakt, um sagen zu können, man habe sie gesehen. Zumindest ging es mir so. Versteht mich nicht falsch, ich reise immer noch sehr gerne, aber nach drei Wochen am Stück ist dann auch wieder gut für ein paar Monate."""
)

# --- Uni ---
st.write('### **Uni**')

st.write(
    """
🎓 Ich wusste nie was ich studieren sollte, als Mutter dann sagte einschreiben oder raus, schrieb ich mich bei Geografie ein. Geografie ist gefährlich. Es ist ein einfaches Studium, man ist sehr generell und vertieft sich nie richtig wenn man klar dem Lehrplan folgt. Zum guten Glück kam mir via GIS die Informatik über den Weg. Definitiv das Studium welches ich im Nachhinein gewählte hätte. Geografie ist aber extrem kulant was Nebenfächer angeht. Folglich konnte ich mir während dem Studium genügend IT-Skills aneignen um anschliessend auch einen Job in der IT zu finden.

🛠️ Während dem Bachelor arbeitet ich als Promoter und Logistiker für diverse Firmen. Lohn war gut, Arbeit flexibel, bringt nichts im CV kann ich aber durchaus empfehlen. Im Master arbeitete ich 40% in einem Ingenieurbüro mit Fokus auf Lärmarmestrassenbeläge. Gut für den CV, aber noch wichtiger war für mich zu merken, dass ich doch nicht in ein Ingenieurbüro will und investierte daher viel Zeit in die Informatik.

🧳 Austauschsemester kann ich wärmstens empfehlen. Im Bachelor war ich 6 Monate in Birmingham. Bezüglich Partys etc. kann man dort in 6 Monaten so viel erleben wie in einer durchschnittlichen schweizer Jugend. War top, könnte es aber nie wieder tun. Im Master ging ich nach Genf, um Französisch zu lernen, zum Glück war alles auf English, adieau Francais ;). In Genf war ich aber hart im Strebermodus 24/7 Bibliothek, da ich ja eben nicht in ein Igenieurbüro wollte. Die Kurse waren super und fachlich war es die wohl lehrreichste Zeit für mich.
"""
)


# --- Arbeit ---
st.write('### **Arbeit**')

st.write(
    """
🏢 Ich hatte das Glück genau gleichzeitig mit COVID in den Arbeitsmarkt einzusteigen, bzw. Homeoffice. Ich war insgesamt bei vier verschiedenen Corpoorates im Praktikum. Ehe ich bei Intervista landete. Dort haben wir ein Panel mit ca. 4000 Personen die permanent geolokalisiert werden. Datenschutz mässig brisant, aber um eine Doppelmoral zu vermeiden, habe ich mich auch in dieses Panel eingeschrieben. Ich mag meinen Job, da wir sehr spannende Daten haben und in verschiedenen Bereichen (Aussenwerbung, Mobilität, Tourismus) Aufträge erledigen dürfen.

"""
)

# --- Startups ---
st.write('### **Startups**')

st.write(
    """
🚀Ich hatte lange Zeit wenig bis keinen Kontakt zur Startup-Szene. Auf LinkedIn wirkten die meisten Vertreter auf mich eher narzisstisch. Angesichts der prekären wirtschaftlichen Situation in Winterthur war ich jedoch dankbar für die Startup Night und meldete mich kurzerhand als Helfer an.

Meine anfänglichen Zweifel verflogen schnell. Ich begann zu verstehen, warum so viel Selbstdarstellung in dieser Branche nötig ist – schliesslich müssen Investoren und Kunden überzeugt werden. Abseits des Verkaufens erlebte ich die Akteure als bodenständige und hart arbeitende Menschen.

Mittlerweile bin ich selbst Teil der Startup-Welt. In einem stundenlohnbezahlten Job bei einem jungen Unternehmen arbeite ich daran, [Fussballtransfers mithilfe von Crowdfunding](https://crowdtransfer.io) zu ermöglichen. Die Idee begeistert mich, und ich bin vom Erfolg des Projekts überzeugt. Daher habe ich sogar einen kleinen Anteil an Aktien erworben.
"""
)
