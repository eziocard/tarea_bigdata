import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns



class DataAnalysis():
    def __init__(self,nombre):
        self.nombre = nombre
        self.df = pd.read_csv(self.nombre).fillna('No Especificado')
       
        

    def get_Df(self):
        self.df['Name'] = self.df['Name'].astype(str)

        self.df['Age'] = pd.to_numeric(self.df['Age'], errors='coerce')
        mean_Age = self.get_mean('Age')
        self.df['Age'] = self.df['Age'].fillna(mean_Age).astype(int)
        self.df['Age'] = self.filtrar_edad()

        self.df['Salary'] = pd.to_numeric(self.df['Salary'], errors='coerce')
        mean_salary = self.get_mean('Salary')
        self.df['Salary'] = self.df['Salary'].fillna(mean_salary).astype(int)

        self.df['Department'] = self.df['Department'].astype(str)  

        self.df['Join_Date'] = pd.to_datetime(self.df['Join_Date'],format = 'mixed',yearfirst = True)
        self.df['Join_Date'] = self.df['Join_Date'].astype(str)  

        self.df['Location'] = self.df['Location'].astype(str)
       
    
        return self.df

    def get_name_columnas(self):       
        return self.df.columns.values

    def set_table(self,agregar):
        ultimo_valor = (self.df[self.get_name_columnas()[0]].iloc[-1]) + 1
        agregar[self.get_name_columnas()[0]] = ultimo_valor
        #agregar.update({self.get_name_columnas()[0] : ultimo_valor})
        agregar = pd.DataFrame([agregar])
        print(agregar)
        self.df = pd.concat([self.df, agregar], ignore_index=True)
        self.df.to_csv(self.nombre, index=False)
            
    def set_table_borrar(self,id):
        fila = self.df.loc[self.df['ID'] == id].index
        self.df = self.df.drop(fila)
        self.df.to_csv(self.nombre, index=False)

    def set_table_modificar(self,id,name,age,salary,department,join_date,location):
        fila = self.df.loc[self.df['ID'] == id].index
        self.df.iloc[fila, 1] = name
        self.df.iloc[fila, 2] = age
        self.df.iloc[fila, 3] = salary
        self.df.iloc[fila, 4] = department
        self.df.iloc[fila, 5] = join_date
        self.df.iloc[fila, 6] = location
        self.df.to_csv(self.nombre, index=False)

    def get_describe(self,nombre):   
        return self.df[nombre].describe()
    def get_moda(self,nombre):
        moda = self.df[nombre].mode()  
        moda = {'moda': moda}
        return moda
    def get_mean(self,nombre):
        return self.df[nombre].mean()
    
    def get_column(self,name):
        return self.df[name]
    def filtrar_edad(self):
        self.df.loc[(self.df['Age'] < 18) | (self.df['Age'] > 100), 'Age'] = self.get_mean('Age')
        return self.df['Age']
    def get_graficos(self,nombre):
        
        plt.figure(figsize=(15,15))
        fig, ax = plt.subplots(figsize=(15, 15))
        plt.subplot(1,1,1)
        sns.histplot(self.get_column(nombre),bins=100,kde=True,color="skyblue")
        plt.title('f{nombre} Distribucion')
        plt.xlabel(nombre)
        plt.ylabel('Frecuencia')
        st.pyplot(fig)

        plt.figure(figsize=(15,15))
        fig, ax = plt.subplots(figsize=(15, 15))
        plt.subplot(1,1,1)
        sns.boxplot(x=self.get_column(nombre))
        plt.title( plt.title('f{nombre} Distribucion'))
        st.pyplot(fig)