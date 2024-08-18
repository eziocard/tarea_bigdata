import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#from IPython.display import display

class DataAnalysis():
    def __init__(self,nombre):
        self.nombre = nombre
        self.df = pd.read_csv(self.nombre).fillna('No Especificado')
       
        

    def get_Df(self):
        self.df['Name'] = self.df['Name'].astype(str)
        self.df['Age'] = pd.to_numeric(self.df['Age'], errors='coerce').fillna(0).astype(int)  
        self.df['Salary'] = pd.to_numeric(self.df['Salary'], errors='coerce')
        mean_salary = self.get_mean('Salary')
        self.df['Salary'] = self.df['Salary'].fillna(mean_salary).astype(int)
        self.df['Department'] = self.df['Department'].astype(str)  
        self.df['Join_Date'] = pd.to_datetime(self.df['Join_Date'],format = 'mixed',yearfirst = True)
        self.df['Join_Date'] = self.df['Join_Date'].astype(str)  
        self.df['Location'] = self.df['Location'].astype(str)
       
    
        return self.df

    def get_tabla(self):
        print(self.df.tail())

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

    def get_describe_age(self):
        return self.df['Age'].describe()
    def get_describe_salary(self):
        return self.df['Salary'].describe()

    def get_mean(self,nombre):
        return self.df[nombre].mean()