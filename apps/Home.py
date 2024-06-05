import streamlit as st

st.set_page_config(
    page_title="Jan Guddal",
    page_icon="🌱🔵",
)

import streamlit as st


st.write("# Luegd das also doch no öpper anders ussert ich ah?! 🤯")

st.sidebar.success("Meine Meinung zu bestimmten Themen, einfach klicken für Insights")

from PIL import Image
image = Image.open('apps/images/me.png')


st.image(image, caption='DISCLAIMER, sieht auf Foto freundlicher aus als in echt')

st.markdown(
    """
    ### Was passt denn em Guddi nid 😌?
    Einer der Hauptgründe, warum ich mich aktiv in der Politik engagieren möchte, ist die Erkenntnis, dass die Jobaussichten in Winterthur nach dem Studium eher schlecht sind. Viele meiner Kolleginnen und Kollegen teilen diese Ansicht und sind bereits nach Zürich gezogen oder spielen mit dem Gedanken, dies zu tun. Ich persönlich bin ein überzeugter Lokalpatriot und möchte keinesfalls nach Zürich ziehen, auch wenn die Stadt mit ihrer internationalen Ausstrahlung, dem See, den vielen interessanten Arbeitsplätzen und den umliegenden steuergünstigen Gemeinden durchaus ihren Reiz hat.

    Sollte Winterthur weiterhin hoch verschuldet bleiben und die Erhöhung des Steuerfusses die einzige kreative Lösung der Stadt sein, um dieses Problem zu bewältigen, könnte auch ich irgendwann gezwungen sein, meine Haltung zu überdenken. Auch wenn ich es mir kaum vorstellen kann, da ich die MFW, den FCW und viele andere Aspekte dieser Stadt sehr schätze, bin ich noch jung und es kann sich viel ändern.

    Ich möchte jedoch alles daran setzen, die Attraktivität und Lebensqualität Winterthurs zu erhalten und zu verbessern, sodass unsere Stadt auch für zukünftige Generationen ein lebenswerter Ort bleibt.
    
    Ein weiterer Grund sind persönliche Erfahrungen, die mich geprägt haben. Ich weiß, dass eine solide Wirtschaft nicht die einzige Grundlage für eine funktionierende Gesellschaft ist. Die Lebensqualität, die sich aus sozialen, sportlichen und kulturellen Angeboten ergibt, ist mindestens genauso wichtig. Während meiner Zeit in der Sekundarschule St. Georgen musste ich eine Auszeit nehmen. Das Trampolin und die Sportangebote des BCW halfen mir, die richtige Richtung für meine Entwicklung zu finden.

    Deshalb interessiere ich mich besonders für die Bereiche Bildung, Sozialarbeit und Sport. Ich sehe sie als wesentliche Säulen einer Gesellschaft, die nicht in Gewinner und Verlierer unterteilt, sondern versucht, allen einen Platz zu geben.
    """
)

image = Image.open('apps/images/Smartspider.png')
st.write("### Smartspider")

st.image(image)

import base64
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
#add_bg_from_local('images/schuetzi_grey.jpg')