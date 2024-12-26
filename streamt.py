import streamlit as st
from PIL import Image

# Title

st.title("hola mi primera app web streamlit")

st.header(" este es el header ")

st.subheader(" este es le subheader ")


st.success(" correcto ")
st.info(" esta es la información")
st.warning(" cuidado ")
st.error(" error de ejecución ")

# otras funciones

st.write(" para escribir texto plano")
st.write(range(2))
canal = "un canal "
st.write( "mi canal es ", canal)

# codigo
code_body= '''for i un range(50):
    print(i)'''
st.code(code_body,language='python')

if(st.checkbox("de acuerdo ")):
    st.text("Si esta de acuerdo ")

# radio
val = st.radio("seleccione el lenguaje ", ('python','java', 'java-scrpit'))
st.write(val, "fue seleccionado")

for i in range(2):
    st.write(i)

img =Image.open("3.jpg")
st.image(img)

option = st.selectbox("selecciones opción ", ['python','java','basic', 'html'])
st.write("se selecciono ", option)

options = st.multiselect("seleccione opciónes multiples ", ['python','java','basic', 'html'])
st.write(" uste selecciono las siguiente ")
for op in options:
    st.write(op)

nombre = st.text_input("escriba su nombre ","nombre?")
st.write(" Su nombre es :",nombre)

# boton

#st.button("oprimir ")
if(st.button("suscribase")):
    st.text("gracias por suscribirse")

valor = st.slider("seleccione valor ", 1000, 8000)
st.write(valor)

