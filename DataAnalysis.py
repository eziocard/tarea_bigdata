import pandas as pd

#from IPython.display import display

class DataAnalysis():
    def __init__(self,nombre):
        self.nombre = nombre
        self.df = pd.read_csv(self.nombre).fillna('No Especificado')

    def get_Df(self):
        self.df['Name'] = self.df['Name'].astype(str)
        self.df['Age'] = pd.to_numeric(self.df['Age'], errors='coerce').fillna(0).astype(int)  
        self.df['Salary'] = pd.to_numeric(self.df['Salary'], errors='coerce').fillna(0).astype(int)  
        self.df['Department'] = self.df['Department'].astype(str)  
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
            
    def set_table_borrar(self,indice):
        self.df = self.df.drop(indice)
        self.df.to_csv(self.nombre, index=False)
