from DataAnalysis import DataAnalysis
import streamlit as st
from datetime import datetime



tabla = DataAnalysis('synthetic_data_usd.csv')
 
agregar = {}
#tabla.get_tabla()
#print(tabla.get_name_columnas()[0])
#tabla.set_table()
tabs_1 = st.tabs(['Mostras base de datos', 'Graficos'])

with tabs_1[0]:
    st.title('Big Data Actividad Nro 2')
    st.write(tabla.get_Df())

with tabs_1[1]:
    st.write('Graficos')

with st.sidebar:
    tabs_2 = st.tabs(['Ingresar datos', 'Herramientas'])
    with tabs_2[0]:
        st.title("Ingresar Datos")
        form = st.form(key='formulario',clear_on_submit=True)
        with form:
            agregar['Name'] = form.text_input('Ingresar Nombre:')
            agregar['Age'] = form.number_input('Ingresar Edad:',min_value= 0,max_value= 120,value=0)
            agregar['Salary'] = form.number_input('Ingresar Salario:',min_value= 0,value=0)
            agregar['Department'] = form.text_input('Ingresar Departamento:')
            agregar['Join_Date'] = form.date_input('Ingresar la fecha de ingreso a la empresa',max_value=datetime.today().date())
            agregar['Location'] = form.text_input('Ingresar Ubicacion:')

        submit_button = form.form_submit_button("Ingresar")

        if submit_button:
            st.write("Datos ingresados con exito!")
            #st.write(agregar)
            tabla.set_table(agregar)
    with tabs_2[1]:
        st.title("Herramientas")
        st.write("Eliminar fila")
        form_h = st.form(key='formulario_eliminar',clear_on_submit=True)
        with form_h:
            input_indice = form_h.number_input('Ingresar Id:',min_value= 0,value=0)
            submit_button_borrar = form_h.form_submit_button("Borrar")
            if submit_button_borrar:
                tabla.set_table_borrar(input_indice)
                st.write("Fila eliminada.")