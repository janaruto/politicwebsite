import streamlit as st

st.set_page_config(
    page_title="Jan Guddal",
    page_icon="🌱🔵",
)

st.write("# Luegd das also doch no öpper anders ussert ich ah?! 🤯")

st.sidebar.success("Meine Meinung zu bestimmten Themen, einfach klicken für Insights")

from PIL import Image
image = Image.open('apps/images/me.png')


st.image(image, caption='DISCLAIMER, sieht auf Foto freundlicher aus als in echt')

st.markdown(
    """
    ### Was passt denn em Guddi nid 😌?
    Einer der Hauptgründe, warum ich mich aktiv in der Politik engagieren will, ist, dass ich nach dem Studium schnell gemerkt habe, dass die Jobaussichten in Winterthur eher schlecht sind. Das sehen auch viele meiner Kolleginnen und Kollegen so, die bereits nach Zürich gezogen sind oder darüber nachdenken, dies zu tun. Ich persönlich bin ein absoluter Lokalpatriot und möchte auf keinen Fall nach Zürich ziehen. Aber ich kann meine Kollegen gut verstehen. Die Stadt mit dem global otreach dem See, den vielen interessanten Arbeitsplätzen und den umliegenden steuergünstigen Gemeinden hat durchaus ihren Reiz.
    Wenn Winterthur weiterhin so hoch verschuldet ist und eine Erhöhung des Steuerfusses die kreativste Lösung der Stadt ist dieses Problem in den Griff zu bekommen, werde ich wohl früher oder später auch mit dem Gedanken spielen, die Stadt zu verlassen. Ich kann es mir zwar kaum vorstellen, weil ich die MFW, den FCW und viele andere Dinge dieser Stadt zu sehr liebe, aber ich bin noch jung und es kann sich so viel ändern.
    
    Ein weiterer Grund sind persönliche Erfahrungen, die mich geprägt haben. Ich weiß, dass nicht nur eine solide Wirtschaft wichtig für eine Gesellschaft ist, sondern auch die Lebensqualität, die sich aus sozialen, sportlichen und kulturellen Angeboten ergibt, mindestens genauso wichtig ist. Als ich in der Sekundarschule St. Georgen war, musste ich eine Auszeit (Trampolin) nehmen. Das Trampolin und die Sportangebote des BCW gaben mir schließlich die richtige Richtung für meine Entwicklung. Aus meiner Sicht war ich aber nicht ganz alleine Schuld, dass ich ein Timeout absolvieren musste. Auch die Schule hat Fehler gemacht. Deshalb interessiere ich mich auch sehr für Bildung, Sozialarbeit und Sport, weil ich sie als wichtige Säulen für eine Gesellschaft sehe, die nicht in Gewinner und Verlierer unterteilt, sondern versucht, allen einen Platz zu geben.
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