from DataAnalysis import DataAnalysis
import streamlit as st
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns




tabla = DataAnalysis('synthetic_data_usd.csv')
st.set_page_config(page_title="Tarea base de datos")

agregar = {}
#tabla.get_tabla()
#print(tabla.get_name_columnas()[0])
#tabla.set_table()
tabs_1 = st.tabs(['Mostras base de datos', 'Analisis de datos','Analisis de Series Temporales','Grafico Heatmap','Grafico Scatterplot'])

with tabs_1[0]:
    st.title('Big Data Actividad Nro 2')
    st.dataframe(tabla.get_Df().set_index("ID"))


    

with tabs_1[1]:
    st.write('Analisis de Datos')
    col1,col2 =st.columns(2)
    with col1:
        st.write('Age')
        st.write(tabla.get_describe('Age'))
        st.dataframe(tabla.get_moda('Age'))
        tabla.get_graf_hisplot('Age')
        tabla.get_graf_boxplot('Age')
 


    with col2:
        st.write('Salary')
        st.write(tabla.get_describe('Salary'))
        st.dataframe(tabla.get_moda('Salary'))
        tabla.get_graf_hisplot('Salary')
        tabla.get_graf_boxplot('Salary')
        
with tabs_1[2]:
    st.write("Cantidad de personas ingresadas por año")
    dates = tabla.get_datetime()
    tabla.get_graf_datetime()
with tabs_1[3]:
    tabla.get_corr_heatmap()
with tabs_1[4]:
    tabla.get_scatterplot("Join_Date", "Salary")
    tabla.get_scatterplot("Join_Date", "Age")
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

        st.write("Modificar")
        form_m = st.form(key='formulario_modificar',clear_on_submit=True)
        with form_m:
            id = form_m.number_input('Ingresar ID:',min_value= 0,value=0)
            name = form_m.text_input('Ingresar Nombre:')
            age = form_m.number_input('Ingresar Edad:',min_value= 0,max_value= 120,value=0)
            salary = form_m.number_input('Ingresar Salario:',min_value= 0,value=0)
            department = form_m.text_input('Ingresar Departamento:')
            join_date = form_m.date_input('Ingresar la fecha de ingreso a la empresa',max_value=datetime.today().date())
            location = form_m.text_input('Ingresar Ubicacion:')
            submit_button_modificar = form_m.form_submit_button("Modificar")
            if submit_button_modificar:
                if (not name or not department or not location or id == 0 or age == 0 or salary == 0 or join_date == ""):
                    st.warning("Error faltan datos")
                else:
                    tabla.set_table_modificar(id,name,age,salary,department,join_date,location)
                    st.write("Fila Modificada.")

    

