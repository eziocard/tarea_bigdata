from Bdd import Bdd
import streamlit as st



tabla = Bdd('synthetic_data_usd.csv')
 
#tabla.get_tabla()
#print(tabla.get_name_columnas()[0])
#tabla.set_table()

titulo = st.title('Big Data Actividad Nro 2')
st.write(tabla.get_Df())
form = st.form(key='formulario',clear_on_submit=True)
agregar = {}

for col in range(len(tabla.get_name_columnas()) - 1):
    agregar[tabla.get_name_columnas()[col+1]] = form.text_input(f'Ingresar {tabla.get_name_columnas()[col+1]}:')

submit_button = form.form_submit_button("Ingresar")

if submit_button:
    st.write("Datos ingresados:")
    st.write(agregar)
    tabla.set_table(agregar)