import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np




class DataAnalysis():
    def __init__(self,nombre):
        self._nombre = nombre
        self._df = pd.read_csv(self._nombre).fillna('No Especificado')
        self.estandarizar()

    def estandarizar(self):
        self._df['Name'] = self._df['Name'].astype(str)
        self._df['Age'] = pd.to_numeric(self._df['Age'], errors='coerce')
        self._df['Salary'] = pd.to_numeric(self._df['Salary'], errors='coerce')
        mean_salary = self.get_mean('Salary')
        self._df['Department'] = self._df['Department'].astype(str)
        self._df['Join_Date'] = pd.to_datetime(self._df['Join_Date'], format='mixed', yearfirst=True)
        self._df['Location'] = self._df['Location'].astype(str)
    def get_Df(self):
        return self._df

    def get_Df_normalizada(self):
        self._df = pd.read_csv(self._nombre).fillna('No Especificado')
        self._df['Name'] = self._df['Name'].astype(str)
        self._df['Age'] = pd.to_numeric(self._df['Age'], errors='coerce')
        mean_Age = self.get_mean('Age')
        self._df['Age'] = self._df['Age'].fillna(mean_Age).astype(int)
        self._df['Age'] = self.filtrar_edad()
        self._df['Salary'] = pd.to_numeric(self._df['Salary'], errors='coerce')
        mean_salary = self.get_mean('Salary')
        self._df['Salary'] = self._df['Salary'].fillna(mean_salary).astype(int)
        self._df['Department'] = self._df['Department'].astype(str)
        self._df['Join_Date'] = pd.to_datetime(self._df['Join_Date'], format='mixed', yearfirst=True)
        self._df['Location'] = self._df['Location'].astype(str)
        return self._df

    def get_name_columnas(self):
        return self._df.columns.values

    def set_table(self,agregar):
        ultimo_valor = (self._df[self.get_name_columnas()[0]].iloc[-1]) + 1
        agregar[self.get_name_columnas()[0]] = ultimo_valor
        #agregar.update({self.get_name_columnas()[0] : ultimo_valor})
        agregar = pd.DataFrame([agregar])
        print(agregar)
        self._df = pd.concat([self._df, agregar], ignore_index=True)
        self._df.to_csv(self._nombre, index=False)
            
    def set_table_borrar(self,id):
        fila = self._df.loc[self._df['ID'] == id].index
        self._df = self._df.drop(fila)
        self._df.to_csv(self._nombre, index=False)

    def set_table_modificar(self,id,name,age,salary,department,join_date,location):
        fila = self._df.loc[self._df['ID'] == id].index
        self._df.iloc[fila, 1] = name
        self._df.iloc[fila, 2] = age
        self._df.iloc[fila, 3] = salary
        self._df.iloc[fila, 4] = department
        self._df.iloc[fila, 5] = join_date
        self._df.iloc[fila, 6] = location
        self._df.to_csv(self._nombre, index=False)

    def get_describe(self,nombre):   
        return self._df[nombre].describe()
    def get_moda(self,nombre):
        moda = self._df[nombre].mode()
        moda = {'moda': moda}
        return moda
    def get_mean(self,nombre):
        return self._df[nombre].mean()
    
    def get_column(self,name):
        return self._df[name]
    def filtrar_edad(self):
        self._df.loc[(self._df['Age'] < 18) | (self._df['Age'] > 100), 'Age'] = self.get_mean('Age')
        return self._df['Age']


    def get_graf_hisplot(self,nombre):
        plt.figure(figsize=(15, 15))
        fig, ax = plt.subplots(figsize=(15, 15))
        plt.subplot(1, 1, 1)
        sns.histplot(self.get_column(nombre), bins=100, kde=True, color="skyblue")
        plt.title(f'{nombre} Distribucion')
        plt.xlabel(nombre)
        plt.ylabel('Frecuencia')
        st.pyplot(fig)

    def get_graf_boxplot(self, name_column):
        plt.figure(figsize=(15, 15))
        fig, ax = plt.subplots(figsize=(15, 15))
        plt.subplot(1, 1, 1)
        sns.boxplot(x=self.get_column(name_column))
        plt.title(plt.title(f'{name_column} Distribucion'))
        st.pyplot(fig)

    def get_datetime(self):
        dates = self._df['Join_Date'].dt.year.value_counts()
        return dates

    def get_graf_datetime(self):
        dates = self.get_datetime()
        plt.figure(figsize=(15, 7))
        sns.barplot(x=dates.index, y=dates.values, color='skyblue')
        plt.title('Personas Ingresadas en Cada Año')
        plt.xlabel('Año')
        plt.ylabel('Número de Empleados')
        plt.xticks(rotation=45)
        st.pyplot(plt.gcf())

    ''' def get_corr_heatmap(self):
        df_number = self.df.select_dtypes(include=[np.number])
        corr = df_number.corr()
        plt.figure(figsize=(10, 8))
        sns.heatmap(corr, annot=True, cmap="coolwarm")
        st.pyplot(plt)
    '''

    def get_corr_heatmap(self):
        df_number = self._df.select_dtypes(include=[np.number]).drop('ID', axis=1)
        corr = df_number.corr()
        plt.figure(figsize=(10, 8))
        sns.heatmap(corr, annot=True, cmap="coolwarm")
        st.pyplot(plt)

    def get_scatterplot(self, col1, col2):
        df_number = self._df.select_dtypes(include=[np.number, 'datetime']).drop('ID', axis=1)
        plt.figure(figsize=(10, 6))
        sns.scatterplot(data=df_number, x=col1, y=col2, palette='viridis')
        plt.title(f"Relación entre {col1} y {col2}")
        plt.xlabel(col1)
        plt.ylabel(col2)
        st.pyplot(plt)

    def get_pairplot(self):
        df_number = self._df.select_dtypes(include=[np.number, 'datetime']).drop('ID', axis=1)
        sns.pairplot(df_number)
        st.pyplot(plt)